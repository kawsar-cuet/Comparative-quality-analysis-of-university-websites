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




def web_performance(webdriver,uni_name,url):

    path = './data/performance/'+'performance'+uni_name+'.txt'
    if os.path.exists(path):
         os.remove(path)
    
    with open(path,'a',encoding="utf-8")as f: 
        stream = urllib2.urlopen(url)
        start_time = time()
        output = stream.read()
        end_time = time()
        stream.close()

        print("step-1")

        f.write("Webpage loading time : %s" % str(end_time-start_time))
        f.write('\n')

        # Creating headless driver number two
        # driver=webdriver

        with webdriver as driver:

            

            wait = WebDriverWait(driver, 10)
            # driver.get(url)   

            print("step-2")

            performance_data = driver.execute_script("return window.performance.getEntries();")
            # print(performance_data)
            driver.quit()
            
            f.write("Webpage loadevent time diff : %s" % str(performance_data[0]["loadEventEnd"]-performance_data[0]["loadEventStart"]))
            f.write('\n')
            f.write("Webpage Domainlookup time diff : %s" % str(performance_data[0]["domainLookupEnd"]-performance_data[0]["domainLookupStart"]))
            f.write('\n')
            f.write("Webpage domcontentloadevent time diff : %s" % str(performance_data[0]["domContentLoadedEventEnd"]-performance_data[0]["domContentLoadedEventEnd"]))
            f.write('\n')
            f.write("Webpage Server connect time diff : %s" % str(performance_data[0]["connectEnd"]-performance_data[0]["connectStart"]))
            f.write('\n')
            f.write("Webpage Serverresponse time diff : %s" % str(performance_data[0]["responseEnd"]-performance_data[0]["requestStart"]))
            f.write('\n')
            f.write("Webpage Ridirect time diff : %s" % str(performance_data[0]["redirectEnd"]-performance_data[0]["redirectStart"]))
            f.write('\n')
            f.write("Connect start : %s" % str(performance_data[0]["connectStart"]))
            f.write('\n')
            f.write("Connect end : %s" % str(performance_data[0]["connectEnd"]))
            f.write('\n')

            f.write(" decodedBodySize : %s" % str(performance_data[0]["decodedBodySize"]))
            f.write('\n')
            f.write("domComplete : %s" % str(performance_data[0]["domComplete"]))
            f.write('\n')
            f.write("domContentLoadedEventEnd : %s" % str(performance_data[0]["domContentLoadedEventEnd"]))
            f.write('\n')
            f.write("domContentLoadedEventStart : %s" % str(performance_data[0]["domContentLoadedEventStart"]))
            f.write('\n')
            f.write("domInteractive : %s" % str(performance_data[0]["domInteractive"]))
            f.write('\n')
            f.write("domainLookupEnd : %s" % str(performance_data[0]["domainLookupEnd"]))
            f.write('\n')
            f.write("domainLookupStart: %s" % str(performance_data[0]["domainLookupStart"]))
            f.write('\n')


            f.write("duration: %s" % str(performance_data[0]["duration"]))
            f.write('\n')
            f.write("encodedBodySize: %s" % str(performance_data[0]["encodedBodySize"]))
            f.write('\n')
            f.write("entryType: %s" % str(performance_data[0]["entryType"]))
            f.write('\n')
            f.write("fetchStart: %s" % str(performance_data[0]["fetchStart"]))
            f.write('\n')
            f.write("loadEventEnd: %s" % str(performance_data[0]["loadEventEnd"]))
            f.write('\n')
            
            f.write("loadEventStart: %s" % str(performance_data[0]["loadEventStart"]))
            f.write('\n')    
            f.write("redirectCount: %s" % str(performance_data[0]["redirectCount"]))
            f.write('\n')
            
            f.write("redirectEnd: %s" % str(performance_data[0]["redirectEnd"]))
            f.write('\n')

            f.write("redirectStart: %s" % str(performance_data[0]["redirectStart"]))
            f.write('\n')
            f.write("requestStart: %s" % str(performance_data[0]["requestStart"]))
            f.write('\n')
            f.write("responseStart: %s" % str(performance_data[0]["responseStart"]))
            f.write('\n')
            
            f.write("secureConnectionStart: %s" % str(performance_data[0]["secureConnectionStart"]))
            f.write('\n')
            f.write("transferSize: %s" % str(performance_data[0]["transferSize"]))
            f.write('\n')
            f.write("unloadEventEnd: %s" % str(performance_data[0]["unloadEventEnd"]))
            f.write('\n')

            f.write("unloadEventStart: %s" % str(performance_data[0]["unloadEventStart"]))
            f.write('\n')

            f.write("workerStart: %s" % str(performance_data[0]["workerStart"]))
            f.write('\n')
            
            

def pd_call(name,url):
    name=name
    url=url
    
    chrome_driver_path = 'chromedriver'
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Headless driver-1
    # webd = webdriver.Chrome(
    # executable_path=chrome_driver_path, options=chrome_options
    # )
    webd = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    #calling performance function
    web_performance(webd,name,url)


       



# def performance_crawl(versity_name):
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
#           'COU' : 'https://www.cou.ac.bd/',
#           'CMU': 'http://www.cmu.edu.bd/',
#           'SMU': 'https://www.smu.edu.bd/',
#           'PUST': 'https://www.pust.ac.bd/',
#           'BSMRSTU': 'https://www.bsmrstu.edu.bd/s/',
#           'CVASU': 'https://cvasu.ac.bd/',
#           'DAFODIL': 'https://daffodilvarsity.edu.bd/'
#
#
#
#     }
#
#     url=url_dic[versity_name]
#
#     print(url)
#     d_call(versity_name,url)
       
        

        