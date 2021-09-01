
from lexer import Lexer
from parser_ import Parser
from interpeter import Interpeter

while True:
    code = input("math> ")
    lexer = Lexer(code)
    tokens:iter = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree: continue
    interpeter = Interpeter()
    value = interpeter.visit(tree)
    print(value,end="\n")
