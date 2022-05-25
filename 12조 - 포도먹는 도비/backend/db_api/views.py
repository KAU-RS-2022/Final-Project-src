from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from db_api.models import Test
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers

from ml.inference_cpu import inference
import json

@method_decorator(csrf_exempt, name='dispatch')
def test(request):
    if request.method == 'GET':
        test = Test.objects.get(dataNumber=0)

        data={
            "dataNumber" : test.dataNumber,
            "name" : test.name,
            "description" : test.description,
            
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Wrong Method!")


@method_decorator(csrf_exempt, name='dispatch')
def recommend(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)["checked"]
        print(body)
        data={"sweet":int(body["sweet-debt-amount"]),
        "acidity":int(body["acid-debt-amount"]),
        "body":int(body["body-debt-amount"]),
        "tannin":int(body["tannin-debt-amount"]),
        "type":int(body["type-debt-amount"])}

        returnData = inference(data)
        print(returnData)
        # print(json.loads(request.body.decode('utf-8')))
        return JsonResponse(json.dumps(returnData),safe=False)
    else:
        return HttpResponse("Wrong Method!")
# Create your views here.
