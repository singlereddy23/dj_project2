from django.http import HttpResponse
from django.shortcuts import render
import os

file_path=os.path.abspath(__file__)
pro_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_dir_path)

def index(request):
    return HttpResponse("<marquee direction=\"left\"><h1>REQUIREMENTS OF THE DAY</h1></marquee>")

def html_respo(request):
    file_addr=os.path.join(dir_path,"sample.html") #1.dynamically called
    #fp=open(r'C:\Users\singl\Desktop\kamal\project2\sample.html',"r") #2. relatively called
    fp=open(file_addr,"r")
    data=fp.read()
    
    return HttpResponse(data)

def rend_demo(request):
        return render(request,"sample.html")

def sam_demo(request):
        return render(request,"html_demo/sample.html")