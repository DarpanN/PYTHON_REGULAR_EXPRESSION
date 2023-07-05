import re

content = "Hello!! Boss Welcome To My World"
word = "\s"

def findWord(word, str):
    content = re.findall(word, str)
    print(content)

findWord(word, content)

def splitStr(word, str):
    content=re.split(word, str)
    print(content)

splitStr(word, content)
    
    