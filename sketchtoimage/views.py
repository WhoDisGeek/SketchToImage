import os
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render

from sketchtoimage.settings import BASE_DIR, MEDIA_ROOT


def home_view(request):
    return render(request, 'home.html', {})


def return_image(request, img_name='2'):
    if request.method == 'GET':
        print(img_name)
        img_name = '1'
        print(os.path.join(BASE_DIR, MEDIA_ROOT, 'input_sketches', img_name + str('.jpg')))
        try:

            with open(os.path.join(BASE_DIR, MEDIA_ROOT, 'input_sketches', img_name + str('.jpg')), "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
