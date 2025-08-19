from .token_type import TokenType
from .token import Token
from .expr import Binary, Expr, Unary, Literal, Grouping


class ParserError(RuntimeError):
    pass

class Parser:
    def __init__(self, tokens: list[Token], error_handler):
        self.tokens = tokens
        self.current = 0
        self.error_handler = error_handler

    def parse(self):
        try:
            return self.expression()
        except ParserError:
            return None
  
    def expression(self) -> Expr:
        return self.equality()
    
    def equality(self) -> Expr:
        expr: Expr = self.comparison()

        while (self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL)):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr = Binary(expr, operator, right) 

        return expr

    def comparison(self) -> Expr:
        expr: Expr = self.term()
        
        while (self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL)):
            operator: Token = self.previous()
            right: Expr = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self) -> Expr:
        expr: Expr = self.factor()

        while (self.match(TokenType.MINUS, TokenType.PLUS)):
            operator: Token = self.previous()
            right: Expr = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self) -> Expr:
        expr: Expr = self.unary()

        while (self.match(TokenType.SLASH, TokenType.STAR)):
            operator: Token = self.previous()
            right: Expr = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self) -> Expr:

        if (self.match(TokenType.BANG, TokenType.MINUS)):
            operator: Token = self.previous()
            right: Expr = self.unary()
            return Unary(operator, right)

        return self.primary()

    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)

        if (self.match(TokenType.STRING, TokenType.NUMBER)):
            return Literal(self.previous().literal)

        if (self.match(TokenType.LEFT_PAREN)):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

        raise ParserError(f"{self.peek()} Expected Expression")

    def match(self, *types: TokenType) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, token_type: TokenType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF 

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, type: TokenType, message: str) -> Token:
        if (self.check(type)):
            return self.advance()
        raise ValueError(self.peek(), message)

    def _error(self, token: Token, message: str): 
        self.error_handler(token, message)
        raise ParserError()

    def synchronize(self):
        self.advance();

        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return
        
        match self.peek().type:
            case TokenType.CLASS \
                | TokenType.FUN \
                | TokenType.FOR \
                | TokenType.WHILE \
                | TokenType.PRINT \
                | TokenType.VAR \
                | TokenType.IF \
                | TokenType.RETURN:
                return

        self.advance()
