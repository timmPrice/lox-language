import os

def define_visitor(base_name: str, types: list[str], file):
    print("class Visitor(ABC, Generic[R]):", file = file)
    for type_def in types:
        class_name = type_def.split(":")[0].strip()
        print("    @abstractmethod", file = file)
        print(f"    def visit_{class_name.lower()}_{base_name.lower()}(self, expr: '{class_name}') -> R:", file = file)
        print("        pass", file = file)
        print("", file = file)

def define_ast(output_dir: str, base_name: str, types: list[str]):
    path = os.path.join(output_dir, f"{base_name.lower()}.py")
    with open(path, "w") as file:
        print("from token import Token", file = file)
        print("from abc import ABC, abstractmethod", file = file)
        print("from typing import Generic, TypeVar", file = file)
        print("", file = file)
        print("R = TypeVar('R')", file = file)
        print("", file = file)
        print(f"class {base_name}(ABC, Generic[R]):", file = file)
        print(f"    @abstractmethod", file = file) 
        print(f"    def accept(self, visitor: 'Visitor[R]') -> R:", file = file)
        print("         pass", file = file)
        print("", file = file)

        define_visitor(base_name, types, file)

        for type_def in types:
            class_name, fields = map(str.strip, type_def.split(":"))
            args = []
            assignments = []
            for field in fields.split(","):
                ftype, fname = field.strip().split(" ")
                args.append(f"{fname}: {ftype}" )
                assignments.append(f"       self.{fname} = {fname}")

            print(f"class {class_name}({base_name}):", file = file)
            print(f"    def __init__(self, {', '.join(args)}):", file = file)
        
            for assignment in assignments:
                print(assignment, file = file)
            print("", file = file)
            
            print("    def accept(self, visitor: Visitor):", file = file)
            print(f"        return visitor.visit_{class_name.lower()}_expr(self)", file = file)
            print(" ", file = file)

define_ast(
    "./src",
    "Expr",
    [
      "Binary   : Expr left, Token operator, Expr right",
      "Grouping : Expr expression",
      "Literal  : object value",
      "Unary    : Token operator, Expr right"
    ]
)

