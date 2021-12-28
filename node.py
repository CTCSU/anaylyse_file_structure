import pandas

class Node:
    val = ''
    def __init__(self,val=''):
        self.children = []
        self.next = None
        self.val = val

    def addChild(self, child):
        self.children.append(child)
    
    def setNext(self, next):
        self.next = next

    def toArray(self, currentDepth=0, currentHight=0, multilist = None):
        # read current node first, add an item if the series doesn't exsit one 
        if multilist is None:
            depthAndHight = self.getNodeDepthAndHight()
            multilist = [['' for col in range(depthAndHight[0])] for row in range(depthAndHight[1])]

        multilist [currentHight][currentDepth] = self.val;

        if self.children and len(self.children) > 0:
            for child in self.children:
                child.toArray(currentDepth+1,currentHight,multilist)
                currentHight = child.getNodeDepthAndHight()[1] + currentHight
        else:
            currentHight = currentHight + 1

        if not self.next is None:
            self.next.toArray(currentDepth, currentHight, multilist)

        return multilist

    def getNodeDepthAndHight(self):
        maxDepth = 1
        totalHight = 1
        next_result = [1,0]
        if self.children and len(self.children) > 0:
            for child in self.children:
                result = child.getNodeDepthAndHight()
                maxDepth = max(result[0]+1, maxDepth)
                totalHight = result[1] + totalHight
        if totalHight != 1:
            totalHight = totalHight - 1
        if not self.next is None:
            next_result = self.next.getNodeDepthAndHight()
        return [max(maxDepth,next_result[0]), totalHight + next_result[1]]
    
    def toDataFrams(self):
        dataframe = pandas.DataFrame(self.toArray())
        dataframe.to_csv('result.csv')
        
def test(): 
    node = Node('good')
    node.setNext(Node('next'))
    node.addChild(Node('child1'))
    node.addChild(Node('child2'))
    node.children[0].addChild(Node('child3'))
    node.children[0].children[0].addChild(Node('end'))
    node.children[0].addChild(Node('child9'))
    node.children[1].addChild(Node("c3"))
    node.children[1].addChild(Node("c4"))
    node.children[1].children[1].addChild(Node('end2'))
