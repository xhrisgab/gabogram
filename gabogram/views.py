from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs '))
    return HttpResponse('Ho, Hi Current server time is {}'.format(now))

def sort_integers(request):
    numb = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numb)
    data = {
            'status': 'ok',
            'numbers': sorted_ints,
            'message': 'Integers sorted successful'
        }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here!'.format(name)
    else:
        message = 'Hello {}! Wellcome to Gabogram'.format(name)
    return HttpResponse(message)
