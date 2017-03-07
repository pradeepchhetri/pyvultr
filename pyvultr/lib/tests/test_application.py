# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestApplication(BaseTest):

    def setUp(self):
        super(TestApplication, self).setUp()
        self.application = pyvultr.lib.Application(token=self.token)

    @responses.activate
    def test_get_application(self):
        data = self.load_from_file('application/list.json')

        url = self.base_url + 'app/list'
        responses.add(responses.GET, url,
                      body=data,
                      status=200,
                      content_type='application/json')

        app = self.application.get_object(self.token, "GitLab")

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "app/list")
        self.assertEqual(key.APPID, "5")
        self.assertEqual(key.name, "GitLab")
        self.assertEqual(key.short_name, "gitlab")
        self.assertEqual(key.deploy_name, "GitLab on CentOS 6 x64")
        self.assertEqual(key.surcharge, 0)

if __name__ == '__main__':
    unittest.main()
