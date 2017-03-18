# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest

from pyvultr.lib.exceptions import *

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

    def test_400(self):
        url = self.base_url + "status/400"
        self.assertRaises(InvalidAPIError, lambda: self.base_api.get_data(url))

    def test_403(self):
        url = self.base_url + "status/403"
        self.assertRaises(InvalidTokenError, lambda: self.base_api.get_data(url))

    def test_405(self):
        url = self.base_url + "status/405"
        self.assertRaises(InvalidHTTPMethodError, lambda: self.base_api.get_data(url))

    def test_412(self):
        url = self.base_url + "status/412"
        self.assertRaises(RequestFailedError, lambda: self.base_api.get_data(url))

    def test_500(self):
        url = self.base_url + "status/500"
        self.assertRaises(InternalServerError, lambda: self.base_api.get_data(url))

    def test_503(self):
        url = self.base_url + "status/503"
        self.assertRaises(RateLimitHitError, lambda: self.base_api.get_data(url))

    def tearDown(self):
        pass
