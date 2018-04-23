from app.image_generator.generator.gan_main import train_gan, test_gan


def generate(classname):
    num_images_gen, images_list = test_gan(classname=classname)
    return {
            'num_images_gen': num_images_gen,
            'images_list': images_list
            }
