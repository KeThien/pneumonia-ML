from django.shortcuts import render
from django.http import JsonResponse


def predict(request):
    return render(request, 'predict.html')


def compute(request):
    return JsonResponse({'id': '1', 'image_url': 'something', 'timestamp': '12/01/2021 10:00', 'result': '0.5', })
