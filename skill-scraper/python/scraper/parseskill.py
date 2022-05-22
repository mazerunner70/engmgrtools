
from bs4 import BeautifulSoup
import csv
from os import listdir
from os.path import isfile, join

def readfile(filename):
    with open(filename, "r") as f:
        data = f.read().replace('\n', '')
    return data

def writecsv(name, rows):
    with open(f'output/skillcsv/{name}.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in rows:
            csvwriter.writerow(row)

def readpage(page):
    res = readfile(f'output/skillspages/{page}.html')
    return res

def startparser(data):
    return BeautifulSoup(data, 'html.parser')

def getBody(node):
    return node.body

def getTitle(body):
    return body.header.h1.text
def getDescription(body):
    return body.header.p.text
def getSkillTable(body):
    return body.table

def has_td_subelement(tag):
    return tag.name == 'tr' and tag.find('td') != None

def findtablerows(skilltable):
    return skilltable.find_all(has_td_subelement)

def tablecells(tablerow):
    return [x.text for x in tablerow.find_all("td")]

def skillpageascsv(data):
    soup = startparser(data)
    body = getBody(soup)
    title = getTitle(body)
    description = getDescription(body)
    skilltable = getSkillTable(body)
    tablerows = findtablerows(skilltable)
    cells = [tablecells(row) for row in tablerows]
    return [[title], [description]] + cells

mypath = "output/skillspages"
onlyfiles = [f.split('.')[0] for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
for file in onlyfiles:
    data = readpage(file)
    skillcsv = skillpageascsv(data)
    writecsv(file, skillcsv)
    print(csv)