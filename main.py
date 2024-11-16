from lexer import lexer
from parser1 import parser
import random

 # we know the file exists , so goes into try block , once error encontered goes to except block 

try:
    with open("D:\Downloads\Another Example\project\new\input1.txt", "r") as file:
        data = file.read()
        print()
        print("The Input File Content:\n")
        print(data)
        print()
        parser.parse(data, lexer=lexer)
        print("Parsing has been completed!\n")

except Exception as e:
    print('Syntax Error!!')
    print(f"Error during parsing: {e}")
