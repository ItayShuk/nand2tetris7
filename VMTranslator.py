import sys, CodeWriter
from Parser import Parser
# from CodeWriter import CodeWriter


def main():
    file = Parser(sys.argv[1])
    # CodeWriter(file.orderList)
    return


if __name__ == '__main__':
    main()
