class CodeWriter:
    output

    def __init__(self, fileOrders, fileDest):
        output = open(fileDest[:-2] + "asm")
        for order in fileOrders:
            writeOrder(order)
