'''The files.txt contains a list of file names. 
Write a program that prints only those file names whose extensions consist of exactly four characters (e.g. .html).'''

import re

with open('files.txt') as f:
    content = f.read()

pattern = '([A-Za-z_\d]+\.[a-z]{4})'

matched = re.findall(pattern, content)

print(matched)