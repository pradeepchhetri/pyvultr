#!/usr/bin/env python

import pyvultr
import unittest
import responses

from .BaseTest import BaseTest

class TestAccount(BaseTest):

    def setUp(self):
        super(TestAccount, self).SetUp()
        self.account = pyvultr.Account(token=self.token)

    @responses.activate
    def test_get_account(self):
        data = self.load_from_file('account/info.json')

        url = self.base_url + 'account/info'
        responses.add(responses.GET, url,
                      body=data,
                      status=200,
                      content_type='application/json')

        acct = self.account.get_object()

        self.assertEqual(responses.calls[0].request.url,
                         self.base_url + "account/info")
        self.assertEqual(acct.token, self.token)
        self.assertEqual(acct.balance, "-5519.11")
        self.assertEqual(acct.pending_charges, "57.03")
        self.assertEqual(acct.last_payment_date, "2014-07-18 15:31:01")
        self.assertEqual(acct.last_payment_amount, "-1.00")

if __name__ == '__main__':
    unittest.main()
