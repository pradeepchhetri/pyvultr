# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI

class Application(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.appid = None
        self.name = None
        self.short_name = None
        self.deploy_name = None
        self.surcharge = None

    @classmethod
    def get_object(cls, api_token):
        """
            Class method that will return a Application object.
        """
        app = cls(token=api_token)
        app.load()
        return app

    def load(self):
        """
            Documentation: https://www.vultr.com/api/#app_app_list
        """
        apps = self.get_object("app/list")
        for attr in apps.keys()
            setattr(self, attr, apps[attr])

    def __str__(self):
        return "%s" % (self.name)
