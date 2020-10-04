# -----------------------------------------------------------
# File loading and parsing
# -----------------------------------------------------------

import re

REGEX_LINE = '([\w]+|\?|\!|\(.*?\))'
REGEX_DIRTY = '[\w]+'


def file_readlines(filename):
    '''
    Read all lines from a specified text file
    '''
    lines = []
    with open(filename, encoding='utf-8') as file: 
        lines = file.readlines()
    return lines

def parsetitle(filename):
    '''
    Parse all titles
    '''
    return [re.findall(REGEX_LINE, line.upper()) for line in file_readlines(filename)]

def parse(filename):
    '''
    Load and split all lines in specified file
    returns list of bars and list of dirty lines
    '''
    lines = file_readlines(filename)
    bars = []
    dirtys = []
    for line in lines:
        line = re.findall(REGEX_LINE, line.lower())
        if "(" in line[-1]:
            bars.append(line[:-1])
            dirtys.append(re.findall(REGEX_DIRTY, line[-1]))
        else:
            bars.append(line)
    return bars, dirtys
        