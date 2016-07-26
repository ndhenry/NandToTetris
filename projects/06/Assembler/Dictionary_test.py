from numpy import binary_repr
import SymbolTable

mySymbolTable = SymbolTable.SymbolTable()
print(mySymbolTable.get_address('THIS'))
print(mySymbolTable.contains('THIS'))

predefineDict = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576,
                 'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
                 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15}

destDict = {'null': 0, 'M': 1, 'D': 2, 'MD': 3, 'A': 4, 'AM': 5, 'AD': 6, 'AMD': 7}
jumpDict = {'null': 0, 'JGT': 1, 'JEQ': 2, 'JGE': 3, 'JLT': 4, 'JNE': 5, 'JLE': 6, 'JMP': 7}

C_intro = '111'
C_function = '0000000'
C_dest = binary_repr(destDict['MD'])
C_jump = binary_repr(jumpDict['JMP'])

BinaryCommand = C_intro + C_function + C_dest + C_jump
print(BinaryCommand)

content = [inputFile.rstrip('\n') for inputFile in open('MachineCode.asm')]
print(content)
