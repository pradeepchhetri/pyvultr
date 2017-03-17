# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI, GET, POST

class Record(BaseAPI):
    def __init__(self, domain_name=None, *args, **kwargs):
        self.domain = domain_name if domain_name else ""
        self.recordid = None
        self.name = None
        self.type = None
        self.data = None
        self.ttl = None
        self.priority = None

        super(Record, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, domain, recordid):
        """
        Class method that will return a Record object by ID and domain.
        """
        record = cls(token=api_token, domain=domain, recordid=recordid)
        record.load()
        return record

    def create(self):
        """
        Create a record for a domain.

        Args:
            domain: string - Domain name to add record to
            name: string - Name (subdomain) of record
            type: string - Type (A, AAAA, MX, etc) of record
            data: string - Data for this record

        Optional Args:
            ttl: integer - TTL of this record
            priority: integer - Priority of this record (only required for MX and SRV)
        """
        input_params = {
            'domain': self.domain,
            'name': self.name,
            'type': self.type,
            'data': self.data,
            'ttl': self.ttl,
            'priority': self.priority
        }

        data = self.get_data(
            "dns/create_record",
            type=POST,
            params=input_params
        )

        return self

    def delete(self):
        """
        Delete a record for a domain.

        Args:
            domain: string - Domain name to delete record from
            recordid: integer - ID of record to delete
        """
        input_params = {
            'domain': self.domain,
            'RECORDID': self.recordid
        }

        data = self.get_data(
            "dns/delete_record",
            type=POST,
            params=input_params
        )

        return self

    def update(self):
        """
        Update a record for a domain.

        Args:
            domain: string - Domain name to update record from
            recordid: integer - ID of record to update

        Optional Args:
            name: string - Name (subdomain) of record
            data: string - Data for this record
            ttl: integer - TTL of this record
            priority: integer - Priority of this record (only required for MX and SRV)
        """
        input_params = {
            'domain': self.domain,
            'RECORDID': self.domain,
            'name': self.name,
            'data': self.data,
            'ttl': self.ttl,
            'priority': self.priority
        }

        data = self.get_data(
            "dns/update_record",
            type=POST,
            params=input_params
        )

        return self
