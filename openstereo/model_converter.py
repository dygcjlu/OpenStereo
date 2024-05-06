

from utils import config_loader, init_seeds, get_msg_mgr



def arg_parse():
    parser = argparse.ArgumentParser(description='Main program for OpenStereo.')
    parser.add_argument('--config', type=str, default='configs/psmnet/PSMNet_sceneflow.yaml',
                        help="path of config file")
    parser.add_argument('--scope', default='train', choices=['train', 'val', 'test_kitti', 'onnx'],
                        help="choose train or test scope")
    parser.add_argument('--master_addr', type=str, default='localhost', help="master address")
    parser.add_argument('--master_port', type=str, default='12355', help="master port")
    parser.add_argument('--no_distribute', action='store_true', default=False, help="disable distributed training")
    parser.add_argument('--log_to_file', action='store_true',
                        help="log to file, default path is: output/<dataset>/<model>/<save_name>/<logs>/<Datetime>.txt")
    parser.add_argument('--device', type=str, default='cuda', help="device to use for non-distributed mode.")
    parser.add_argument('--restore_hint', type=str, default=0, help="restore hint for loading checkpoint.")
    opt = parser.parse_args()
    return opt






if __name__ == '__main__':
    opt = arg_parse()
    cfgs = config_loader(opt.config)
    is_dist = not opt.no_distribute
    if is_dist:
        print("Distributed mode.")
        world_size = torch.cuda.device_count()
        mp.spawn(worker, args=(world_size, opt, cfgs), nprocs=world_size)
    else:
        print("Non-distributed mode.")
        worker(0, None, opt, cfgs)
