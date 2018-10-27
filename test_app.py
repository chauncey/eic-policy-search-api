#!/usr/bin/env python3

import os
import app as eic_status
import unittest


class EicPolicySearch(unittest.TestCase):
    def setUp(self):
        self.app = eic_status.app.test_client()
        self.version = "v1.0"

    def test_echo(self):
        '''Test that echo returns a result'''
        resp = self.app.get("/echo")
        assert 'result' in resp.data.decode('utf-8')

    def test_hello_world(self):
        '''Test the obligatory Hello, World response'''
        resp = self.app.get("/")
        assert 'Hello, World!' == resp.data.decode('utf-8')


if __name__ == "__main__":
    unittest.main()
