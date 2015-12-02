from django.template.loaders import filesystem
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render
admin.autodiscover()
#   t = get_template('/bootstrap/bootstrap-master/helloworld.html')
#  html = t.render(Context({'':}))
#  return HttpResponse(html)
def request_squeezer(request):
    return render_to_response('test.html')

def SqueezerHighchartsCDF(request):
    pass

def SqueezerHighchartsHis(request):
    pass
@csrf_exempt
def CallShell(request):
    print request.GET
    sn =  request.GET['text1']
    cn =  request.GET['text2']
    svn =  request.GET['text3']
    sla =  request.GET['text4']
    message = os.popen('/django/mysite/mysite/templates/bin/squeezerTest.sh '+sn+' '+cn+' '+svn+' '+sla)
    return HttpResponse(message.read())

@csrf_exempt
def test(request):
    f1 = open('/home/hxx/squeezer/sojournCdf75.txt','r')
    f2 = open('/home/hxx/squeezer/waitCdf75.txt','r')
    f3 = open('/home/hxx/squeezer/sojournHis75.txt','r')
    f4 = open('/home/hxx/squeezer/waitHis75.txt','r')
    f5 = open('/home/hxx/squeezer/powercap75.log').read()
    lie1=[]
    lie2=[]
    lie3=[]
    lie4=[]
    lie5=[]
    lie6=[]
    lie7=[]
    lie8=[]
    for line in f1:
        line=line.split(', ')
        lie1.append(line[1])
        lie2.append(line[2])
    lie1[0]='0'
    x1=map(float,lie1)
    lie2[0]=0
    y1=map(float,lie2)
    for i in range(0,len(x1)):
	x1[i]=x1[i]*1000
    x1=map(str,x1)
    for line in f2:
        line=line.split(', ')
        lie3.append(line[1])
        lie4.append(line[2])
    lie3[0]='0'
    x2=map(float,lie3)
    lie4[0]=0
    y2=map(float,lie4)
    for i in range(0,len(x2)):
	x2[i]=x2[i]*1000
    x2=map(str,x2)
    for line in f3:
        line=line.split(', ')
        lie5.append(line[1])
        lie6.append(line[2])
    lie5[0]='0'
    lie6[0]=0
    x3=map(float,lie5)
    s3=0.0
    y3=map(float,lie6)
    for i in range(0,len(x3)):
	x3[i]=x3[i]*1000
    x3=map(str,x3)
    for i in y3:
	s3=s3+i
    for i in range(0,len(y3)):
	y3[i]=y3[i]/s3*100
    for line in f4:
        line=line.split(', ')
        lie7.append(line[1])
        lie8.append(line[2])
    lie7[0]='0'
    lie8[0]=0
    x4=map(float,lie7)
    s4=0.0
    y4=map(float,lie8)
    for i in range(0,len(x4)):
	x4[i]=x4[i]*1000
    x4=map(str,x4)
    for i in y4:
	s4+=i
    for i in range(0,len(y4)):
	y4[i]=y4[i]/s4*100
    f5 = f5.replace('\n','&')
    return render(request,'requestsqueezer.html',{'xdata1':x1,'ydata1':y1,'xdata2':x2,'ydata2':y2,'xdata3':x3,'ydata3':y3,'xdata4':x4,'ydata4':y4,'log':f5})



def add(request):
    f1=open('/home/hxx/squeezer/sojournCdf75.txt','r')
    lie1=[]
    lie2=[]    
    for line in f1:
        line=line.split(', ')
        lie1.append(line[1])
        lie2.append(line[2])
    x1=lie1[1:]
    y1=map(float,lie2[1:])
    return render(request,'index.htm',{'xdata1':x1,'ydata1':y1})
def test1(request):
    return render(request,'index.htm')
