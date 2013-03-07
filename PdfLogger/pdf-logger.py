#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The pdf-logger main script"""
import fileinput
import sys
import os
import re

from pdflogger.parser import main_parser

def main(args, di):
    for file_name in os.listdir(di):
        if re.match(".+_log.tex$",file_name):
            args.log_file_name = file_name
            break
    if args.func.__name__ != "init":
        try:
            with open(os.path.join(di,args.log_file_name),'r+') as log_file:
                args.log_file = log_file
                args.func(args)
        except AttributeError:
            sys.stderr.write('No log file initialized\n')
            
    else:
        args.dir = di
        args.func(args)


if __name__=="__main__":
    parser = main_parser()
    args = parser.parse_args()

    if args.verbose:
        print >> sys.stderr, "parameters: %s" %(args)

    path=os.getcwd()
    
    main(args,path)
