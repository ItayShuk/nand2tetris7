class CodeWriter:

    segmentsCodes = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "pointer": "3",
                     "temp": "5"}

    def __init__(self, fileOrders, fileDest):
        output = open(fileDest[:-2] + "asm","w+")
        for order in fileOrders:
            self.writeOrder(order, output)

    def writeOrder(self, order, output):
        switch = {
            "push": self.pushCommand(order[1], order[2], output),
            "pop": self.popCommand(order[1], order[2], output),
            "add": self.add(output),
            "sub": self.sub(output)
        }
        switch.get(order[0])

    def pushCommand(self, variable, index, output):
        if variable == "constant":
            output.write("@" + index + "\n")
            output.write("D=A\n")
            output.write("@SP\n")
            output.write("A=M\n")
            output.write("M=D\n")
            output.write("@SP\n")
            output.write("M=M+1\n")
        else:
            output.write("@" + index + "\n")
            output.write("D=A\n")
            output.write("@" + self.segmentsCodes[variable] + "\n")
            output.write("A=A+D\n")
            output.write("D=M\n")
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

    def add(self, output):
        self.preAddSub(output)
        output.write("M=D+M" + "\n")
        self.pushCommand("temp", "2", output)

    def sub(self, output):
        self.preAddSub(output)
        output.write("M=D-M" + "\n")
        self.pushCommand("temp", "2", output)

    def preAddSub(self, output):
        self.popCommand("temp", "1", output)
        self.popCommand("temp", "2", output)
        output.write("@" + str(int(self.segmentsCodes["temp"]) + 1) + "\n")
        output.write("D=M")
        output.write("@" + str(int(self.segmentsCodes["temp"]) + 2) + "\n")
