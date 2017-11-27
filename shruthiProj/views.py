from django.http import HttpResponse
from datetime import datetime
import time
from datetime import datetime
from  django.template import loader
import os

def index(request):
    dateToday = str(datetime.now());
    template = loader.get_template("index.html")
    # variable = {"date":dateToday}
    return HttpResponse(template.render())
    # return HttpResponse("<h1>Hello the date today is "+dateToday+"</h1>");
def date(request):
    dateToday = str(datetime.now());
    template = loader.get_template("date.html")
    variable = {"date":dateToday}
    return HttpResponse(template.render(variable))

def create(request):
    filesCreated = False;
    for x in range(0,20):
        print("inside for loop");
        newFile = open("/tmp/test/hello"+str(x)+".txt", "w");
        filesCreated = True;
    if(filesCreated):
        return HttpResponse("<h1> files has been created </h1>");
    else:
        return HttpResponse("<h1>HTTP_503_SERVICE_UNAVAILABLE</h1>")


def delete(request):
    path_info = request.META.get('PATH_INFO')
    http_host = request.META.get('HTTP_HOST')
    result = path_info.split("/")
    print(result);
    x = int(result[2]);
    print(http_host)
    for x in range(0,x):
        os.chdir("/tmp/test")
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime);
        oldest = files[0];
        os.remove(oldest);
    return HttpResponse("<h1> the oldest file in this folder is " +oldest+ "</h1>");

