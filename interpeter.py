from nodes import *
from values import Number
import math

class Interpeter:
    def visit(self,node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self,method_name)

        return method(node)
    
    def visit_NumberNode(self,node):
        return Number(node.value)
    def visit_AddNode(self,node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_FactorialNode(self,node):
        return Number(math.factorial(self.visit(node.node).value))
    
    def visit_ModuloNode(self,node):
        return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
    def visit_SubtractNode(self,node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self,node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_PlusNode(self,node):
        return self.visit(node.node).value
    def visit_MinusNode(self,node):
        return Number(self.visit(node.node).value * -1)

    def visit_PowNode(self,node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_DivideNode(self,node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("runtime Math error")


