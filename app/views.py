import os

import time
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# upload the sketch and store it some place where
from django.views.decorators.csrf import csrf_exempt

from sketchtoimage.settings import BASE_DIR

from app.sketch_recognizer.controller import recognize
from app.image_generator.controller import generate
from app.image_comparer.controller import compare


@csrf_exempt
def upload_sketch(request):
    if request.method == 'POST':
        settings.SKETCH_FILE_NAME = 'ip_' + str(int(time.time() * 1000)) + '.jpg'
        upload_path = os.path.join(BASE_DIR, settings.MEDIA_ROOT, 'input_sketches')

        # check if path exits else create one..
        try:
            os.path.exists(upload_path)
        except Exception as e:
            print(e)
            os.mkdir(upload_path)

        # check if file with same name already exists..
        # if yes remove it and save the current sketch

        if os.path.exists(os.path.join(upload_path, settings.SKETCH_FILE_NAME)):
            os.remove(os.path.join(upload_path, settings.SKETCH_FILE_NAME))
        default_storage.save(
            os.path.join(upload_path, settings.SKETCH_FILE_NAME), ContentFile(
                request.FILES['sketch'].read()))

    return JsonResponse({
        "success": "true",
        "input_image": settings.SKETCH_FILE_NAME
    })


@csrf_exempt
def execute(request):
    try:
        # returns a dict with classname and target_images_list as keys
        recognizer_response = recognize(filename=settings.SKETCH_FILE_NAME)
    except Exception as ex:
        print('Crap... Exception in Recognizer..')
        print(ex)
        return JsonResponse({
            "success": "false",
            "target_images_list": [],
            "output_images_list": []
        })

    try:
        # returns a dict with gen_images_list as key
        generator_response = generate(classname=recognizer_response['classname'])
    except Exception as ex:
        print('Crap... Exception in Generator..')
        print(ex)
        return JsonResponse({
            "success": "false",
            "target_images_list": recognizer_response['target_images_list'],
            "output_images_list": []
        })

    # recognizer_response = {'target_images_list': ["target_airplane_n02691156_58.jpg",
    #                                               "target_airplane_n02691156_1074.jpg",
    #                                               "target_airplane_n02691156_1512.jpg",
    #                                               "target_airplane_n02691156_2377.jpg",
    #                                               "target_airplane_n02691156_5583.jpg",
    #                                               "target_airplane_n02691156_7476.jpg",
    #                                               "target_airplane_n02691156_9245.jpg",
    #                                               "target_airplane_n02691156_9916.jpg",
    #                                               "target_airplane_n02691156_10578.jpg",
    #                                               "target_airplane_n02691156_53586.jpg"]}
    # generator_response = {'gen_images_list': ["gen_airplane9_0.png",
    #                                           "gen_airplane9_1.png",
    #                                           "gen_airplane9_2.png",
    #                                           "gen_airplane9_3.png",
    #                                           "gen_airplane9_4.png",
    #                                           "gen_airplane9_5.png",
    #                                           "gen_airplane9_6.png",
    #                                           "gen_airplane9_7.png",
    #                                           "gen_airplane9_8.png",
    #                                           "gen_airplane9_9.png",
    #                                           "gen_airplane9_10.png",
    #                                           "gen_airplane9_11.png",
    #                                           "gen_airplane9_12.png",
    #                                           "gen_airplane9_13.png",
    #                                           "gen_airplane9_14.png",
    #                                           "gen_airplane9_15.png"]}

    try:

        # returns a dict with output_images_list as key
        comparer_response = compare(
            target_images_list=recognizer_response['target_images_list'],
            gen_images_list=generator_response['gen_images_list']
        )
    except Exception as ex:
        print(ex)
        print('Crap... Exception in Comparer..')
        return JsonResponse(
            {
                "success": "false",
                "target_images_list": recognizer_response['target_images_list'],
                "output_images_list": generator_response['gen_images_list']
            })

    return JsonResponse(
        {
            "success": "true",
            "target_images_list": recognizer_response['target_images_list'],
            "output_images_list": comparer_response['output_images_list']
        })


    #

    # generator_response = {'gen_images_list': ["gen_airplane9_0.png",
    #                                           "gen_airplane9_1.png",
    #                                           "gen_airplane9_2.png",
    #                                           "gen_airplane9_3.png",
    #                                           "gen_airplane9_4.png",
    #                                           "gen_airplane9_5.png",
    #                                           "gen_airplane9_6.png",
    #                                           "gen_airplane9_7.png",
    #                                           "gen_airplane9_8.png",
    #                                           "gen_airplane9_9.png",
    #                                           "gen_airplane9_10.png",
    #                                           "gen_airplane9_11.png",
    #                                           "gen_airplane9_12.png",
    #                                           "gen_airplane9_13.png",
    #                                           "gen_airplane9_14.png",
    #                                           "gen_airplane9_15.png"]}

    # return JsonResponse(
    #     {
    #         "success": "true",
    #         "target_images_list": recognizer_response['target_images_list'],
    #         "output_images_list": generator_response['gen_images_list']
    #     })

    # comparer_response = compare(
    #     target_images_list=['target_airplane_4201.jpg', 'target_airplane_8732.jpg'],
    #     gen_images_list=['gen_airplane_8241.jpg', 'gen_airplane_2347.jpg']
    # )
    #
    # return JsonResponse({
    #     "success": "true",
    #     "target_images_list": ['target_1010.jpg', 'target_1233.jpg'],
    #     "output_images_list": ['op_3061.jpg', 'op_8273.jpg']
    # })
