instance = None


def get_instance():
    """Docstring."""
    global instance
    if instance is None:
        instance = ImageGenerator()
    return instance


class ImageGenerator:

    # function to receive request for generating a sketch
    # parameters classname
    # call respective generating api
    # returns a json containing keys num_of_images and path to generated images
    @staticmethod
    def generate(classname):
        pass
