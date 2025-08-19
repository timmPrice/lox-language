import sys 
from pathlib import Path 
from .lox_scanner import Scanner
from .parser import Parser
from .ast_printer import ASTPrinter 

class Lox:
    had_error = False
    
    @staticmethod
    def main(args):          
        if len(args) > 1:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(args) == 1:
            Lox.run_file(args[0])
        else: 
            Lox.run_prompt()

    @staticmethod
    def run_file(path: str) -> None:
        filepath = Path(path)
        source = filepath.read_text(encoding="utf-8")
        Lox.run(source)
        if Lox.had_error:
            sys.exit(65)
       
    @staticmethod
    def run_prompt() -> None:
        while True:
            try:
                line = input("> ")
                if line.strip() == "":
                    continue
                Lox.run(line)
                Lox.had_error = False 
            except EOFError:
                break

    @staticmethod
    def run(source: str) -> None:
        scanner = Scanner(source, Lox.error)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens, Lox.error)
        expression = parser.parse()

        if Lox.had_error or expression is None:
            return 

        print(ASTPrinter().print(expression))

    @staticmethod
    def error(line: int, message: str) -> None: 
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}" , file=sys.stderr)
        Lox.had_error = True 

if __name__ == "__main__":
    Lox.main(sys.argv[1:])
