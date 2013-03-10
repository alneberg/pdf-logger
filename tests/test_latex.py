#!/usr/bin/env python
import unittest
from nose.tools import assert_almost_equal, assert_equal,\
    assert_is_none
import os
import tempfile
import sys
import re

from pdflogger.parser import main_parser
from pdflogger.content import section, subsection, add_content
from pdflogger.core import latex_template

class TestContent(object):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    # testing constructor: LatexFile
    def test_latex_file(self):
        dir = os.path.dirname(__file__)
        file_name = os.path.join(dir,"fixtures/basic_latex.tex")
        latex_file = LatexFile(file_name)
        assert_equal(latex_file.file_name, file_name)

        last_section(latex_file)
    # testing function: last_section
    def test_last_section(self):

    # testing function: last_subsection
    def test_last_subsection(self):
        pass
    
    # testing function: insert
    def test_insert(self):
        pass
