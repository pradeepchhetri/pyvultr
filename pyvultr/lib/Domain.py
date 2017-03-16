# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI, GET, POST

class Domain(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.domain = None
        self.serverip = None
        self.date_created = None

        super(Domain, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, domain_name):
        """
        Class method that will return a Domain object by Name.
        """
        domain = cls(token=api_token, domain=domain_name)
        domain.load()
        return domain

    def load(self):
        """
        Documentation: https://www.vultr.com/api/#dns_dns_list
        """
        domains = self.get_data("dns/list")

        for domain in domains:
            if domain["domain"] == self.domain:
                for attr in domain.keys():
                    setattr(self, attr, domain[attr])

        return self

    def create(self):
        """
        Creates a domain name in DNS. (https://www.vultr.com/api/#dns_create_domain)

        Args:
            domain: string - Domain name to create.
            serverip: string - Server IP to use while creating default records (A and MX)
        """
        input_params = {
            'domain': self.domain,
            'serverip': self.serverip
        }

        data = self.get_data(
            "dns/create_domain",
            type=POST,
            params=input_params
        )

        return self

    def delete(self):
        """
        Delete a domain name and all associated records. (https://www.vultr.com/api/#dns_delete_domain)

        Args:
            domain: string - Domain name to delete.
        """
        input_params = {
            'domain': self.domain
        }

        data = self.get_data(
            "dns/delete_domain",
            type=POST,
            params=input_params
        )

        return self

    def __str__(self):
        return "<Domain: %s>" % (self.domain)
