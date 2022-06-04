from node import Node
import re
import convert 
from node import Node
file = open("./TransferPDFToCSV/2022 AWS SAP-C01(494题中文).txt", "r+", encoding="utf-16")

contents = []

rex = ["^\u95EE\u9898",".*\u7B54\u6848.*"];
count = 0;
for line in file:
    if count < 100000:
        contents.append(line)
        count = count + 1

rex_list = []
for x in rex:
        rex_list.append(re.compile(x))

node = Node()
firstNode = node;

currentQuestion = "";
currentAnswer = "";
appendQuestion = False;
appendAnswer = False

for str in contents:
    if(rex_list[0].match(str)):
        if(currentQuestion != ""):
            node.val = currentQuestion;
            child = Node(currentAnswer)
            node.addChild(child)
            next = Node();
            node.next = next;
            node = next;

        appendAnswer=False
        appendQuestion=True
        currentQuestion=str
    elif (rex_list[1].match(str)):
        str = str.strip()
        if not str.startswith("答案") :
            list = str.split("答案")
            first = list[0]
            currentQuestion = currentQuestion + "\n" + str
            str = "答案" + list[1]

        appendAnswer=True
        appendQuestion=False
        currentAnswer = str
    elif (appendQuestion):
        currentQuestion = currentQuestion + "\n" + str
    else: 
        currentAnswer = currentAnswer + "\n" + str

firstNode.toDataFrams()


