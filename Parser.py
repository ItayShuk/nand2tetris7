class Parser:
    orderList = []

    def __init__(self, filePath):
        lineList = [line.rstrip('\n') for line in open(filePath) if line.strip()]
        cleanList = self.cleanTheList(lineList)
        self.orderList = self.setOrders(cleanList)

    def cleanTheList(self, list):
        cleanList = []
        for line in list:
            if line[0] == "" or line[0] == "/":
                continue
            else:
                cleanList.append(line)
        return cleanList

    def setOrders(self, cleanList):
        ordersList = []
        finalLine = []
        for line in cleanList:
            splittedLine = line.split(" ")
            for word in splittedLine:
                if word != "" and word[0] != "/":
                    finalLine.append(word)
                else:
                    break
            ordersList.append(finalLine)
            finalLine = []
        return ordersList
