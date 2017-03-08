# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

class Error(Exception):
    """
    Base exception class
    """
    pass

class DataReadError(Error):
    """
    Error while reading data
    """
    pass

class JSONReadError(Error):
    """
    Error while reading JSON
    """
    pass

class NoTokenError(Error):
    """
    No Api-Key provided
    """
    pass

class InvalidTokenError(Error):
    """
    Invalid Api-Key provided
    """
    pass

class InvalidAPIError(Error):
    """
    HTTP Resource not found
    """
    pass

class InvalidHTTPMethodError(Error):
    """
    Invalid HTTP method invoked
    Allowed: GET, POST
    """
    pass

class RequestFailedError(Error):
    """
    Failed HTTP Request, check the
    response body for detail
    """
    pass

class InternalServerError(Error):
    """
    Internal Server Error
    """
    pass

class RateLimitHitError(Error):
    """
    Reached rate-limits,
    Limit: 2 req/sec (avg)
    """
    pass
