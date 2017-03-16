# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestDomain(BaseTest):

    def setUp(self):
        super(TestDomain, self).setUp()
        self.domain = pyvultr.lib.Domain(
            domain="example.in",
            token=self.token
        )

    @responses.activate
    def test_load(self):
        data = self.load_from_file('domain/list.json')

        url = self.base_url + 'dns/list'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        self.domain.load()
        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/list")
        self.assertEqual(self.domain.domain, "example.in")
        self.assertEqual(self.domain.date_created, "2017-03-16 05:33:49")

    @responses.activate
    def test_create(self):
        data = self.load_from_file('domain/single.json')

        url = self.base_url + 'dns/create_domain'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        domain = pyvultr.lib.Domain(
            domain="example.in",
            serverip="127.0.0.1",
            token=self.token
        ).create()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/create_domain")
        self.assertEqual(domain.domain, "example.in")
        self.assertEqual(domain.serverip, "127.0.0.1")

    @responses.activate
    def test_delete(self):
        url = self.base_url + 'dns/delete_domain'
        responses.add(responses.POST,
                      url,
                      status=200,
                      content_type='application/json')

        domain = pyvultr.lib.Domain(
            domain="example.in",
            token=self.token
        ).delete()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/delete_domain")
        self.assertEqual(domain.domain, "example.in")

if __name__ == '__main__':
    unittest.main()
