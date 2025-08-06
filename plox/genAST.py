import os

def define_ast(output_dir: str, base_name: str, types: list[str]):
    path = os.path.join(output_dir, f"{base_name.lower()}.py")
    with open(path, "w") as file:
        print("from token import Token", file = file)
        print("", file = file)
        print(f"class {base_name}:", file = file)
        print("    pass", file = file)
        print("", file = file)

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
