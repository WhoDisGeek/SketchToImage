instance = None


def get_instance():
    """Docstring."""
    global instance
    if instance is None:
        instance = ImageComparer()
    return instance


class ImageComparer:

    # function to receive request for recognizing the sketch
    # parameters filename
    # call respective recognizing api
    # returns path where target k nearest images are stored
    @staticmethod
    def compare(filename):
        pass
