from antlr.molecularWeightListener import molecularWeightListener


class Listener(molecularWeightListener):

    def __init__(self, weights):
        assert(isinstance(weights, dict))
        self.weights = weights
        self.total = 0

    @property
    def get_total(self):
        total = self.total
        self.total = 0
        return total

    def enterElements(self, ctx):
        """
        Enter a parse tree produced by molecularWeightParser#elements.

        :type ctx: ElementsContext
        """
        self.total += self.weights[str(ctx.ELEMENT().getText())] * int(ctx.QTY().getText() if ctx.QTY() is not None else 1)