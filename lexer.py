from utils import *
from tokens import TokenType,Token

class Lexer:
    def __init__(self,text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    def generate_tokens(self) -> iter:
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == DECIMAL or self.current_char in DIGIT:
                yield self.generate_number()
            
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS) 
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS) 
            elif self.current_char == "^" or self.current_char == "*":
                self.advance()
                if self.current_char == "*":
                    yield Token(TokenType.POW)
                else:
                    yield Token(TokenType.MULTIPLY) 
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "!":
                self.advance()
                yield Token(TokenType.FACTORIAL)
            elif self.current_char == "%":
                self.advance()
                yield Token(TokenType.MODULO)    
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN) 
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)  
            else:
                raise Exception(f"Illegal character:{self.current_char}")
    
    def generate_number(self)  -> Token:
        decimal_point_count = 0
        number:str = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char == DECIMAL or self.current_char in DIGIT):
            if self.current_char == DECIMAL:
                decimal_point_count += 1
                if  decimal_point_count > 1:
                    break
            number += self.current_char
            self.advance()
        if number.startswith(DECIMAL):
            number = '0' + number
        elif number.endswith(DECIMAL):
            number += "0"
        
        return Token(TokenType.NUMBER, float(number))