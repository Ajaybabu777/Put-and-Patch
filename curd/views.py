from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from.models import Task
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def post(request):
    try:    
        data = json.loads(request.body)
        titttli = data["tittle"]
        description = data["descra"]

        postObj =Task(tittle = titttli, descra=description)

        postObj.save()

        return JsonResponse ({
            "message" : "Data Saved Succesfully"
        })

    
    except Exception as ex:
        return JsonResponse ({
            "message":str(ex)
        })


@csrf_exempt
@require_http_methods(["PUT"])
def put(request):
    try:    
        data = json.loads(request.body)
        titttli = data["tittle"]
        description = data["descra"]
        idOfPostMethod = data["id"]

        putobj=Task.objects.get(id = idOfPostMethod)

        if putobj:
            putobj.tittle = titttli
            putobj.descra = description


        putobj.save()

        return JsonResponse ({
            "message" : "Data Saved Succesfully"
        })

    
    except Exception as ex:
        return JsonResponse ({
            "message":str(ex)
        })



@csrf_exempt
@require_http_methods(["PATCH"])
def patch(request):
    try:    
        data = json.loads(request.body)
        idOfPostMethod = data["id"]

        patchobj=Task.objects.get(id = idOfPostMethod)

        if patchobj:
            if "tittle" in data and data["tittle"] != "":
                patchobj.tittle = data["tittle"]

            if "descra" in data and data["descra"] != "":
                patchobj.descra = data["descra"]
                
            patchobj.save()

            return JsonResponse ({
                "message" : "Data Saved Succesfully"
                })

    except Exception as ex:
        return JsonResponse ({
            "message":str(ex)
        })