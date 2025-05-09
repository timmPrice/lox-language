import sys
from pathlib import Path 

def main(args):          
    if len(args) > 1:
        print("Usage: plox [script]")
        sys.exit(64)
    elif len(args) == 1:
        runFile(args[0])
    else: 
        runPompt()

def runFile(path: str) -> None:
    filepath = Path(path)
    source = filepath.read_text(encoding="utf-8")
    run(source)
   
def runPrompt -> None:
    while True:
        try:
            line = input("> ")
            if line.strip() == "":
                continue
            run(line)
        except EOFError:
            break

def run(source: str) -> None:
    tokens[] = source.split() # this will be real tokenizaiton later

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main(sys.argv1[1:])
