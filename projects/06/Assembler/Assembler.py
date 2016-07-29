import SymbolTable, Code, Parser, sys


class Assembler(object):

    def __init__(self):
        self.symbols = SymbolTable.SymbolTable()

    def pass1(self):
        """Pass 1 is responsible for management of symbols and removal of unnecessary portions of the assembly code."""
        pass

    def pass2(self, sourcefile, outfile):
        """Pass 2 is responsible for translation of prepared assembly code to HACK binary machine code."""

        parser = Parser.Parser(sourcefile)
        code = Code.Code()
        outfile = open()
        while Parser.has_more_commands():

            parser.advance()
            cmd = parser.command_type()

            if cmd == parser.a_cmd:
                pass

            elif cmd == parser.c_cmd:
                pass

            elif cmd == parser.l_cmd:
                pass

            else:
                print('Pass 2: Failed Check')

        outfile.close()

    def outname(self, sourcefile):
        """Generates an appropriate output file name."""
        return sourcefile.replace('.asm', '.hack')

    def build(self, sourcefile):
        """Build is responsible for the management of the assembly process."""

        self.pass1(sourcefile)
        self.pass2(sourcefile, self.outname(sourcefile))


def main():
    if len(sys.argv) != 2:
        print('Format: python Assembler filename.asm')
    else:
        sourcefile = sys.argv[1]

    assembler = Assembler()
    assembler.build(sourcefile)
    print('Done')

main()
