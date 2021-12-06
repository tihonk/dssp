from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from types import SimpleNamespace
import json


@csrf_exempt
def dsspcalc(request):
    if request.method == 'POST':
        json_object = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    return HttpResponse(json_object.value)
