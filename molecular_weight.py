from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4 import ParseTreeWalker

from antlr.molecularWeightParser import molecularWeightParser
from antlr.molecularWeightLexer import molecularWeightLexer
from listener import Listener


class MolecularWeight(object):
    """
    MolecularWeight contains methods to process a given string representation of a molecule into its molecular weight.
    """
    def __init__(self, weights):
        self.listener = Listener(weights)
        self.walker = ParseTreeWalker()

    def process(self, molecule):
        """
        Determine the molecular weight of a given molecule.

        :param molecule: String representing the molecule to be processed
        :type molecule: str
        """
        parse_tree = self._parse_molecule(molecule)
        self.walker.walk(self.listener, parse_tree)
        return self.listener.get_total

    @staticmethod
    def _parse_molecule(molecule):
        """
        Parse the molecule string with the ANTLR grammar, resulting in a parse tree

        :param molecule: String representing the molecule to be processed
        :type molecule: str
        """
        input_stream = InputStream(molecule)
        lexer = molecularWeightLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = molecularWeightParser(stream)
        return parser.molecule()