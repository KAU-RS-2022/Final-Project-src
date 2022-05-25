import os
import logging
import torch
import torch.nn as nn
import torch.nn.init as initer
import torch.distributed as torch_dist
from PIL import Image
import numpy as np


def merge_config(cfg, args):
    cfg.defrost()
    
    if args.config is not None:
        cfg.merge_from_file(args.config)
    if args.opts is []:
        cfg.merge_from_list(args.opts)
    cfg.SYS.OUTPUT_DIR = 'results/' + cfg.SYS.EXP_NAME + '/'
    cfg.freeze()

    return cfg

def update_config(cfg, args):
    cfg.defrost()
    
    cfg.merge_from_list(args)
    
    cfg.freeze()

    return cfg

def get_logger(path):
    
    logger_name = 'main-logger'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    fmt = "[%(asctime)s %(levelname)s %(filename)s line %(lineno)d %(process)d] %(message)s"
    
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    
    file_handler = logging.FileHandler(path)
    logger.addHandler(file_handler)
    
    return logger



class AverageMeter(object):
    """
        code is from pytorch imagenet examples
        Computes and stores the average and current value
    """
    def __init__(self, name, fmt=':f'):
        self.name = name
        self.fmt = fmt
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        # print(val, n)
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

    def __str__(self):
        fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
        return fmtstr.format(**self.__dict__)



def adjust_learning_rate(optimizer, base_lr, max_iters, cur_iters, nbb_lr=0, power=0.9):
    """
        code is from pytorch imagenet examples
        Sets the learning rate to the initial LR decayed with poly learning rate with power 0.9
    """
    steps = ((1-float(cur_iters)/max_iters)**(power))
    
    lr = base_lr * steps
    optimizer.param_groups[0]['lr'] = lr

    if len(optimizer.param_groups) == 2:
        lr2 = nbb_lr * steps
        optimizer.param_groups[1]['lr'] = lr2

    return lr

def check_mkdir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
def check_makedirs(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
def colorize(gray, palette):
    # gray: numpy array of the label and 1*3N size list palette

    color = Image.fromarray(gray).convert('P')
    color.putpalette(palette)
    return color