class Parser:

    def __init__(self, filePath):
        lineList = [line.rstrip('\n') for line in open(filePath) if line.strip()]
        cleanList = self.cleanTheList(lineList)
        orderList = self.setOrders(cleanList)
        print(orderList)

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
        for line in cleanList:
            ordersList.append(line.split(" "))
        return ordersList

