from .token import Token
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

R = TypeVar('R')

class Expr(ABC, Generic[R]):
    @abstractmethod
    def accept(self, visitor: 'Visitor[R]') -> R:
         pass

class Visitor(ABC, Generic[R]):
    @abstractmethod
    def visit_binary_expr(self, expr: 'Binary') -> R:
        pass

    @abstractmethod
    def visit_grouping_expr(self, expr: 'Grouping') -> R:
        pass

    @abstractmethod
    def visit_literal_expr(self, expr: 'Literal') -> R:
        pass

    @abstractmethod
    def visit_unary_expr(self, expr: 'Unary') -> R:
        pass

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
       self.left = left
       self.operator = operator
       self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visit_binary_expr(self)
 
class Grouping(Expr):
    def __init__(self, expression: Expr):
       self.expression = expression

    def accept(self, visitor: Visitor):
        return visitor.visit_grouping_expr(self)
 
class Literal(Expr):
    def __init__(self, value: object):
       self.value = value

    def accept(self, visitor: Visitor):
        return visitor.visit_literal_expr(self)
 
class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
       self.operator = operator
       self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visit_unary_expr(self)
 
