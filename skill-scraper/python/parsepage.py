
from bs4 import BeautifulSoup
import csv
import requests
from scraper import scrapeskill

def webCall(url):
    res = requests.get(url)
    return res

def readfile(filename):
    with open(filename, "r") as f:
        data = f.read().replace('\n', '')
    return data

def readpage(page):
    res = readfile(f'output/basepage/{page}.html')
    return res

def has_class(tag):
    return tag  == 'th' and tag.has_attr('class')

def has_tr_subelement(tag):
    return tag.name == 'table' and tag.find('tr') != None and tag.tr.find('th') != None and tag.tr.th.has_attr('class')

def get_role_tables():
    data = readpage('analyst')
    soup = BeautifulSoup(data, 'html.parser')
    tabletags = soup.find_all(has_tr_subelement)
    return tabletags

def extractname(tabletag):
    return tabletag.tr.th.text

def has_roles_subelement(tag):
    return tag.name == 'tr' and tag.has_attr('id') and tag['id'] == 'roles'

def extractlevels(tabletag):
    s = tabletag.find(has_roles_subelement)
    return [ x.text for x in s.find_all('th')]

def has_dataskill_subelement(tag):
    return tag.name == 'tr' and tag.has_attr('data-skill')

def extract_skill_data(trtag):
    return [ [trtag['data-skill']], [ x.text for x in trtag.find_all('th')], [ x.text for x in trtag.find_all('td')] ]

def extract_skill_name(tabletag):
    s = tabletag.find_all(has_dataskill_subelement)
    return [ extract_skill_data(x) for x in s]

def assemble_line(dataentry):
    return [item for sublist in dataentry for item in sublist]

def assemblelists(datalists):
    return [assemble_line(x) for x in datalists]

def writecsv(name, rows):
    with open(f'output/csv/{name}.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in rows:
            csvwriter.writerow(row)

def getskillpage(rows):
    return [x[0] for x in rows]

tabletags = get_role_tables()
skills_list = []
for tag in tabletags:
    name = extractname(tag)
    levels = extractlevels(tag)
    lists = extract_skill_name(tag)
    csvform = assemblelists(lists)
    writecsv(name, [[name], levels] + csvform)
    skills_list  = skills_list + getskillpage(csvform)

nodups = list(dict.fromkeys(skills_list))
skillpage = scrapeskill.scrapeskillpages(nodups)
