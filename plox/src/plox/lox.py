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
            run_file(args[0])
        else: 
            run_prompt()

    @staticmethod
    def run_file(path: str) -> None:
        filepath = Path(path)
        source = filepath.read_text(encoding="utf-8")
        run(source)
       
    @staticmethod
    def run_prompt() -> None:
        while True:
            try:
                line = input("> ")
                if line.strip() == "":
                    continue
                run(line)
            except EOFError:
                break

    @staticmethod
    def run(source: str) -> None:
        tokens = source.split() # this will be real tokenizaiton later

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None: 
        report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}" , file=sys.stderr)
        had_error = true


if __name__ == "__main__":
    Lox.main(sys.argv[1:])
