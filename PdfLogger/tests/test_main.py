#!/usr/bin/env python
import unittest
from nose.tools import assert_almost_equal, assert_equal,\
    assert_is_none
import os
import tempfile
import sys
from StringIO import StringIO
sys.path.append('../')
pdflogger_main = __import__("pdf-logger")
main = pdflogger_main.main
from pdflogger.parser import main_parser


class TestMain(object):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # testing function: main
    def test_main_with_log_file(self):

        parser = main_parser()
        args = parser.parse_args(['section','temp_header'])

        with tempfile.NamedTemporaryFile(suffix='_log.tex') as tmp_file:
            di = '/tmp'
            main(args,di)
            tmp_file.seek(0)
            first_line = tmp_file.readline()
            true_first_line = r"\section{temp_header}"
            assert_equal(true_first_line, first_line)

    def test_main_without_log_file(self):

        parser = main_parser()
        args = parser.parse_args(['subsection','temp_header'])

        saved_stderr = sys.stderr
        try:
            out = StringIO()
            sys.stderr = out
            di = '/tmp'
            main(args,di)
            output = out.getvalue().strip()

            assert_equal(output,"No log file initialized")
        finally:
            sys.stderr = saved_stderr


    def test_main_add_content(self):
        pass
