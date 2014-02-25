#!/usr/bin/env python2

from lexer.tag import Tag
from exceptions.exceptions import CompilerSyntaxErrorException, EndOfFileErrorException

class Parser (object):
    def __init__(self, lexer):
        self.lex = lexer
        self.move()

    def move(self):
        self.look = self.lex.scan()

    def match(self, tag):
        if self.look.tag == tag:
            self.move()
            return
        else:
            raise CompilerSyntaxErrorException(self.lex.line)

    def P(self):
        self.D()
        self.L()

    def D(self):
        self.B()
        self.N()
        self.match(Tag.END)
        try:
            self.D()
        except CompilerSyntaxErrorException:
            pass

    def B(self):
            self.match(Tag.BASIC)

    def N(self):
        self.match(Tag.ID)
        self.N1()

    def N1(self):
        try:
            self.match(Tag.COMMA)
        except CompilerSyntaxErrorException:
            return

        self.match(Tag.ID)
        self.N1()

    def L(self):
        self.S()
        try:
            self.match(Tag.END)
        except EndOfFileErrorException:
            pass

        try:
            self.L()
        except CompilerSyntaxErrorException:
            pass

    def S(self):
        try:
            self.match(Tag.ID)
        except CompilerSyntaxErrorException:
            self.E()
            return

        self.match(Tag.ASSIGN)
        self.E()

    def E(self):
        self.T()
        self.E1()

    def E1(self):
        try:
            self.match(Tag.ADD)
        except CompilerSyntaxErrorException:
            return

        self.T()
        self.E1()

    def T(self):
        self.F()
        self.T1()

    def T1(self):
        try:
            self.match(Tag.MUL)
        except CompilerSyntaxErrorException:
            return

        self.F()
        self.T1()

    def F(self):
        try:
            self.match(Tag.OPEN_PARAN)
        except CompilerSyntaxErrorException:
            try:
                self.match(Tag.NUM)
            except CompilerSyntaxErrorException:
                self.match(Tag.ID)
            return

        self.E()
        self.match(Tag.CLOSE_PARAN)
