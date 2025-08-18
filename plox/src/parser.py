from src import token_type
from token_type import TokenType
from token import Token
from lox import error
from expr import Binary, Expr, Unary, Literal, Grouping


class ParserError(RuntimeError):
    pass

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0
  
    def expression(self) -> Expr:
        return self.equality()
    
    def equality(self) -> Expr:
        expr: Expr = self.comparison()

        while (self.match(Token.BANG_EQUAL, Token.EQUAL_EQUAL)):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr = Binary(expr, operator, right) 

        return expr

    def comparison(self) -> Expr:
        expr: Expr = self.term()
        
        while (self.match(Token.GREATER, Token.GREATER_EQUAL, Token.LESS, Token.LESS_EQUAL)):
            operator: Token = self.previous()
            right: Expr = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self) -> Expr:
        expr: Expr = self.factor()

        while (self.match(Token.MINUS, Token.PLUS)):
            operator: Token = self.previous()
            right: Expr = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self) -> Expr:
        expr: Expr = self.unary()

        while (self.match(Token.SLASH, Token.STAR)):
            operator: Token = self.previous()
            right: Expr = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self) -> Expr:

        if (self.match(Token.BANG, Token.MINUS)):
            operator: Token = self.previous()
            right: Expr = self.unary()
            return Unary(operator, right)

        return self.primary()

    def primary(self) -> Expr:
        if self.match(Token.FALSE):
            return Literal(False)
        if self.match(Token.TRUE):
            return Literal(True)
        if self.match(Token.NULL):
            return Literal(None)

        if (self.match(Token.STRING, Token.NUMBER)):
            return Literal(self.previous().literal)

        if (self.match(Token.LEFT_PAREN)):
            expr = self.expression()
            self.consume(Token.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

        raise ParserError("Expected Expression")

    def match(self, *types: TokenType) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, token_type: TokenType) -> bool:
        if self.is_at_end():
            return False
        return type(self.peek()) == token_type

    def advance(self) -> Token:
        if (self.is_at_end):
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return type(self.peek()) == 'EOF' 

    def peek(self) -> Token:
        return self.tokens[self.current + 1]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, type: TokenType, message: str) -> Token:
        if (self.check(type)):
            return self.advance()
        raise ValueError(self.peek(), message)

    def _error(self, token: Token, message: str): 
        error(token, message)
        raise ParserError()
