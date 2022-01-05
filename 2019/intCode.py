# To Import:
# import sys
# sys.path.append('../')
# from intCode import *

class Argument:
    def __init__(self, val, addr):
        self.val = val
        self.addr = addr

class Instr(object):
    code, argNum = 0,0
    def execute(self, intcode, args): pass
    def newPointer(self, intcode):
        return intcode.pointer + self.argNum + 1

class sumInstr(Instr):
    code, argNum = 1,3
    def execute(self, intcode, args):
        intcode.set(args[2].addr, args[0].val + args[1].val)
        return self.newPointer(intcode)

class multiplyInstr(Instr):
    code, argNum = 2,3
    def execute(self, intcode, args):
        intcode.set(args[2].addr, args[0].val * args[1].val)
        return self.newPointer(intcode)

class inputInstr(Instr):
    code, argNum = 3,1
    def execute(self, intcode, args):
        intcode.set(args[0].addr, intcode.getInput())
        return self.newPointer(intcode)

class outputInstr(Instr):
    code, argNum = 4,1
    def execute(self, intcode, args):
        intcode.output = args[0].val
        return self.newPointer(intcode)

class jumpIfTrueInstr(Instr):
    code, argNum = 5,2
    def execute(self, intcode, args):
        return args[1].val if args[0].val!=0 else self.newPointer(intcode)

class jumpIfFalseInstr(Instr):
    code, argNum = 6,2
    def execute(self, intcode, args):
        return args[1].val if args[0].val==0 else self.newPointer(intcode)

class lessThanInstr(Instr):
    code, argNum = 7,3
    def execute(self, intcode, args):
        intcode.set(args[2].addr, int(args[0].val < args[1].val))
        return self.newPointer(intcode)

class equalsInstr(Instr):
    code, argNum = 8,3
    def execute(self, intcode, args):
        intcode.set(args[2].addr, int(args[0].val == args[1].val))
        return self.newPointer(intcode)

class adjustRelativeBaseInstr(Instr):
    code, argNum = 9,1
    def execute(self, intcode, args):
        intcode.relativeBase += args[0].val
        return self.newPointer(intcode)

class endInstr(Instr):
    code, argument_num = 99, 0
    def execute(self, intcode, arguments):
        intcode.end = True
        return None

class IntCode:
    def __init__(self, program, inputs=[], inputFunc=None):
        self.program = program
        self.inputs = inputs[::-1]
        self.output = None
        self.end = False
        self.pointer = 0
        self.relativeBase = 0
        self.memory = {}
        self.inputFunc = inputFunc

    def getInstr(self, instCode):
        for inst in Instr.__subclasses__():
            if inst.code == instCode: return inst

    def getArgs(self, argNum):
        modes = str(self.program[self.pointer]).zfill(5)[:3][::-1]
        args = []
        for i in range(argNum):
            val = self.program[self.pointer+i+1] + (self.relativeBase if modes[i] == '2' else 0)
            if modes[i] == '1':
                args.append(Argument(val,val))
            else:
                args.append(Argument(self.program[val] if val < len(self.program) else self.memory.get(val,0), val))
        return args

    def run(self):
        self.output = None
        while not self.end and self.output == None:
            Instr = self.getInstr(self.program[self.pointer]%100)
            args = self.getArgs(Instr.argNum)
            self.pointer = Instr().execute(self, args)
        return self.output

    def execute(self):
        lastOut = None
        while not self.end:
            output = self.run()
            if not self.end:
                lastOut = output
        return lastOut

    def set(self, addr, val):
        if addr<len(self.program):
            self.program[addr] = val
        else:
            self.memory[addr] = val

    def getInput(self):
        return self.inputs.pop() if self.inputs else self.inputFunc()

    def addInput(self,input):
        self.inputs = [input]+self.inputs

    def copy(self):
        copy = IntCode(self.program, self.inputs[:], self.inputFunc)
        copy.output = self.output
        copy.end = self.end
        copy.pointer = self.pointer
        copy.relativeBase = self.relativeBase
        copy.memory = self.memory
        return copy
