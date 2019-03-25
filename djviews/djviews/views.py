# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse
#ef home(request):
    #print(request)
    #rint(dir(request))
   #print(request.method)
   #rint(request.is_ajax)
   #int(request.get_full_path)
    #eturn HttpResponse("<h1>hello worldd</h1>")
def home(request):
    response = HttpResponse()
    response.write("<p>here is the text of the webpage</p>")
    response.write("<p>here is the text of the webpage</p>")
    response.write("<p>here is the text of the webpage</p>")
    return response
