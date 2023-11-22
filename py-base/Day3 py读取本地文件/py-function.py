# coding=utf-8
import requests
import json
import logging

logger = logging.getLogger('webapp')


class RemoteRequests(object):

    def __init__(self,
                 address="127.0.0.1",
                 protocol="http",
                 port="8080",
                 timeout=10):
        self.address = address
        self.protocol = protocol
        self.port = port
        self.timeout = timeout
        self.base_url = self.protocol + "://" + self.address + ":" + self.port
        self.headers = {"Content-Type": "application/json"}

    def get(self, api_url, params):
        try:
            data = requests.get(
                url=self.base_url + api_url
            )
            return data.json()
        except Exception as e:
            logger.error("err")
