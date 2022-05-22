
import requests
import time
import random

roles = [ 'analyst', 'core-engineer', 'developer', 'performance-engineer', 'software-delivery', 'sre', 'tester' ]

def webCall(url):
    res = requests.get(url)
    return res

def write2File(filename, string):
    text_file = open(filename, "w")
    n = text_file.write(string)
    text_file.close()

def scrapeBasePage(name):
    return webCall(f'https://sky-uk.github.io/career-progression/#{name}')

def scrapeBasePages():
    for page in roles:
        res = scrapeBasePage(page)
        write2File(f'output/basepage/{page}.html', res.text)
        time.sleep(random.randint(10, 30)/10)

scrapeBasePages()