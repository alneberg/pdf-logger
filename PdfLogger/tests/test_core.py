#!/usr/bin/env python
import unittest
from nose.tools import assert_almost_equal, assert_equal,\
    assert_is_none
import os
import tempfile

from pdflogger.core import init

class TestCore(object):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # testing function: init
    def test_init(self):
        with tempfile.NamedTemporaryFile() as tmp_file:
            sg.print_group_contigs(tmp_file)
            tmp_file.seek(0)
            contig_seqs = list(SeqIO.parse(tmp_file, "fasta"))
            assert_equal(len(contig_seqs),10)
            assert_equal(contig_seqs[0].id, "Capnocytophaga_canimorsus_Cc5_uid70727_10")

