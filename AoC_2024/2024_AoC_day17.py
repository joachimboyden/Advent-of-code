# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:16:04 2024

@author: joach
"""
import re
import math as m

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

reNumbers = "[0-9]+"

file = inputFile.readlines()

program = list(map(int, re.findall(reNumbers, file[4])))

def prime_factors(num):
  factors = []
  factor = 2

  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return factors

def Combo(operand, A, B, C):
    if 0 <= operand < 4:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
        
def RunProgram(a, program):
    A = a
    B = 0
    C = 0
    pointer = 0
    output = []
    
    while pointer < len(program) - 1:
        opcode = program[pointer]
        operand = program[pointer + 1]
        pointerChanged = False
        
        if opcode == 0:
            A = m.trunc(A / (2 ** Combo(operand, A, B, C)))
            
        elif opcode == 1:
            B = B ^ operand
            
        elif opcode == 2:
            B = Combo(operand, A, B, C) % 8
            
        elif opcode == 3:
            if A == 0:
                pointerChanged = False
            else:
                pointer = operand
                pointerChanged = True
                
        elif opcode == 4:
            B = B ^ C
            
        elif opcode == 5:
            output.append(Combo(operand, A, B, C) % 8)
            
        elif opcode == 6:
            B = m.trunc(A / (2 ** Combo(operand, A, B, C)))
            
        elif opcode == 7:
            C = m.trunc(A / (2 ** Combo(operand, A, B, C)))
            
            
        if output != program[:len(output)]:
            if len(output) > 5:
                print(output, a, prime_factors(a))
            return output
            
        if not pointerChanged:
            pointer += 2
            
    return output

def FindCopyA():
    output = []
    A = 1
    while output != program:
        output = RunProgram(A, program)
        A += 2
        
    return A - 1

print(FindCopyA())

'''
225000000
'''