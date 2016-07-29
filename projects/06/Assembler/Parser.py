import re
import fileinput

class Parser:
    def __init__(self, ):
        self.a_cmd = 0
        self.c_cmd = 1
        self.l_cmd = 2
        return

    def has_more_commands(self):
        return # Boolean true or false

    def advance(self):
        return # nothing, just advances the current line

    def command_type(self):
        return # Either: a_cmd, c_cmd, l_cmd

    def symbol(self):
        return # String: returns if A or L command types

    def dest(self):
        return # String: the mnemonic destination representation

    def comp(self):
        return # String: the mnemonic command representation

    def jump(self):
        return # String: the mnemonic jump representation