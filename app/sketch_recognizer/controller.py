from app.sketch_recognizer.recognizer.KNN import main


def recognize(filename):
    response = main(sketch_path=filename, as_submodule=True)
    return response
