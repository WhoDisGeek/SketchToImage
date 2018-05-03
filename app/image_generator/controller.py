import os, sys
import subprocess
from time import sleep

from sketchtoimage.settings import INTERMEDIATE_FILES_PATH, GAN_PATH_PYTHON, GEN_OUTPUT_PATH

classname_mapping = {
    'airplane': 'airplane',
    'balloon': 'hotair_balloon',
    'chair': 'chair',
    'butterfly': 'butterfly',
    'flower': 'flower'

}


def generate(classname):
    print('classname is ..', classname_mapping[classname])
    os.makedirs(INTERMEDIATE_FILES_PATH, exist_ok=True)
    with open(os.path.join(INTERMEDIATE_FILES_PATH, 'classname.txt'), 'w+') as cfile:
        cfile.write(classname + '\n')
    os.makedirs(GEN_OUTPUT_PATH, exist_ok=True)

    # subprocess.call('/home/prime/call_gan.sh')
    # os.system('python /home/prime/Final\ Sem\ Project/code/gans/DCGAN-tensorflow/gan_main.py --dataset=' + classname)
    os.system('python ' + os.path.join(GAN_PATH_PYTHON, 'gan_main.py') + ' --dataset=' + classname
              + ' --intermediate_path=' + INTERMEDIATE_FILES_PATH
              + ' --output_path=' + GEN_OUTPUT_PATH
              )

    sleep(10)
    with open(os.path.join(INTERMEDIATE_FILES_PATH, 'gen_images_list.txt'), 'r') as cfile:
        images_list = [line.rstrip('\n') for line in cfile]
    # print('image_list..', images_list[0])

    with open(os.path.join(INTERMEDIATE_FILES_PATH, 'num_images_gen.txt'), 'r') as cfile:
        num_images_gen = int([line.rstrip('\n') for line in cfile][0])

    # print('num_images_gen', num_images_gen)

    # num_images_gen, images_list = test_gan(dataset=classname_mapping[classname])

    return {
        'num_images_gen': num_images_gen,
        'gen_images_list': images_list
    }
