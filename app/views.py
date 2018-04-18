import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# upload the sketch and store it some place where
from django.views.decorators.csrf import csrf_exempt

from app.sketch_recognizer.controller import SketchRecognizer


@csrf_exempt
def upload_sketch(request):
    if request.method == 'POST':
        settings.SKETCH_FILE_NAME = '1.jpg'
        upload_path = os.path.join(settings.MEDIA_ROOT + 'input_sketches')
        try:
            os.chdir(upload_path)
        except Exception as e:
            print(e)
            os.mkdir(upload_path)
            # os.chdir(settings.MEDIA_ROOT + 'input_sketches')
        if os.path.exists(os.path.join(upload_path, settings.SKETCH_FILE_NAME)):
            os.remove(os.path.join(upload_path, settings.SKETCH_FILE_NAME))
        default_storage.save(
            os.path.join(upload_path, settings.SKETCH_FILE_NAME), ContentFile(
                request.FILES['sketch'].read()))
        response = None
        # SketchRecognizer.recognize(settings.SKETCH_FILE_NAME)

    return JsonResponse({"success": "true", "images_list": "this is a list [1.jpg,2.jpg]"})


@csrf_exempt
def execute(request):
    return JsonResponse({"success": "true", "images_list": "this is a list [1.jpg,2.jpg]"})
