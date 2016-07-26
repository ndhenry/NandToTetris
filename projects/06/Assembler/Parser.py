class Parser:
    def __init__(self, ):
        return

    def hasMoreCommands(self):
        return # Boolean true or false

    def advance(self):
        return # nothing, just advances the current line

    def commandType(self):
        return # Either: A_COMMAND, B_COMMAND, C_COMMAND

    def symbol(self):
        return # String: returns if A or L command types

    def dest(self):
        return # String: the mnemonic destination representation

    def comp(self):
        return # String: the mnemonic command representation

    def jump(self):
        return # String: the mnemonic jump representation