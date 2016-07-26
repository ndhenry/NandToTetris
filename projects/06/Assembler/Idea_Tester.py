#############################################
# Author:   Nelson Henry                    #
# Created:  7/25/2016                       #
# Revised:  7/25/2016                       #
#############################################

# Importing packages
import os

# Initialization
# cwd = os.getcwd()
# print('Current Directory: ', cwd)
from sys import argv

predefineDict = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576, 'R0': 0, 'R1': 1,
                 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
                 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15}

destDict = {'null': 0, 'M': 1, 'D': 2, 'MD': 3, 'A': 4, 'AM': 5, 'AD': 6, 'AMD': 7}
jumpDict = {'null': 0, 'JGT': 1, 'JEQ': 2, 'JGE': 3, 'JLT': 4, 'JNE': 5, 'JLE': 6, 'JMP': 7}

os.system('cls')
print('Begin Reading File')

# Reading target file
inputFilename = argv[1]
filename, file_ext = os.path.splitext(inputFilename)
if file_ext != '.asm':
    print('\tFilename: ', filename)
    print('\tFile Extension: ', file_ext, '\n')
    print('Please input an assembly file only and in the following format: \n')
    print('python Idea_Tester.py [Filename].asm\n')
    quit()

inputFile = open(inputFilename, 'r')
inputContents = inputFile.read()
inputContents = inputContents.rstrip('\n')


# Writing machine code binary file
outputFilename = filename + '.hack'
outputFile = open(outputFilename, 'w')
outputContents = '10011010\n00001111'
outputFile.write(outputContents)

# Outputting results
print('\nOriginal File:\t', inputFilename)
print('--------------------------------------------------')
print(inputContents)
print('-------------------- File End --------------------\n\n')
print('New File:\t', outputFilename)
print('--------------------------------------------------')
print(outputContents)
print('-------------------- File End --------------------\n')
print('Done\n')

# Clean up
inputFile.close()
outputFile.close()
