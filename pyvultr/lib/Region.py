# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

try:
    from builtins import itervalues
except ImportError:
    from six import itervalues

from .baseapi import BaseAPI, GET

class Region(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.dcid = None
        self.name = None
        self.country = None
        self.continent = None
        self.state = None
        self.ddos_protection = None
        self.block_storage = None
        self.regioncode = None

        super(Region, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, name):
        """
        Class method that will return a Region object by name.
        """
        region = cls(token=api_token, name=name)
        region.load()
        return region

    def load(self):
        """
        Documentation: https://www.vultr.com/api/#regions_region_list
        """
        regions = self.get_data("regions/list")

        for desc in itervalues(regions):
            if desc["name"] == self.name:
                for attr in desc.keys():
                    setattr(self, attr.lower(), desc[attr])

        return self

    def availability(self):
        """
        Documentation: https://www.vultr.com/api/#regions_region_available
        """
        input_params = {
            DCID': self.dcid
        }

        available_vpsids = self.get_data(
            "regions/availability",
            type=GET,
            params=input_params
        )

        return available_vpsids

    def __str__(self):
        return "<Region: %s %s>" % (self.regioncode, self.name)
