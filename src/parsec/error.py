#!/usr/bin/env python3
# coding:utf-8

class ParsecError(Exception):
    def __init__(self, state, message):
        self.index = state.index
        self.message = message
    def __str__(self):
        return "Error at {0}: {1}".format(self.index, self.message)

class ParsecEof(ParsecError):
    def __init__(self, state):
        ParsecError.__init__(self, state, "eof")
        # self.index = state.index
        # self.message = "eof"
