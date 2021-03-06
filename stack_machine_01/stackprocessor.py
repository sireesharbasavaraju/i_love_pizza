import sys

# this is the implementeation of stack processor
# credits to http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
class Stack(object):
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        return self.stack_list == []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def fetch_operand(self):
        return (self.stack_list.pop(-2), self.stack_list.pop(-1))
    
    def print_stack(self):
        for item in self.stack_list:
            print "|", item,
        print ("")

class CPU(object):
    def __init__(self):
        self.Stack = Stack()
        self.SP = -1 # last index is always -1 in python
        self.instruction = ""
	
    def run(self, program):
        for l in program:
            self.instruction = l
            self.execute()
            self.print_state()
		
    def execute(self):
        try:
            opc, val = tuple(self.instruction.split())
        except ValueError:
            opc = self.instruction

        if opc == "push":
            self.Stack.push(int(val))
        if opc == "end":
            sys.exit()
        if opc == "add":
            x1, x2 = self.Stack.fetch_operand()
            self.Stack.push(x1+x2)
        if opc == "sub":
            x1, x2 = self.Stack.fetch_operand()
            self.Stack.push(x2-x1)
        if opc == "mul":
            x1, x2 = self.Stack.fetch_operand()
            self.Stack.push(x1*x2)

    def print_state(self):
        print (self.instruction)
        self.Stack.print_stack()
    
