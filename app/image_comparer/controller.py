from app.image_comparer.comparer import


def compare(gen_images_list):
    num_images_gen, images_list = test_gan(classname=classname)
    return {
            'num_images_gen': num_images_gen,
            'images_list': images_list
            }
