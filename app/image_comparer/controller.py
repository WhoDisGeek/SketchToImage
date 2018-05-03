import os

import shutil

from app.image_comparer import result
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

    os.makedirs(os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors/gen'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors/target'), exist_ok=True)

    ############################################################################################

    out_file_name = SKETCH_FILE_NAME.split('.')[0] + 'ip_target' + '.h5'
    feature_dataset_target = feat_extract_main(
        all_images=target_images_list,
        out_file=os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors', out_file_name),
        times=1
    )

    ##################################################################################

    out_file_name = SKETCH_FILE_NAME.split('.')[0] + '_gen' + '.h5'
    feature_dataset_gen = feat_extract_main(
        all_images=gen_images_list,
        out_file=os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors', out_file_name),
        times=2
    )

    #######################################################################################
    outfolder = os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors/gen')
    shutil.rmtree(outfolder)
    os.makedirs(outfolder, exist_ok=True)
    filenames = [i.decode("utf-8").split('/')[-1].split('.')[0] + '.txt' for i in feature_dataset_gen['filenames']]
    print('filenames[0] ', filenames[0])
    num_list = feature_dataset_gen['Logits'].tolist()
    print(num_list[0][0])
    i = 0
    for filename in filenames:
        with open(os.path.join(outfolder, filename), 'w+') as log_file:
            for j in num_list[i]:
                log_file.write(str(j) + '\n')
        i = i + 1

    ########################################################################################

    outfolder = os.path.join(BASE_DIR, MEDIA_ROOT, 'feature_vectors/target')
    shutil.rmtree(outfolder)
    os.makedirs(outfolder, exist_ok=True)
    filenames = [i.decode("utf-8").split('/')[-1].split('.')[0] + '.txt' for i in feature_dataset_target['filenames']]
    num_list = feature_dataset_target['Logits'].tolist()
    i = 0
    for filename in filenames:
        with open(os.path.join(outfolder, filename), 'w+') as log_file:
            for j in num_list[i]:
                log_file.write(str(j) + '\n')
        i = i + 1
    print('feature vector done...')
    output_images_list = result.main()
    # images_list = nearest_to_target(gen_images_list=gen_images_list,
    #                                 target_images_list=target_images_list,
    #                                 feature_dataset=feature_dataset)

    # add feature similarity matrix

    # return {
    #     'output_images_list': images_list
    # }

    return {'output_images_list': output_images_list}
