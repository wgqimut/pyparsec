#!/usr/bin/env python3
# coding:utf-8

import unittest
from parsec import *

simple = "It is a simple string."

class TestState(unittest.TestCase):
    def test_next(self):
        st = BasicState(simple)
        for i in range(len(simple)):
            idx = st.index
            re = st.next()
            self.assertEqual(re, st.data[idx])
        with self.assertRaises(Exception) as err:
            st.next()
        self.assertTrue(issubclass(type(err.exception), error.ParsecEof))

if __name__ == '__main__':
    unittest.main()
