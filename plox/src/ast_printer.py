from .token import Token
from .expr import Expr, Visitor, Binary, Grouping, Literal, Unary

class ASTPrinter(Visitor[str]):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)
   
    def visit_binary_expr(self, expr: Binary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: Grouping) -> str:
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: Literal) -> str:
        if (expr.value == None):
            return "nil"
        return str(expr.value)

    def visit_unary_expr(self, expr: Unary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        parts = " ".join(expr.accept(self) for expr in exprs)
        return f"({name} {parts})" 
