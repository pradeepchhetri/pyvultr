# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestVolume(BaseTest):

    def setUp(self):
        super(TestVolume, self).setUp()
        self.volume = pyvultr.lib.Volume(
            subid=1313217,
            token=self.token
        )

    @responses.activate
    def test_load(self):
        data = self.load_from_file('volume/list.json')

        url = self.base_url + 'block/list'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        self.volume.load()
        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "block/list")
        self.assertEqual(self.volume.subid, 1313217)
        self.assertEqual(self.volume.date_created, "2016-31-29 10:10:48")
        self.assertEqual(self.volume.cost_per_month, 5)
        self.assertEqual(self.volume.status, "active")
        self.assertEqual(self.volume.size_gb, 50)
        self.assertEqual(self.volume.dcid, 1)
        self.assertEqual(self.volume.attached_to_subid, 1313207)
        self.assertEqual(self.volume.label, "files2")

    @responses.activate
    def test_create(self):
        data = self.load_from_file('volume/single.json')

        url = self.base_url + 'block/create'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        volume = pyvultr.lib.Volume(
            dcid=1,
            size_gb=10,
            token=self.token
        ).create()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "block/create")
        self.assertEqual(volume.size_gb, 10)
        self.assertEqual(volume.dcid, 1)

if __name__ == '__main__':
    unittest.main()
