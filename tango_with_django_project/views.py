from django.shortcuts import render_to_response
from django.template import RequestContext

def error404(request):
    context = RequestContext(request)
    context.status_code = 404
    return render_to_response('error/404.html', {}, context)
