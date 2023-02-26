import re

characters = [0, 1]
word = input(f"write word using {characters} ")
while not (word.count('0')+word.count('1') == len(word)):
    word = input('...\n')

pattern = re.compile('11001')
result = pattern.findall(word)
print(f"{bool(result)} {len(result)}")
