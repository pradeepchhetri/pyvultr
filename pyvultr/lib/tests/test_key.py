# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestKey(BaseTest):

    def setUp(self):
        super(TestKey, self).setUp()
        self.key = pyvultr.lib.Key(token=self.token)

    @responses.activate
    def test_get_auth(self):
        data = self.load_from_file('auth/info.json')

        url = self.base_url + 'auth/info'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        key = self.key.get_object(self.token)

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "auth/info")
        self.assertEqual(key.token, self.token)
        self.assertEqual(key.acls, [ "subscriptions","billing",
                                     "support","provisioning" ])
        self.assertEqual(key.email, "example@vultr.com")
        self.assertEqual(key.name, "Example Account")

if __name__ == '__main__':
    unittest.main()
