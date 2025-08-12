from token_type import TokenType
from token import Token
from expr import Binary, Expr

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0
  
    def expression(self) -> Expr:
        return self.equality()
    
    def equality(self) -> Expr:
        expr: Expr = comparison()

        while (self.match(Token.BANG_EQUAL, Token.EQUAL_EQUAL)):
            operator: Token = self.previous()
            right: Expr = comparison()
            expr = Binary(expr, operator, right) 

        return expr

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
