# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI

class Key(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.acl = None
        self.name = None
        self.email = None

        super(Key, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token):
        """
            Class method that will return a Key object.
        """
        key = cls(token=api_token)
        key.load()
        return key

    def load(self):
        """
            Documentation: https://www.vultr.com/api/#auth_info
        """
        key = self.get_object("auth/info")
        for attr in key.keys()
            setattr(self, attr, key[attr])

    def __str__(self):
        return "<API Key: %s %s>" % (self.name, self.email)
