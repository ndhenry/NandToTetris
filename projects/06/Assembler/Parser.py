import re


class Parser:
    def __init__(self, sourcefile):
        self.a_cmd = 0
        self.c_cmd = 1
        self.l_cmd = 2
        self.sourcefile = sourcefile
        self.re_dest_reduce = '@.*'
        self.re_comp_reduce = ''
        self.re_jump_reduce = ''
        return

    def command_type(self, line):
        """Determines the command type of a given assembly code line"""
        if line.startswith('//'):
            return None
        elif line.startswith('@'):
            return self.a_cmd
        elif '=' in line or ';' in line:
            return self.c_cmd
        elif line.startswith('(') and line.endswith(')'):
            return self.l_cmd
        else:
            if line != '\n':
                print('Error: has_more_commands had no correct command matching for %r' % line)

    def symbol(self, line):
        """Returns a string of A or L command types"""
        # Needs to address symbol conversion to addresses
        return (re.search('(?<=@)\w+', line)).group(0)

    def c_dissect(self, line):
        """Returns the Hack Mnemonics dissected into dest, comp, and jump sections"""
        half1 = re.split('[=]', line)
        if len(half1) == 2:
            half1.append(' ')
            parts = half1

        else:
            half2 = re.split('[;]', line)
            temp = [' ']
            temp.extend(half2)
            parts = temp

        return parts
