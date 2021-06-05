from django.shortcuts import render

from django.shortcuts import render,redirect


import cv2
import numpy as np
import threading
from django.http import StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import F
from django.contrib import messages

# authentication r jnno
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth import authenticate as auth_main, login as dj_login

#this is needed for making login compulsary and redirect to login
from django.contrib.auth.decorators import login_required
from django.views.decorators.gzip import gzip_page
from django.conf import settings
from django.http import JsonResponse
import os
import cv2 as cv
from PIL import  Image
# Create your views here.

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
from . front_page_crawl import cd_call
from . performance import pd_call
BASE_DIR = settings.BASE_DIR

detail_perform_data = []
uniList = {}


def home(request):
    print("yes home!----------------")
    fname = './data/' + 'versityList.txt'
    with open(fname, encoding="utf8") as f:
        for line in f:
            chunk = line.split(',')
            flag=0
            firstStr = ''
            secondStr = ''
            for i in chunk:
                if (flag == 1):
                    secondStr = i[:-1]
                if (flag == 0):
                    firstStr = i
                flag = flag + 1
            uniList.update({firstStr : secondStr})
            print(uniList[firstStr])
    context = {'universityList': uniList}
    return render(request, 'home/home.html', context)

def about(request):
    print("yes home!----------------")
    return render(request,'home/about.html')
def add_university(request):
    print("yes add-university!----------------")
    return render(request, 'home/add_university.html')
def addUniversity(request):
    print("yes addUniversity!---------------")
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            urlLink = request.POST.get('urlLink')
            title = title.replace(" ", "")
            title = title.upper()
            urlLink = urlLink.replace(" ", "")
            print(title)
            print(urlLink)
            if title in uniList:
                if uniList[title] == urlLink:
                    messages.success(request, 'This url already exist')
                    return render(request, 'home/add_university.html')
                else:
                    messages.success(request, 'This Title name already exist')
                    return render(request, 'home/add_university.html')
            elif urlLink in uniList.values():
                messages.success(request, 'This url already exist')
                return render(request, 'home/add_university.html')
            else:
                cd_call(title, urlLink)
                pd_call(title, urlLink)
                with open('./data/' + 'versityList.txt', 'a', encoding="utf-8")as f:
                    f.write(title + "," + urlLink)
                    f.write('\n')
                    f.close()
                messages.success(request, 'Successfully crawled data and add the university!')
                return render(request, 'home/add_university.html')

    except:
        path1 = './data/performance/' + 'performance' + title + '.txt'
        if os.path.exists(path1):
            os.remove(path1)
        path2 = './data/content/' + 'content' + title + '.txt'
        if os.path.exists(path2):
            os.remove(path2)
        messages.success(request, 'Not able to crawl or you are not authorized to crawl data for the university!')
        return render(request, 'home/add_university.html')


def deleteUniversity(request):
    context = {'universityList': uniList}
    return render(request, 'home/deleteUniversity.html', context)

def delete_university(request):
    try:
        if request.method == 'POST':
            universityList = request.POST.getlist('keyValue')
            for key in universityList:
                path1 = './data/performance/' + 'performance' + key + '.txt'
                if os.path.exists(path1):
                    os.remove(path1)
                path2 = './data/content/' + 'content' + key + '.txt'
                if os.path.exists(path2):
                    os.remove(path2)
                del uniList[key]
            fname = './data/' + 'versityList.txt'
            if os.path.exists(fname):
                os.remove(fname)
            with open('./data/' + 'versityList.txt', 'a', encoding="utf-8")as f:
                for key in uniList:
                    f.write(key + "," + uniList[key])
                    f.write('\n')
                f.close()
        messages.success(request, 'Successfully deleted database for selected university!')
        context = {'universityList': uniList}
        return render(request, 'home/home.html', context)
    except:
        context = {'universityList': uniList}
        messages.success(request, 'Not deleted data-base for selected university!')
        return render(request, 'home/home.html', context)


def update_db(request):

    print("update db camse!")
    
    try:
        if request.method == 'POST':
            universityList = request.POST.getlist('keyValue')
            if len(universityList) == 0:
                messages.success(request, 'No university has selected')
                context = {'universityList': uniList}
                return render(request, 'home/home.html', context)
            for key in universityList:
                alertMessage = 'Not able to crawl or you are not authorized to crawl data for(' + key + ').Try again for(' + key + ')'
                cd_call(key, uniList[key])
                pd_call(key, uniList[key])

        messages.success(request, 'Successfully updated database for selected university!')
        context = {'universityList': uniList}
        return render(request, 'home/home.html', context)
    except:
        context = {'universityList': uniList}
        messages.success(request, alertMessage)
        return render(request, 'home/home.html', context)

def check(fname, txt):
    with open(fname, encoding="utf8") as dataf:
        return any(txt.lower() in line.lower() for line in dataf)
def calculate_performance(request, versity_name, marks_content, contents):
    nullValue = 0
    fname = './data/performance/' + 'performance' + versity_name + '.txt'
    if os.path.exists(fname):
        with open(fname, encoding="utf8") as dataf:
            lines = dataf.readlines()
            temp_load_time = lines[0].partition(':')[2]
            temp_load_time = temp_load_time.strip()
            load_time = float(temp_load_time)
            print(fname + "load_time:", load_time)
            mark_of_load_time = max(10 - load_time, 0)

            connect_start = lines[7].partition(':')[2]
            val_connect_start = float(connect_start.strip())
            v1 = max(40 - val_connect_start * 4.0, 0)

            connect_end = lines[8].partition(':')[2]
            val_connect_end = float(connect_end.strip())
            v2 = max(40 - val_connect_end * 4.0, 0)

            dom_complete = lines[10].partition(':')[2]
            val_dom_complete = float(dom_complete.strip())
            v3 = max(40 - val_dom_complete / 12.5, 0)

            dom_content_loaded_event_end = lines[11].partition(':')[2]
            val_dom_content_loaded_event_end = float(dom_content_loaded_event_end.strip())
            v4 = max(40 - val_dom_content_loaded_event_end / 12.5, 0)

            dom_content_loaded_event_start = lines[12].partition(':')[2]
            val_dom_content_loaded_event_start = float(dom_content_loaded_event_start.strip())
            v5 = max(40 - val_dom_content_loaded_event_start / 12.5, 0)

            dom_interactive = lines[13].partition(':')[2]
            val_dom_interactive = float(dom_interactive.strip())
            v6 = max(40 - val_dom_interactive / 12.5, 0)

            domain_lookup_end = lines[14].partition(':')[2]
            val_domain_lookup_end = float(domain_lookup_end.strip())
            v7 = max(40 - val_domain_lookup_end * 4.0, 0)

            domain_lookup_start = lines[15].partition(':')[2]
            val_domain_lookup_start = float(domain_lookup_start.strip())
            v8 = max(40 - val_domain_lookup_start * 4.0, 0)

            duration = lines[16].partition(':')[2]
            val_duration = float(duration.strip())
            v9 = max(40 - val_duration / 12.5, 0)

            fetch_start = lines[19].partition(':')[2]
            val_fetch_start = float(fetch_start.strip())
            v10 = max(40 - val_fetch_start * 4.0, 0)

            load_event_end = lines[20].partition(':')[2]
            val_load_event_end = float(load_event_end.strip())
            v11 = max(40 - val_load_event_end / 12.5, 0)

            load_event_start = lines[21].partition(':')[2]
            val_load_event_start = float(load_event_start.strip())
            v12 = max(40 - val_load_event_start / 12.5, 0)

            redirect_end = lines[23].partition(':')[2]
            val_redirect_end = float(redirect_end.strip())
            v13 = max(40 - val_redirect_end * 4.0, 0)

            redirect_start = lines[24].partition(':')[2]
            val_redirect_start = float(redirect_start.strip())
            v14 = max(40 - val_redirect_start * 4.0, 0)

            request_start = lines[25].partition(':')[2]
            val_request_start = float(request_start.strip())
            v15 = max(40 - val_request_start * 4.0, 0)

            response_start = lines[26].partition(':')[2]
            val_response_start = float(response_start.strip())
            v16 = max(40 - val_response_start * 4.0, 0)

            secure_connection_start = lines[27].partition(':')[2]
            val_secure_connection_start = float(secure_connection_start.strip())
            v17 = max(40 - val_secure_connection_start * 4.0, 0)

            unload_event_end = lines[29].partition(':')[2]
            val_unload_event_end = float(unload_event_end.strip())
            v18 = max(40 - val_unload_event_end * 4.0, 0)

            unload_event_start = lines[30].partition(':')[2]
            val_unload_event_start = float(unload_event_start.strip())
            v19 = max(40 - val_unload_event_start * 4.0, 0)

            worker_start = lines[31].partition(':')[2]
            val_worker_start = float(worker_start.strip())
            v20 = max(40 - val_worker_start * 4.0, 0)

            mark_of_performance = (v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19+v20)/20.0
            print(mark_of_performance)
            performance_of_page = (mark_of_performance * 100) / 40

            perData = {
                'versityName': versity_name,
                'loadTime': load_time,
                'markLoadTime': mark_of_load_time,
                'connect_start': val_connect_start,
                'connect_end': val_connect_end,
                'domComplete': val_dom_complete,
                'domContentLoadEventStart': val_dom_content_loaded_event_start,
                'domContentLoadEventEnd': val_dom_content_loaded_event_end,
                'domInterActive': val_dom_interactive,
                'domainLookUpEnd': val_domain_lookup_end,
                'domainLookUpStart': val_domain_lookup_start,
                'duration': val_duration,
                'fetchStart': val_fetch_start,
                'loadEventEnd': val_load_event_end,
                'loadEventStart': val_load_event_start,
                'redirectEnd': val_redirect_end,
                'redirectStart': val_redirect_start,
                'request_start': val_request_start,
                'response_start': val_response_start,
                'unloadEventEnd': val_unload_event_end,
                'unloadEventStart': val_unload_event_start,
                'secureConnectionStart': val_secure_connection_start,
                'workerStart': val_worker_start,
                'markPerformance': mark_of_performance,
                'markContent': marks_content,
                'contents': contents
            }
            detail_perform_data.append(perData)

            print(fname + ": performance", mark_of_performance)
            print(fname + ": load time", mark_of_load_time)
            return mark_of_load_time + mark_of_performance
    else:
        return nullValue



        


def content_calculation(request,versity_name):
    nullValue = 0
    key_string= {

        '1':['vision', 'mission', 'objective', 'goal' ] ,
        '2':[ 'webmail', 'mail', 'web mail' ],
        '3':[ 'faculties', 'faculty list', 'faculty' ],
        '4':[ 'administration' ],
        '5':[ 'workshop', 'seminar' ],
        '6':[ 'research' ],
        '7':[ 'conference' ],
        '8':[ 'publication' ],
        '9':[ 'Academic program' ],
        '10':[ 'department' ],
        '11':[ 'institute' ],
        '12':[ 'career', 'job', 'field' ],
        '13':['accommodation', 'accomodation','acomodation',  'residence' ],
        '14':[ 'transportation',  'transport' ],
        '15':[ 'library' ],
        '16':[ 'online requisition', 'online course registration', 'online class', 'online application',
               'online registration', 'online service', 'online admission', 'online learning', 'online exam' ],
        '17':[ 'notice' ],
        '18':[ 'news', 'event' ],
        '19':[ 'Alumni' ],
        '20':[ 'Convocation' ],
        '21':[ 'scholarship' ],
        '22':[ 'IQAC' ],
        '23':[ 'Admission' ],
        '24':[ 'FAQ' ],
        '25':[ 'Academic information', 'Academic regulation', 'Academic calendar' ]

        }

    tot_found = 0
    marks_content = 0
    val=[]
    path = './data/content/' + 'content' + versity_name + '.txt'
    if os.path.exists(path):
        for key, values in key_string.items():
            for value in values:
                f = False

                if check(path, value):
                    f = True

                if f == True:
                    tot_found += 1
                    val.append(value)
                    break
        # Open the performance text file calculate load time and others

        marks_content = tot_found * 2
        performance = calculate_performance(request, versity_name, marks_content, val)
        if (performance == 0):
            return nullValue
        else:
           return marks_content + performance
    else:

        return nullValue


def graph(request):
    detail_perform_data.clear()
   
    plot_x =[]
    plot_y=[]
    

    if request.method == 'POST':
         universityList = request.POST.getlist('keyValue')
         for key in universityList:
             alertMessage = 'Data not found for(' + key + ').Please update database for(' + key+')'
             try:
                 value = content_calculation(request, key)
                 if (value == 0):
                     messages.success(request, alertMessage)
                 else:
                     plot_x.append(key)
                     plot_y.append(value)
             except:
                 messages.success(request, alertMessage)





    # Drawing the chart using plotly
    fig = go.Figure(
    data=[go.Bar(x=plot_x,y=plot_y)]
    
    )
    plot_div = plot(fig,output_type='div')

    
    return render(request, "home/graph.html", context={'plot_div': plot_div})


    def checkbox(request):
        print("yes")

def detail_data_view(request):
    print(detail_perform_data)
    context={'performData':detail_perform_data}

    return render(request,'home/detail_view.html',context)