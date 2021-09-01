
from tokens import Token,TokenType
from nodes import *

class Parser:
    def __init__(self,tokens):
        self.tokens = iter(tokens)
        self.advance()
    def raise_error(self):
        raise Exception(f"Invalid syntax: {self.current_tokens}")
    def advance(self):
        try:
            self.current_tokens = next(self.tokens)
        except StopIteration:
            self.current_tokens = None
    
    def parse(self):
        if self.current_tokens == None:
            return None
        result = self.expr()
        if self.current_tokens != None:
            self.raise_error()
        
        return result

    def expr(self):
        result = self.term()

        while self.current_tokens != None and self.current_tokens.type in (TokenType.PLUS,TokenType.MINUS):
            if self.current_tokens.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result,self.term())
            elif self.current_tokens.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result,self.term())
        return result

    def term(self):
        result = self.factor()

        while self.current_tokens != None and self.current_tokens.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.POW,
            TokenType.LPAREN,
            TokenType.MODULO,
            TokenType.FACTORIAL
            ):
            if self.current_tokens.type == TokenType.FACTORIAL:
                self.advance()
                result = FactorialNode(result)
            elif self.current_tokens.type == TokenType.POW:
                self.advance()
                result = PowNode(result,self.factor())
            elif self.current_tokens.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result,self.factor())
            elif self.current_tokens.type == TokenType.MODULO:
                self.advance()
                result = ModuloNode(result,self.factor())
            elif self.current_tokens.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result,self.factor())
            elif self.current_tokens.type == TokenType.LPAREN:
                result = MultiplyNode(result,self.factor())
                self.advance()
        return result
    
    def factor(self):
        token = self.current_tokens
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_tokens.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
            
        self.raise_error()
        
