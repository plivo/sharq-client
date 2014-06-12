# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
import requests
import ujson as json


class BadParameterException(Exception):
    pass


class SharQClient(object):

    """Provides methods to interact with SharQ server."""

    def __init__(self, host, port=80, scheme='http'):
        """Configures and constructs the SharQClient"""
        self._rs = requests.Session()
        self._rs.headers = {
            'Accept': 'application/json'
        }
        self._url = '%s://%s:%s' % (scheme, host, port)

    def enqueue(self, **params):
        """Enqueues a job in SharQ server."""
        try:
            queue_type = params.pop('queue_type')
            queue_id = params.pop('queue_id')
        except KeyError as e:
            return (400, {
                'status': 'failure',
                'message': '`%s` is a mandatory parameter' % e.message})

        response = self._rs.post(
            '%s/enqueue/%s/%s/' % (self._url, queue_type, queue_id),
            data=json.dumps(params),
            headers={'Content-Type': 'application/json'})
        return (response.status_code, json.loads(response.text))

    def dequeue(self, **params):
        """Dequeues a job from SharQ server."""
        queue_type = params.pop('queue_type', 'default')
        response = self._rs.get(
            '%s/dequeue/%s/' % (self._url, queue_type))
        return (response.status_code, json.loads(response.text))

    def finish(self, **params):
        """Marks a job as successfully completed in SharQ server."""
        try:
            queue_type = params.pop('queue_type')
            queue_id = params.pop('queue_id')
            job_id = params.pop('job_id')
        except KeyError as e:
            return (400, {
                'status': 'failure',
                'message': '`%s` is a mandatory parameter' % e.message})

        response = self._rs.post(
            '%s/finish/%s/%s/%s/' % (self._url, queue_type, queue_id, job_id))
        return (response.status_code, json.loads(response.text))
