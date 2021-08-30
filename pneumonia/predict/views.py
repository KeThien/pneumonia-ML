from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from .models import Image

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input

model = tf.keras.models.load_model("ml_model.h5")


def predict(request):
    """Process images uploaded by users"""
    data = Image.objects.all().order_by('-id')
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #
            # Machine Learning Model
            # load the image
            input_img = load_img(path=img_obj.image.path,
                                 target_size=(150, 150))

            # preprocess the image
            input_img = img_to_array(input_img)
            input_img = input_img.reshape(
                (1, input_img.shape[0], input_img.shape[1], input_img.shape[2]))
            input_img = preprocess_input(input_img)

            # make the prediction
            prediction = model.predict(input_img)

            # Edit result field from img_obj
            predict_image = Image.objects.get(id=img_obj.id)
            predict_image.result = prediction
            predict_image.save()

            return render(request, 'predict.html', {'form': form, 'img_obj': img_obj, 'predictions': data})
    else:
        form = ImageForm()
    return render(request, 'predict.html', {'form': form, 'predictions': data})


def compute(request):
    return JsonResponse({'id': '1', 'image_url': 'something', 'timestamp': '12/01/2021 10:00', 'result': '0.5', })
