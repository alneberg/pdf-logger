#!/usr/bin/env python
import unittest
from nose.tools import assert_almost_equal, assert_equal,\
    assert_is_none
import os
import tempfile
import sys

from pdflogger.parser import main_parser
from pdflogger.content import section, subsection, add_content

class TestContent(object):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # testing function: main
    def test_section(self):

        parser = main_parser()
        args = parser.parse_args(['section','temp_header'])

        with tempfile.NamedTemporaryFile(suffix='_log.tex') as tmp_file:
            di = '\tmp'
            with open(os.path.join(di,tmp_file.name),'r+') as f:
                args.log_file = f
                section(args)
                f.seek(0)
                first_line = f.readline()
                true_first_line = r"\section{temp_header}"
                assert_equal(true_first_line, first_line)

    def test_subsection(self):

        parser = main_parser()
        args = parser.parse_args(['subsection','temp_header'])

        with tempfile.NamedTemporaryFile(suffix='_log.tex') as tmp_file:
            di = '\tmp'
            with open(os.path.join(di,tmp_file.name),'r+') as f:
                args.log_file = f
                subsection(args)
                f.seek(0)
                first_line = f.readline()
                true_first_line = r"\subsection{temp_header}"
                assert_equal(true_first_line, first_line)


    def test_main_add_content(self):
        pass
