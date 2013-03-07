import os

def init(args):
    log_dir = os.path.join(args.dir,'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_path = os.path.join(log_dir,args.title + '_log.tex')
    log_file = open(log_file_path, 'w+')
    log_file.close()
