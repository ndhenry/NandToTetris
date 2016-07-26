from numpy import binary_repr


class Code(object):
    """Translates Hack assembly language mnemonics into binary code."""

    def __init__(self):
        pass

    _c_codes = {
        '0': '0101010',   '1': '0111111',   '-1': '0111010',  'D': '0001100',
        'A': '0110000',   '!D': '0001101',  '!A': '0110001',  '-D': '0001111',
        '-A': '0110011',  'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
        'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111',
        'D&A': '0000000', 'D|A': '0010101',

        '': 'acccccc',

        'M': '1110000',   '!M': '1110001',  '-M': '1110011',  'M+1': '1110111',
        'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
        'D&M': '1000000', 'D|M': '1010101'
    }
    _d_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    _j_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def comp(self, c_string):
        return self._c_codes[c_string]

    def dest(self, d_string):
        return binary_repr(self._d_codes.index(d_string), 3)

    def jump(self, j_string):
        return binary_repr(self._j_codes.index(j_string), 3)

    def a_gen(self, address):
        return '0' + address

    def c_gen(self, comp, dest, jump):
        return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)