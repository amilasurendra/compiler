#!/usr/bin/env python2

class EndOfFileErrorException(Exception):
    def __str__(self):
        return repr("End of File")

class CompilerSyntaxErrorException(Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        return ("Syntax error at line " + str(self.line))

class CompilerLexErrorException(Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        return ("Syntax error at line " + str(self.line))

