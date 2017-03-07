# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pyvultr
import pyvultr.lib
import unittest
import responses

from .BaseTest import BaseTest

class TestBackup(BaseTest):

    def setUp(self):
        super(TestBackup, self).setUp()
        self.backup = pyvultr.lib.Backup(token=self.token)

    @responses.activate
    def test_get_backup(self):
        data = self.load_from_file('backup/list.json')

        url = self.base_url + 'backup/list'
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        app = self.backup.get_object(self.token, "543d34149403a")

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "backup/list")
        self.assertEqual(app.BACKUPID, "543d34149403a")
        self.assertEqual(app.date_created, "2014-10-14 12:40:40")
        self.assertEqual(app.description, "Automatic server backup")
        self.assertEqual(app.size, "42949672960")
        self.assertEqual(app.status, "complete")

if __name__ == '__main__':
    unittest.main()
