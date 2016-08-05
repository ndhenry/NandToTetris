import SymbolTable, Code, Parser, sys, os.path


class Assembler(object):

    def __init__(self):
        self.symbols = SymbolTable.SymbolTable()

    def outname(self, sourcefile):
        """Generates an appropriate output file name."""
        return sourcefile.replace('.asm', '.hack')

    def pass1(self, sourcefile):
        """Pass 1 is responsible for management of symbols and removal of unnecessary portions of the assembly code."""
        parser = Parser.Parser(sourcefile)
        with open(parser.sourcefile) as parser.open_file:
            for line in parser.open_file:
                print(line)

        return parser

    def pass2(self, parser):
        """Pass 2 is responsible for translation of prepared assembly code to HACK binary machine code."""
        code = Code.Code()

        # Overwriting any existing file and preparing for
        outfile = open(self.outname(parser.sourcefile),'w')

        with open(parser.sourcefile) as parser.open_file:
            for line in parser.open_file:

                cmd = parser.command_type(line)
                line = line.strip('\n')

                if cmd == parser.a_cmd:
                    address = parser.symbol(line)
                    outfile.write((code.a_gen(address) + '\n'))

                elif cmd == parser.c_cmd:
                    parts = parser.c_dissect(line)
                    outfile.write((code.c_gen(parts[0], parts[1], parts[2]) + '\n'))

                elif cmd == parser.l_cmd:
                    outfile.write('L Command\n')

                else:
                    print('Not A, C, or L Command')

        outfile.close()

    def build(self, sourcefile):
        """Build is responsible for the management of the assembly process."""

        parser = self.pass1(sourcefile)
        self.pass2(parser)


def input_checking(args):
    if len(args) != 2:
        print('Format: python Assembler filename.asm')
        exit()
    else:
        sourcefile = args[1]

    if os.path.isfile(sourcefile.replace('.asm', '.hack')):
        print('\nOutput file already exists, Override?')
        response = ''
        while response == '':
            response = input('Y/N: ')
            if (response == 'Y') | (response == 'y'):
                continue
            elif (response == 'N') | (response == 'n'):
                exit()
            else:
                response = ''
        print('')

    return sourcefile


def main():
    sourcefile = input_checking(sys.argv)
    assembler = Assembler()
    assembler.build(sourcefile)
    print('\nDone\n')

if __name__ == "__main__":
    main()
