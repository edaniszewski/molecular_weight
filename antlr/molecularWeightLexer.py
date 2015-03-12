# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\4\16\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\3\6\3\13\n\3\r\3")
        buf.write(u"\16\3\f\2\2\4\3\3\5\4\3\2\4\6\2EEJJQQUU\3\2\62;\16\2")
        buf.write(u"\3\3\2\2\2\2\5\3\2\2\2\3\7\3\2\2\2\5\n\3\2\2\2\7\b\t")
        buf.write(u"\2\2\2\b\4\3\2\2\2\t\13\t\3\2\2\n\t\3\2\2\2\13\f\3\2")
        buf.write(u"\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\6\3\2\2\2\4\2\f\2")
        return buf.getvalue()


class molecularWeightLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    ELEMENT = 1
    QTY = 2

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
 ]

    symbolicNames = [ u"<INVALID>",
            u"ELEMENT", u"QTY" ]

    ruleNames = [ u"ELEMENT", u"QTY" ]

    grammarFileName = u"molecularWeight.g4"

    def __init__(self, input=None):
        super(molecularWeightLexer, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


