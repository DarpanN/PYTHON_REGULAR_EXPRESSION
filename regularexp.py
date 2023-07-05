import re

content = "Hello!! Boss Welcome To To My World"
word = "Boss"

def findWord(word, str):
    content = re.findall(word, str)
    print(content)

findWord(word, content)
    
    