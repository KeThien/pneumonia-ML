from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage


def predict(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            result = {'id': '1', 'image_url': 'something', 'timestamp': '12/01/2021 10:00', 'result': '0.5', }
            return render(request, 'predict.html', {'form': form, 'img_obj': img_obj, 'result': result})
    else:
        form = ImageForm()
    return render(request, 'predict.html', {'form': form})


def compute(request):
    return JsonResponse({'id': '1', 'image_url': 'something', 'timestamp': '12/01/2021 10:00', 'result': '0.5', })