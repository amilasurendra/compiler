#!/usr/bin/env python2

import sys

from lexer.lexer import Lexer
from exceptions.exceptions import EndOfFileErrorException, CompilerSyntaxErrorException, CompilerLexErrorException
from parser.parser import Parser

def process_arguments():
    if len(sys.argv) != 2:
        print "Usage:\n     " , sys.argv[0] , "<input_file>\n"
        sys.exit(1);

    filename = sys.argv[1]

    return filename

def main():
    filename = process_arguments()

    with open(filename) as filebuffer:

        try:
            lex = Lexer(filebuffer)
            parser = Parser(lex)
            parser.P()

        except EndOfFileErrorException:
            print "Syntax error at line " + str(lex.line)

        except CompilerSyntaxErrorException as e:
            print e
        except CompilerLexErrorException as e:
            print e

if __name__ == '__main__':
    main()
