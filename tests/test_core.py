#!/usr/bin/env python
import unittest
from nose.tools import assert_almost_equal, assert_equal,\
    assert_is_none
import os
import tempfile
import shutil

from pdflogger.core import init, title_to_file_name
from pdflogger.parser import main_parser

class TestCore(object):
    def __init__(self):
        self.tmp_dir = None

    def setUp(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.tmp_dir =  os.path.join(cur_dir,'tmp')

    def tearDown(self):
        log_dir = self.tmp_dir =  os.path.join(self.tmp_dir,'log')
        if os.path.exists(log_dir):
            shutil.rmtree(log_dir)
        
    # testing function: init
    def test_init_creates_log_directory(self):
        tmp_dir = self.tmp_dir
        parser = main_parser()
        args = parser.parse_args(['init','my_temp_log_file', '--author=testing_author'])
        args.dir = tmp_dir
        init(args)
        tmp_dir_list = os.listdir(tmp_dir)
        assert_equal(("log" in tmp_dir_list),True)

    def test_init_creates_log_file(self):
        tmp_dir = self.tmp_dir
        parser = main_parser()
        args = parser.parse_args(['init','my_temp_log_file', '--author=testing_author'])
        args.dir = tmp_dir
        init(args)
        log_dir = os.path.join(tmp_dir,'log')
        log_dir_list = os.listdir(log_dir)
        assert_equal(("my_temp_log_file_log.tex" in log_dir_list),True)

    def test_init_inserts_template(self):
        tmp_dir = self.tmp_dir
        parser = main_parser()
        args = parser.parse_args(['init','my_temp_log_file', '--author=testing_author'])
        args.dir = tmp_dir
        init(args)
        log_file = os.path.join(tmp_dir,'log/my_temp_log_file_log.tex')
        log = open(log_file,'r')
        tex_string = log.read()
        assert_equal(r"\begin{document}" in tex_string, True)
        assert_equal(r"\title{my_temp_log_file}" in tex_string, True)
        assert_equal(r"\author{testing_author}" in tex_string, True)
        
    def test_title_to_file_name(self):
        first = "My nice Title"
        second = "MyniceTitle"
        assert_equal(title_to_file_name(first),"my_nice_title_log.tex")
        assert_equal(title_to_file_name(second),"mynicetitle_log.tex")
