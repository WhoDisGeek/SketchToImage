instance = None


def get_instance():
    """Docstring."""
    global instance
    if instance is None:
        instance = SketchRecognizer()
    return instance


class SketchRecognizer:

    # function to receive request for recognizing the sketch
    # parameters filename
    # call respective recognizing api
    # returns path where target k nearest images are stored
    @staticmethod
    def recognize(filename):
        pass
