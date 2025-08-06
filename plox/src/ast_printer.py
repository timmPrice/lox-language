from expr import Expr, Visitor

class ast_printer(Visitor[str]):
    def print(self, expr: Expr[str]) -> str:
        return expr.accept(self)


