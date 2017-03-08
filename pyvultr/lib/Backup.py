# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

try:
    from builtins import itervalues
except ImportError:
    from six import itervalues

from .baseapi import BaseAPI

class Backup(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.date_created = None
        self.description = None
        self.size = None
        self.status = None

        super(Backup, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, backup_id):
        """
        Class method that will return a Backup object by ID.
        """
        backup = cls(token=api_token, id=backup_id)
        backup.load()
        return backup

    def load(self):
        """
        Documentation: https://www.vultr.com/api/#backup_backup_list
        """
        backups = self.get_data("backup/list")

        for desc in itervalues(backups):
            if desc["BACKUPID"] == self.id:
                for attr in desc.keys():
                    setattr(self, attr, desc[attr])

    def __str__(self):
        return "<Backup: %s>" % (self.id)
