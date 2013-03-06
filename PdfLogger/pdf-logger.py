#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The pdf-logger main script"""
import fileinput
import sys
from argparse import ArgumentParser

def init(args):
    print args.title

def section(args):
    print args.header

def subsection(args):
    print args.header

def add_content(args):
    print args.script_file

if __name__=="__main__":
    parser = ArgumentParser(\
        description=""" The pdf-logger """)
    parser.add_argument('-v', '--verbose', action='store_true',
        help='information written to stderr during execution.')

    subparsers = parser.add_subparsers()

    parser_init = subparsers.add_parser('init')
    parser_init.add_argument('title', help='The title of the log file that will be created')
    parser_init.set_defaults(func=init)

    parser_section = subparsers.add_parser('section')
    parser_section.add_argument('header', help="The section header that will be created")
    parser_section.set_defaults(func=section)

    parser_subsection = subparsers.add_parser('subsection')
    parser_subsection.add_argument('header', help="The subsection header that will be created")
    parser_subsection.set_defaults(func=subsection)

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('script_file', \
                                help='The script file that will be logged')
    parser_add.add_argument('-c','--caption',
                            type=str, help='Specify an optional caption for the code')
    parser_add.set_defaults(func=add_content)

    args = parser.parse_args()

    if args.verbose:
        print >> sys.stderr, "parameters: %s" %(args)
    
    args.func(args)
