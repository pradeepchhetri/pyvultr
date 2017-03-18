# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
import json
import logging
import requests
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from .exceptions import DataReadError
from .exceptions import JSONReadError
from .exceptions import NoTokenError
from .exceptions import InvalidTokenError
from .exceptions import InvalidAPIError
from .exceptions import InvalidHTTPMethodError
from .exceptions import RequestFailedError
from .exceptions import InternalServerError
from .exceptions import RateLimitHitError

GET = 'GET'
POST = 'POST'
REQUEST_TIMEOUT = 'PYTHON_VULTR_REQUEST_TIMEOUT_IN_SEC'

class BaseAPI(object):
    """
    Basic api class for Vultr APIs.
    """
    token = ""
    end_point = "https://api.vultr.com/v1/"

    def __init__(self, *args, **kwargs):
        self.token = ""
        self.end_point = "https://api.vultr.com/v1/"
        self._log = logging.getLogger(__name__)

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

    def __perform_request(self, url, type=GET, params=None):
        """
        This method will perform the real request,
        in this way we can customize only the "output"
        of the API call by using self.__call_api method.
        This method will return the request object.
        """
        if params is None:
            params = {}

        if not self.token:
            raise NoTokenError("No token provided. Please use a valid token")

        url = urljoin(self.end_point, url)

        # lookup table to find out the apropriate requests method,
        # headers and payload type (json or query parameters)
        identity = lambda x: x
        json_dumps = lambda x: json.dumps(x)
        lookup = {
            GET:  (
                    requests.get,
                    {},
                    'params',
                    identity
                  ),
            POST: (
                    requests.post,
                    {'Content-type': 'application/json'},
                    'data',
                    json_dumps
                  ),
        }

        requests_method, headers, payload, transform = lookup[type]
        headers.update({'API-Key': self.token})
        kwargs = {'headers': headers, payload: transform(params)}

        timeout = self.get_timeout()
        if timeout:
            kwargs['timeout'] = timeout

        # remove token from log
        headers_str = str(headers).replace(self.token.strip(), 'TOKEN')

        self._log.debug('%s %s %s:%s %s %s'
                        % (type,
                           url,
                           payload,
                           params,
                           headers_str,
                           timeout))

        return requests_method(url, **kwargs)

    def get_timeout(self):
        """
        Checks if any timeout for the requests to Vultr is required.
        To set a timeout, use the REQUEST_TIMEOUT environment
        variable.
        """
        timeout_str = os.environ.get(REQUEST_TIMEOUT)
        if timeout_str:
            try:
                return float(timeout_str)
            except:
                self._log.error('Failed parsing the request read timeout of '
                                '"%s". Please use a valid float number!'
                                % (timeout_str))
        return None

    def get_data(self, url, type=GET, params=None):
        """
        This method is a basic implementation of __call_api that checks
        errors too. In case of success the method will return True or the
        content of the response to the request.
        """
        if params is None:
            params = dict()

        req = self.__perform_request(url, type, params)
        print(len(req.content))

        if req.status_code == 400:
            raise InvalidAPIError()

        if req.status_code == 403:
            raise InvalidTokenError()

        if req.status_code == 405:
            raise InvalidHTTPMethodError()

        if req.status_code == 412:
            raise RequestFailedError()

        if req.status_code == 500:
            raise InternalServerError()

        if req.status_code == 503:
            raise RateLimitHitError()

        try:
            if len(req.content) == 0:
                data = {}
            else:
                data = req.json()
        except ValueError as e:
            raise JSONReadError(
                'Read failed from Vultr: %s' % str(e)
            )

        if not req.ok:
            msg = [data[m] for m in ("id", "message") if m in data][1]
            raise DataReadError(msg)

        return data

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode__(self):
        return u"%s" % self.__str__()

    def __repr__(self):
        return str(self)
