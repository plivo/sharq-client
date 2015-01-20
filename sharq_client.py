# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
import requests
import json


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

    def interval(self, **params):
        """Updates the interval of a queue for a particular type."""
        try:
            queue_type = params.pop('queue_type')
            queue_id = params.pop('queue_id')
            interval = params.pop('interval')
        except KeyError as e:
            return (400, {
                'status': 'failure',
                'message': '`%s` is a mandatory parameter' % e.message})

        params = {
            'interval': interval
        }

        response = self._rs.post(
            '%s/interval/%s/%s/' % (self._url, queue_type, queue_id),
            data=json.dumps(params),
            headers={'Content-Type': 'application/json'})
        return (response.status_code, json.loads(response.text))


    def metrics(self, **params):
        """Fetches various metrics from SharQ server."""
        queue_type = params.pop('queue_type', None)
        queue_id = params.pop('queue_id', None)

        if not queue_type and not queue_id:
            response = self._rs.get(
                '%s/metrics/' % (self._url))
        elif queue_type and not queue_id:
            response = self._rs.get(
            '%s/metrics/%s/' % (self._url, queue_type))
        elif not queue_type and queue_id:
            # invalid case
            return (400, {
                'status': 'failure',
                'message': '`queue_id` should be accompanied by `queue_type`.'})
        elif queue_type and queue_id:
            response = self._rs.get(
                '%s/metrics/%s/%s/' % (self._url, queue_type, queue_id))

        return (response.status_code, json.loads(response.text))