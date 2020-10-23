class CodeWriter:

    segmentsCodes = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "pointer": "3",
                     "temp": "5"}

    def __init__(self, fileOrders, fileDest):
        output = open(fileDest[:-2] + "asm")
        for order in fileOrders:
            self.writeOrder(order, output)

    def writeOrder(self, order, output):
        switch = {
            "push": self.pushCommand(order, output),
            "pop": self.popCommand(order, output),
            "add": self.add(order, output),
            "sub": self.sub(order, output)
        }
        switch.get(order[0])

    def pushCommand(self, order, output):
        if order[1] == "constant":
            output.write("@" + order[2] + "\n")
            output.write("D=A\n")
            output.write("@SP\n")
            output.write("A=M\n")
            output.write("M=D\n")
            output.write("@SP\n")
            output.write("M=M+1\n")
        else:
            output.write("@" + order[2] + "\n")
            output.write("D=A\n")
            output.write("@" + self.segmentsCodes[order[1]] + "\n")
            output.write("A=A+D\n")
            output.write("D=M\n")
            output.write("@SP\n")
            output.write("A=M\n")
            output.write("M=D\n")
            output.write("@SP\n")
            output.write("M=M+1\n")

    def popCommand(self, order, output):
        output.write("@"+order[2]+"\n")
        output.write("D=A\n")
        output.write("@"+self.segmentsCodes[order[1]]+"\n")
        output.write("D=A+D\n")
        output.write("@"+self.segmentsCodes["temp"]+"\n")
        output.write("M=D\n")
        output.write("@SP\n")
        output.write("M=M-1\n")
        output.write("A=M\n")
        output.write("D=M\n")
        output.write("@"+self.segmentsCodes["temp"]+"\n")
        output.write()
