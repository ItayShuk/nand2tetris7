class CodeWriter:
    segmentsCodes = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "pointer": "3",
                     "temp": "5"}

    def __init__(self, fileOrders, fileDest):
        output = open(fileDest[:-2] + "asm", "w+")
        for order in fileOrders:
            self.writeOrder(order, output)

    def writeOrder(self, order, output):
        if order[0] == "push":
            self.pushCommand(order[1], order[2], output)
        elif order[0] == "pop":
            self.popCommand(order[1], order[2], output)
        elif order[0] == "add":
            self.binaryCommand(output, "+")
        elif order[0] == "sub":
            self.binaryCommand(output, "-")
        elif order[0] == "and":
            self.binaryCommand(output, "&")
        elif order[0] == "or":
            self.binaryCommand(output, "|")
        elif order[0] == "neg":
            self.unaryCommand(output, "-")
        elif order[0] == "not":
            self.unaryCommand(output, "!")
        # else:
            # self.sub(output)
        ## need to add gt, lt, eq, and what happens if order is not valid

    def pushCommand(self, variable, index, output):
        if variable == "constant":
            output.write("@" + index + "\n")
            output.write("D=A\n")
            self.pushToStack(output)

        elif variable == "local" or variable == "that" or variable == "this" or variable == "argument":
            output.write("@" + index + "\n")
            output.write("D=A\n")
            output.write("@" + self.segmentsCodes[variable] + "\n")
            output.write("A=M+D\n")
            output.write("D=M\n")
            self.pushToStack(output)

        elif variable == "pointer" or variable == "temp":
            output.write("@" + index + "\n")
            output.write("D=A\n")
            output.write("@" + self.segmentsCodes[variable] + "\n")
            output.write("A=M+D\n")
            output.write("D=M\n")
            self.pushToStack(output)

        else:
            output.write("@" + index + "\n")
            output.write("D=A\n")
            output.write("@" + self.segmentsCodes[variable] + "\n")
            output.write("A=A+D\n")
            output.write("D=M\n")
            self.pushToStack(output)

    def pushToStack(self, output):
        output.write("@SP\n")
        output.write("A=M\n")
        output.write("M=D\n")
        output.write("@SP\n")
        output.write("M=M+1\n")

    def popCommand(self, variable, index, output):
        output.write("@" + index + "\n")
        output.write("D=A\n")
        output.write("@" + self.segmentsCodes[variable] + "\n")
        output.write("D=A+D\n")
        output.write("@" + self.segmentsCodes["temp"] + "\n")
        output.write("M=D\n")
        output.write("@SP\n")
        output.write("M=M-1\n")
        output.write("A=M\n")
        output.write("D=M\n")
        output.write("@" + self.segmentsCodes["temp"] + "\n")
        output.write("A=M\n")
        output.write("M=D\n")

    def unaryCommand(self, output, operation):
        output.write("@SP\n")
        output.write("M=M-1\n")
        output.write("A=M\n")
        output.write("M=" + operation + "M\n")
        output.write("@SP\n")
        output.write("M=M+1\n")

    def binaryCommand(self, output, operation):
        output.write("@SP\n")
        output.write("M=M-1\n")
        output.write("A=M\n")
        output.write("D=M\n")
        output.write("@SP\n")
        output.write("M=M-1\n")
        output.write("A=M\n")
        output.write("M=M" + operation + "D" + "\n")
        output.write("@SP\n")
        output.write("M=M+1\n")
