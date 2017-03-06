# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI

class Account(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.balance = None
        self.pending_charges = None
        self.last_payment_date = None
        self.last_payment_amount = None

        super(Account, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token):
        """
            Class method that will return an Account object.
        """
        acct = cls(token=api_token)
        acct.load()
        return acct

    def load(self):
        """
            Documentation: https://www.vultr.com/api/#account_info
        """
        account = self.get_data("account/info")
        for attr in account.keys():
            setattr(self, attr, account[attr])

    def __str__(self):
        return "<%s>" % self.__class__.__name__
