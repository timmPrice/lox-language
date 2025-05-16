from token_type import TokenType 
from token import Token
from typing import List, Any

class Scanner:
    def __init__(self, source: str):
        self.source = source 
        self.tokens: List[Token] = []
        self.current = 0
        self.start = 0
        self.line = 1

    def scan_tokens(self) -> List[Token]:
        while(self.current <= len(self.source))
            self.start = current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self) -> None:
        c = self.advance()
        match c:
            case "(": self.add_token(TokenType.LEFT_PAREN)
            case ")": self.add_token(TokenType.RIGHT_PAREN)
            case "{": self.add_token(TokenType.LEFT_BRACE)
            case "}": self.add_token(TokenType.RIGHT_BRACE)
            case ",": self.add_token(TokenType.COMMA)
            case ".": self.add_token(TokenType.DOT)
            case "-": self.add_token(TokenType.MINUS)
            case "+": self.add_token(TokenType.PLUS)
            case ";": self.add_token(TokenType.SEMICOLON)
            case "*": self.add_token(TokenType.STAR)

    def advance(self) -> str:
        c = self.source[self.current]
        self.current += 1
        return c 
    
    def add_token(self, a_type: TokenType, literal: Any = None) -> str:
        text = self.source[self.start:self.current]
        tokens.append(Token(a_type, text, literal, self.line))
