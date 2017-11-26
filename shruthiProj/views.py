from django.http import HttpResponse
from datetime import datetime
from  django.template import loader

def index(request):
    date = datetime.date.today();
    template = loader.get_template("index.html")
    variable = {"date":date}
    return HttpResponse(template.render(variable))
