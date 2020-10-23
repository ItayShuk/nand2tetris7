class CodeWriter:
    RAM = []
    memoryPointers = [("SP", 256),
                      ("local", 300),
                      ("argument", 400),
                      ("temp", 5),
                      ("this", 3000),
                      ("that", 3010),
                      ("pointer", 500),
                      ("static", 16)
                      ]

    SP = 0

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
        output.write("@" + order[2]+"\n")
        output.write("D=A\n")
        output.write("@")

