#!/usr/bin/env python3
# coding:utf-8

class Parsec(object):
    def __init__(self, parsec):
        self.parsec = parsec
    def __call__(self, state):
        return self.parsec(state)
    def bind(self, continuation):
        def bind(state):
            return continuation(self.parsec(state))
        return Monad(bind)
    def then(self, p):
        def then(state):
            self.parsec(state)
            return p(state)
        return Monad(then)
    def over(self, p):
        def over(state):
            re = self.parsec(state)
            p(state)
            return re
        return Monad(over)
