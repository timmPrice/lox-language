from token import Token
from abc import ABC, abstractmethod

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor'):
         pass

class Visitor(ABC):
    @abstractmethod
    def visit_binary_expr(self, expr: 'Binary'):
        pass

    @abstractmethod
    def visit_grouping_expr(self, expr: 'Grouping'):
        pass

    @abstractmethod
    def visit_literal_expr(self, expr: 'Literal'):
        pass

    @abstractmethod
    def visit_unary_expr(self, expr: 'Unary'):
        pass

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
       self.left = left
       self.operator = operator
       self.right = right

class Grouping(Expr):
    def __init__(self, expression: Expr):
       self.expression = expression

class Literal(Expr):
    def __init__(self, value: object):
       self.value = value

class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
       self.operator = operator
       self.right = right

