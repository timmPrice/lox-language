import sys 
from pathlib import Path 


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
        if had_error:
            sys.exit(65)
       
    @staticmethod
    def run_prompt() -> None:
        while True:
            try:
                line = input("> ")
                if line.strip() == "":
                    continue
                Lox.run(line)
                had_error = false
            except EOFError:
                break

    @staticmethod
    def run(source: str) -> None:
        tokens = source.split() # this will be real tokenizaiton later

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None: 
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}" , file=sys.stderr)
        Lox.had_error = true


if __name__ == "__main__":
    Lox.main(sys.argv[1:])
