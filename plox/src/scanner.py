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

    keywords = {
        "and": TokenType.AND,
        "class":TokenType.CLASS ,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "fun": TokenType.FUN,
        "for": TokenType.FOR,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE,
    }

    def scan_tokens(self) -> List[Token]:
        while not self.isAtEnd():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))   # append end-of-line token after scanning loop
        return self.tokens

    def isAtEnd(self):
        return self.current >= len(self.source)

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
                    while(self.peek() != "\n" and not self.isAtEnd()):
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case " " | "\r" | "\t":
                pass
            case "\n":
                self.line += 1
            case '"':
                self.string()
            case _: 
                if c.isdigit():
                    self.number()
                elif:
                    self.identifier()
                else:
                    error(self.line, "Unexpected Character")

    def advance(self) -> str:
        c = self.source[self.current]
        self.current += 1
        return c 
    
    def add_token(self, a_type: TokenType, literal: Any = None) -> None:
        text = self.source[self.start:self.current]
        self.tokens.append(Token(a_type, text, literal, self.line))

    def match(self, expected: str) -> bool:
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self) -> str: 
        if self.isAtEnd():
            return "\0"
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 == len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def string(self) -> None:
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == "\n":
                self.line += 1
                self.advance()

        if self.isAtEnd():
            error(self.line, "Unterminated String")
            return

        self.advance() # consume closing """
        value = self.source[self.start + 1:self.current - 1] # exclude quotes
        self.add_token(TokenType.STRING, value)

    def number(self) -> None:
        while self.peek().isdigit():
            self.advance()

        if self.peek() == "." and self.peek_next().isdigit():
            self.advance() # consume the "."
            while self.peek().isdigit():
                self.advance()
       
        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def isAlpha(self, c: str) -> bool:
        return c.isalpha() or c == "_":

   def isAlphaNumeric(self, c: str) -> bool:
       return self.isAlpha(c) or c.isdigit():
    
    def identifier(self) -> None:
        while self.isAlphaNumeric(self.peek()):
            self.advance()

        self.add_token(TokenType.IDENTIFIER)


