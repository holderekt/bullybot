import re

REGEX_LINE = '([\w]+)|\((.*?)\)'
REGEX_DIRTY = '[\w]+'

def file_readlines(filename):
    lines = []
    with open(filename, encoding='utf-8') as file: 
        lines = file.readlines()
    return lines

def extract_line(line):
    if(line[-1][1] == ''):
        bar = [first for first, _ in line]
        dirty = []
    else:
        bar = [first for first, _ in line[:-1]]
        dirty = re.findall(REGEX_DIRTY, line[-1][1])
    return bar,  dirty

def parse(filename):
    lines = file_readlines(filename)
    bars = []
    dirtys = []
    for line in lines:
        line = re.findall(REGEX_LINE, line)
        line, dirty = extract_line(line)
        bars.append(line)
        if len(dirty) != 0:
            dirtys.append(dirty)
    return bars, dirtys
        


