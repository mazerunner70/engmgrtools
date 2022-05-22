import requests
import time
import random

def webcall(url):
    res = requests.get(url)
    return res.text

def write2file(filename, string):
    text_file = open(filename, "w")
    n = text_file.write(string)
    text_file.close()

def scrapeskillpage(name):
    return webcall(f'https://sky-uk.github.io/career-progression/skill-{name}.html')

def scrapeskillpages(skills):
    for pageindex in range(len(skills)):
        page = skills[pageindex]
        print(f'page {pageindex} of {len(skills)} pages: {page}')
        res = scrapeskillpage(page)
        write2file(f'output/skillspages/{page}.html', res)
        time.sleep(random.randint(10, 30)/10)

