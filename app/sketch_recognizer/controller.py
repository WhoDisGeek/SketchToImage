from app.sketch_recognizer.recognizer.KNN import main


# returns a dict with classname and target_images_list as keys
def recognize(filename):
    response = main(sketch_path=filename, as_submodule=True)
    return response
