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
            token=self.token
        )

    
