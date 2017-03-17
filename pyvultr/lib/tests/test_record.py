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

    @responses.activate
    def test_create(self):
        data = self.load_from_file('record/single.json')

        url = self.base_url + 'dns/create_record'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        record = pyvultr.lib.Record(
            domain_name="example.in",
            name="vultr",
            type="A",
            data="192.168.100.1",
            token=self.token
        ).create()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/create_record")
        self.assertEqual(record.domain, "example.in")
        self.assertEqual(record.name, "vultr")
        self.assertEqual(record.type, "A")
        self.assertEqual(record.data, "192.168.100.1")

    @responses.activate
    def test_delete(self):
        data = self.load_from_file('record/single.json')

        url = self.base_url + 'dns/delete_record'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        record = pyvultr.lib.Record(
            domain_name="example.in",
            recordid=3586458,
            token=self.token
        ).delete()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/delete_record")
        self.assertEqual(record.domain, "example.in")
        self.assertEqual(record.name, None)
        self.assertEqual(record.type, None)
        self.assertEqual(record.data, None)

    @responses.activate
    def test_update(self):
        data = self.load_from_file('record/single.json')

        url = self.base_url + 'dns/update_record'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        record = pyvultr.lib.Record(
            domain_name="example.in",
            name="vultr",
            type="A",
            data="192.168.100.2",
            token=self.token
        ).update()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "dns/update_record")
        self.assertEqual(record.domain, "example.in")
        self.assertEqual(record.name, "vultr")
        self.assertEqual(record.type, "A")
        self.assertEqual(record.data, "192.168.100.2")

if __name__ == '__main__':
    unittest.main()
