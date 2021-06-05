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
import time
import sys
import json

from front_page_crawl import info_retrieve
from front_page_link import text_extaction
from front_page_crawl import info_crawl
from faculty_crawl import faculty_info
from  performance import web_performance

if __name__ == "__main__":


    '''URL for the link extractions.
    '''
    front_url=""
    faculty_url = 'https://www.cuet.ac.bd/dept/me/faculty-list'
    
    chrome_driver_path = 'E:/kawser/src/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    
    
    # Headless driver-1
    webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
    )


    '''Extracts all the links from the front page..
    '''
    links=info_crawl(front_url,webdriver)


    '''Extract  info from these links
    '''
    info_retrieve(webdriver,links)


   
    # # Faculty information extraction....
    

    chrome_driver_path = 'E:/kawser/src/chromedriver'

    chrome_options = Options()
    chrome_options.add_argument('--headless')


    # Creating headless driver number two
    webdriver3 = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
    )

    # # Extract faculties details information................
    # """
    # TO DO:
    #      Email indentify
    #      Contact No identify
    #      Qualification Identify
    # """
    
    faculty_info(webdriver3,faculty_url)


    '''Performance test
    '''
    web_performance(webdriver,front_url)
    
   
    
   
    

   



    
   

    


        
       