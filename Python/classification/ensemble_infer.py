from feature_extract import all_f

# NOTE: it could be more effecient to read the parameters from a file
from ensemble_train import model

def infer(f, fc):
    return model.predict([all_f(f, fc)])[0]
