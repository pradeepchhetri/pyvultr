# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestRecord(BaseTest):

    def setUp(self):
        super(TestRecord, self).setUp()
        self.record = pyvultr.lib.Record(
            domain_name="example.in",
            recordid=3586458,
            token=self.token
        )

    @responses.activate
    def test_load(self):
        data = self.load_from_file('record/list.json')

        url = self.base_url + 'dns/records'
        domain_uri = '?domain=example.in'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        self.record.load()
        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/records" + domain_uri)
        self.assertEqual(self.record.type, "A")
        self.assertEqual(self.record.data, "127.0.0.1")
        self.assertEqual(self.record.ttl, 300)

if __name__ == '__main__':
    unittest.main()
