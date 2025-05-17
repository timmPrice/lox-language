from lox import error
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
        while not self.isAtEnd():
            self.start = current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))   # append end-of-line token after scanning loop
        return self.tokens

    def isAtEnd(self):
        return self.current >= len(self.source):

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
            case "!": 
                if self.match("="):
                    self.add_token(TokenType.BANG_EQUAL)
                else:
                    self.add_token(TokenType.BANG)
            case "=": 
                if self.match("="):
                    self.add_token(TokenType.EQUAL_EQUAL)
                else:
                    self.add_token(TokenType.EQUAL)
            case "<":
                if self.match("="):
                    self.add_token(TokenType.GREATER_EQUAL)
                else:
                    self.add_token(TokenType.GREATER)
            case ">":
                if self.match("="):
                    self.add_token(TokenType.LESS_EQUAL)
                else:
                    self.add_token(TokenType.LESS)
            case "/": 
                if self.match("/"):
                    while(self.peek() != "\n" && not self.isAtEnd()):
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case _: error(line, "Unexpected Character")

    def advance(self) -> str:
        c = self.source[self.current]
        self.current += 1
        return c 
    
    def add_token(self, a_type: TokenType, literal: Any = None) -> str:
        text = self.source[self.start:self.current]
        self.tokens.append(Token(a_type, text, literal, self.line))

    def match(self, expected: str) -> bool:
        if not self.isAtEnd():
            return False
        if source[current] != expected:
            return False

        current++
        return True

    def peek(self) -> str: 
        if self.isAtEnd():
            return "/0"
        return source[current]
