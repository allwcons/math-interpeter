import enum
from dataclasses import dataclass

# math_expr:str = "(( 1- 2) /3) * 4"

class TokenType(enum.Enum):
    NUMBER      = 0
    PLUS        = 1
    MINUS       = 2
    DIVIDE      = 3
    MULTIPLY    = 4
    LPAREN      = 5
    RPAREN      = 6
    POW         = 7
    MODULO  = 8
    FACTORIAL   = 9

@dataclass
class Token:
    type:TokenType
    value:any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
