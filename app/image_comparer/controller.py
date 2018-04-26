import os

from sketchtoimage.settings import MEDIA_ROOT, BASE_DIR, SKETCH_FILE_NAME

# import os
# if 'PYTHONPATH' not in os.environ:
#     os.environ['PYTHONPATH'] = ''
#     print('Python path is empty..')
#
# os.environ["PYTHONPATH"] = MODEL_PATH + os.pathsep + os.environ["PYTHONPATH"]

from app.image_comparer.feature_vector.feat_extract_main import feat_extract_main


def compare(gen_images_list, target_images_list):
    gen_images_list = [os.path.join(BASE_DIR, MEDIA_ROOT, 'gen_output', i) for i in gen_images_list]
    target_images_list = [os.path.join(BASE_DIR, MEDIA_ROOT, 'cnn1_output', i) for i in target_images_list]
    all_images = gen_images_list + target_images_list
    out_file_name = SKETCH_FILE_NAME.split('.')[0] + '.h5'

    os.makedirs(os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors'), exist_ok=True)

    feature_dataset = feat_extract_main(
        all_images=all_images,
        out_file=os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors', out_file_name)
    )
    print('feature_dataset is .. ', feature_dataset)
    # images_list = nearest_to_target(gen_images_list=gen_images_list,
    #                                 target_images_list=target_images_list,
    #                                 feature_dataset=feature_dataset)

    # add feature similarity matrix

    # return {
    #     'output_images_list': images_list
    # }

    return {'output_images_list': []}
