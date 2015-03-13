# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .molecularWeightListener import molecularWeightListener
else:
    from molecularWeightListener import molecularWeightListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\4\20\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\3\3")
        buf.write(u"\3\5\3\16\n\3\3\3\2\2\4\2\4\2\2\17\2\7\3\2\2\2\4\13\3")
        buf.write(u"\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2")
        buf.write(u"\2\t\n\3\2\2\2\n\3\3\2\2\2\13\r\7\3\2\2\f\16\7\4\2\2")
        buf.write(u"\r\f\3\2\2\2\r\16\3\2\2\2\16\5\3\2\2\2\4\t\r")
        return buf.getvalue()


class molecularWeightParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ u"<INVALID>", u"ELEMENT", u"QTY" ]

    RULE_molecule = 0
    RULE_elements = 1

    ruleNames =  [ u"molecule", u"elements" ]

    EOF = Token.EOF
    ELEMENT=1
    QTY=2

    def __init__(self, input):
        super(molecularWeightParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MoleculeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(molecularWeightParser.MoleculeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def elements(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(molecularWeightParser.ElementsContext)
            else:
                return self.getTypedRuleContext(molecularWeightParser.ElementsContext,i)


        def getRuleIndex(self):
            return molecularWeightParser.RULE_molecule

        def enterRule(self, listener):
            if isinstance( listener, molecularWeightListener ):
                listener.enterMolecule(self)

        def exitRule(self, listener):
            if isinstance( listener, molecularWeightListener ):
                listener.exitMolecule(self)




    def molecule(self):

        localctx = molecularWeightParser.MoleculeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_molecule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.elements()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==molecularWeightParser.ELEMENT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(molecularWeightParser.ElementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ELEMENT(self):
            return self.getToken(molecularWeightParser.ELEMENT, 0)

        def QTY(self):
            return self.getToken(molecularWeightParser.QTY, 0)

        def getRuleIndex(self):
            return molecularWeightParser.RULE_elements

        def enterRule(self, listener):
            if isinstance( listener, molecularWeightListener ):
                listener.enterElements(self)

        def exitRule(self, listener):
            if isinstance( listener, molecularWeightListener ):
                listener.exitElements(self)




    def elements(self):

        localctx = molecularWeightParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(molecularWeightParser.ELEMENT)
            self.state = 11
            _la = self._input.LA(1)
            if _la==molecularWeightParser.QTY:
                self.state = 10
                self.match(molecularWeightParser.QTY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




