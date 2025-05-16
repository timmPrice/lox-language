from token_type import TokenType 
from token import Token
from typing import List
from typing import Any

class Scanner:
    def __init__(self, source: str):
        self.source = source 
        self.tokens: List[Token] = []
        self.current = 0
        self.start = 0
        self.line = 1

    def scan_tokens(self) -> List[Token]:
        while(current <= len(self.source))
            start = current
            # scan token
        tokens = self.token
        tokens.append(Token(EOF, "", null, line))
        return tokens

    def scan_token(self) -> None:
        c = advance()

    def advance() -> str:
        return source[current++]
    
    def add_token(self, a_type: TokenType, literal: Any) -> str:
        text: str = source[start:current]
        tokens.append(Token(a_type, text, literal, line))
