# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
import requests
import ujson as json


class SharQClient(object):
    """Provides methods to interact with SharQ server."""

    def __init__(self, host, port=80, scheme='http'):
        """Configures and constructs the SharQClient"""
        self._rs = requests.Session()
        self._rs.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self._url = '%s://%s:%s' % (scheme, host, port)

    def enqueue(self, **params):
        """Enqueues a job in SharQ server."""
        response = self._rs.post(
            '%s/enqueue/' % self._url, data=json.dumps(params))
        return (response.status_code, json.loads(response.text))

    def dequeue(self, **params):
        """Dequeues a job from SharQ server."""
        response = self._rs.post(
            '%s/dequeue/' % self._url, data=json.dumps(params))
        return (response.status_code, json.loads(response.text))

    def finish(self, **params):
        """Marks a job as successfully completed in SharQ server."""
        response = self._rs.post(
            '%s/finish/' % self._url, data=json.dumps(params))
        return (response.status_code, json.loads(response.text))
