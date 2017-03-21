# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestRegion(BaseTest):

    def setUp(self):
        super(TestRegion, self).setUp()
        self.region = pyvultr.lib.Region(
            name="New Jersey",
            token=self.token
        )

    @responses.activate
    def test_load(self):
        data = self.load_from_file('region/list.json')

        url = self.base_url + 'regions/list'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        self.region.load()
        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "regions/list")
        self.assertEqual(self.region.dcid, "1")
        self.assertEqual(self.region.country, "US")
        self.assertEqual(self.region.continent, "North America")
        self.assertEqual(self.region.state, "NJ")
        self.assertEqual(self.region.regioncode, "EWR")

    @responses.activate
    def test_availability(self):
        data = self.load_from_file('region/availability.json')

        url = self.base_url + 'regions/availability'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        domain_uri = '?DCID=12'

        availability = pyvultr.lib.Region(
            name="New Jersey",
            dcid="12",
            token=self.token
        ).availability()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "regions/availability" + domain_uri)

if __name__ == '__main__':
    unittest.main()
