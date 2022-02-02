from node import Node
import re
import convert


def readFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        return f.read()


def writeNodeAsFile(node, output_name):
    dataFrame = node.toDataFrams()
    dataFrame.to_csv(output_name+'.csv', encoding='utf-8',
                     header=False, index=False)


def convert_file(filePath, output_name='default', rex_list_str=["^\d{1,4}\..*"]):
    rex_list = []
    for x in rex_list_str:
        rex_list.append(re.compile(x))
    node = Node()

    readStr = readFile(filePath)
    convert.convertStringListToNode(readStr.splitlines(), rex_list, 0, node)
    writeNodeAsFile(node, output_name)
