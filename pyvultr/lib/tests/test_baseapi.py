# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest

class TestBaseAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://httpbin.org/"
        self.token = "afaketokenthatwillworksincewemockthings"
        self.base_api = pyvultr.lib.BaseAPI(
            token=self.token
        )

    def test_200(self):
        url = self.base_url + "status/200"
        data = self.base_api.get_data(url)
        self.assertEqual(data, {})

    def tearDown(self):
        pass
