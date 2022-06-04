import re
from node import Node

last_result = {'line':'','level':0}

def convertStringListToNode(str_list, rex_list, current_level=0, node=Node()):
    while len(str_list) > 0:
        line = str_list[0]
        line_level = getLineLevel(line, rex_list)
        if (line_level > current_level):
            childNode = Node()
            node.addChild(childNode)
            convertStringListToNode(str_list,rex_list,current_level+1,childNode)
        if (line_level == current_level):
            if line_level == len(rex_list):
                str_list.remove(line)
                if node.val == '':
                    node.val = line
                else:
                    node.val = node.val + "\n" + line
            elif line_level == 0:
                str_list.remove(line)
                if node.val == '':
                    node.val = line
                else:
                    node.setNext(Node())
                    node = node.next
                    node.val = line
            elif node.val != '':
                return
            elif node.val == '':
                str_list.remove(line)
                node.val = line
                continue
        if line_level < current_level:
            return


def getLineLevel(str, rex_list):
    if str == last_result['line']:
        return last_result['level']
    last_result['line'] = str
    for x in rex_list:
        if x.match(str):
            last_result['level'] = rex_list.index(x)
            return last_result['level']
    last_result['level'] = len(rex_list)
    return last_result['level']
