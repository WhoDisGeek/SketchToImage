import os
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render

from sketchtoimage.settings import BASE_DIR, MEDIA_ROOT


def home_view(request):
    return render(request, 'home.html', {})


def return_image(request, type=None, img_name='2'):
    if request.method == 'GET':
        print(img_name)
        image_path = ''
        if type == 'ip':
            image_path = os.path.join(BASE_DIR, MEDIA_ROOT, 'input_sketches', img_name)
        elif type == 'op':
            image_path = os.path.join(BASE_DIR, MEDIA_ROOT, 'output_sketches', img_name)
        elif type == 'target':
            image_path = os.path.join(BASE_DIR, MEDIA_ROOT, 'cnn1_output', img_name)
        elif type == 'gen':
            image_path = os.path.join(BASE_DIR, MEDIA_ROOT, 'gen_output', img_name)
        print('image path is..', image_path)
        try:

            with open(image_path, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
