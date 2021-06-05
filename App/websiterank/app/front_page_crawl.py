import urllib.request as urllib2
from time import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from enchant.checker import SpellChecker
import sys
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import os


def info_retrieve(webdriver,uni_name,url):
    info_txt =[]

    path = './data/content/'+'content'+uni_name+'.txt'
    if os.path.exists(path):
         os.remove(path)

    with open('./data/content/'+'content'+uni_name+'.txt','a',encoding="utf-8")as f: 

        with webdriver as driver:
            
           
            url=url
            # Set timeout time 
            wait = WebDriverWait(driver, 20)

            # retrive url in headless browser
            driver.get(url)
            html_source = driver.page_source
            
            # Get the source html from the page
            soup = BeautifulSoup(html_source, 'html.parser')
            # print(soup)

            # Get the all items from dropdown menu
            for name_list in soup.find_all(class_ ='dropdown'):
                # print(name_list.text)
                f.write(name_list.text)
                f.write('\n')
            
            # Find all the text in links 
            # up_links=soup.find_all(lambda tag: tag.name == 'a')
            # print(up_links)
            elems = driver.find_elements_by_xpath("//a[@href]")

            for elem in elems:
                lnk=(elem.get_attribute("href"))
                lnk_txt=elem.get_attribute('text')
                if lnk_txt:
                    f.write(lnk_txt)
                    f.write('\n')

            # for u_link in up_links:
            #     print(u_link)
            #     print('\n')
            #     if u_link.txt:
            #         f.write(u_link.txt)
            #         f.write('\n')
                    
        f.close()        


'''Link extraction and save text in text file
'''

def info_crawl(url,webdriver1):
    links = set()
    with webdriver1 as driver:
        # Set timeout time 
        wait = WebDriverWait(driver, 30)

        # retrive url in headless browser
        driver.get(url)
        links.add(url)

        elems = driver.find_elements_by_xpath("//a[@href]")

        urls_to_visit = set()
        path = './data/content/'+'content'+versity_name+'.txt'
        with open('./content_asset/versity.txt','a',encoding="utf-8")as f:  
            for elem in elems:
                lnk=(elem.get_attribute("href"))
                if lnk !='https://web.facebook.com/' or  lnk !='https://twitter.com/' or lnk !='https://plus.google.com/':

                    urls_to_visit.add(elem.get_attribute("href"))
                    lnk_txt=elem.get_attribute('text')
                    f.write(lnk_txt)
                    f.write('\n')
        f.close()

    return links

           

def cd_call(name,url):
    name=name
    url=url
    
    chrome_driver_path = 'chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Headless driver-1
    # webd = webdriver.Chrome(
    # executable_path=chrome_driver_path, options=chrome_options
    # )
    webd = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    #webd = webdriver.Chrome(ChromeDriverManager().install())
    #calling performance function
    info_retrieve(webd,name,url)


       



# def front_content_crawl(versity_name):
#     url_dic={
#            'BUET':'https://www.buet.ac.bd/web/',
#            'RUET':'https://www.ruet.ac.bd/',
#           'KUET':'http://www.kuet.ac.bd/',
#           'CUET':'https://www.cuet.ac.bd/',
#           'DU':'https://www.du.ac.bd/',
#            'CU':'https://cu.ac.bd/',
#            'BRAC':'https://www.bracu.ac.bd/',
#           'JU':'https://www.juniv.edu/',
#           'JUST':'https://just.edu.bd/',
#           'AUST':'http://www.aust.edu/',
#           'AIUB':'https://www.aiub.edu/',
#           'BUBT':'https://www.bubt.edu.bd/',
#           'UIU':'http://www.uiu.ac.bd/',
#           'RU':'http://www.ru.ac.bd/',
#           'SUST':'https://www.sust.edu/',
#           'NSU':'http://www.northsouth.edu/',
#           'IUT':'https://www.iutoic-dhaka.edu/',
#           'BAU':'https://www.bau.edu.bd/',
#           'IIUC':'https://www.iiuc.ac.bd/',
#           'MIST':'https://mist.ac.bd/',
#           'DUET': 'https://www.duet.ac.bd/',
#           'SBAU': 'http://www.sau.edu.bd/',
#           'JNU': 'https://www.jnu.ac.bd/',
#           'KU': 'https://ku.ac.bd/',
#           'SEU': 'https://seu.edu.bd/',
#           'NSTU': 'http://www.nstu.edu.bd/',
#           'BSMMU': 'https://www.bsmmu.edu.bd/',
#           'SAU': 'http://www.sau.ac.bd/',
#           'PSTU': 'https://www.pstu.ac.bd/',
#           'MBSTU': 'https://mbstu.ac.bd/',
#           'IU': 'https://www.iu.ac.bd/',
#           'BRUR': 'https://brur.ac.bd/',
#           'BUTEX': 'https://www.butex.edu.bd/',
#           'HSTU': 'https://www.hstu.ac.bd/',
#           'COU': 'https://www.cou.ac.bd/',
#           'CMU': 'http://www.cmu.edu.bd/',
#           'SMU': 'https://www.smu.edu.bd/',
#           'PUST': 'https://www.pust.ac.bd/',
#           'BSMRSTU': 'https://www.bsmrstu.edu.bd/s/',
#           'CVASU': 'https://cvasu.ac.bd/',
#           'DAFODIL': 'https://daffodilvarsity.edu.bd/'
#
#     }
#
#
#     url=url_dic[versity_name]
#
#     print(url)
#     d_call(versity_name,url)