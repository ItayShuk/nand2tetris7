class MemorySegments:
    def __init__(self):
        self.SP = 256
        self.LCL = 300
        self.ARG = 400
        self.THIS = 3000
        self.THAT = 3010
        self.RAM = {0: self.SP, 1: self.LCL, 2: self.ARG, 3: self.THIS, 4: self.THAT}

    def getLocal(self, index):
        return self.RAM[self.LCL + index]

    def getArg(self, index):
        return self.RAM[self.ARG + index]

    def getThis(self, index):
        return self.RAM[self.THIS + index]

    def getThat(self, index):
        return self.RAM[self.THAT +index]

    def push(self, number):
        self.RAM[self.SP] = number
        self.SP += 1

    def pop(self, memorySegmentIndex, memorySegmentType):
        switch = {
            "local": self.getLocal(memorySegmentIndex),
            "argument": self.getArg(memorySegmentIndex),
            "this": self.getThis(memorySegmentIndex),
            "that": self.getThat(memorySegmentIndex)
        }
        ramIndex = switch.get(memorySegmentType)
        self.SP -= 1
        self.RAM[ramIndex] = self.RAM[self.SP]