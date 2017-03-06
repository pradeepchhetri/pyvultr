# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
import unittest

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.vultr.com/v1/"
        self.token = "afaketokenthatwillworksincewemockthings"

    def load_from_file(self, json_file):
        cwd = os.path.dirname(__file__)
        fpath = os.path.join(cwd, 'data/%s' % json_file)
        with open(fpath, 'r') as f:
            return f.read()
