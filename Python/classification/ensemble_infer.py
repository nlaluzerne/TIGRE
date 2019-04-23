from feature_extract import all_f

# NOTE: it could be more effecient to read the parameters from a file
from ensemble_train import model, scaler

def infer(f, fc):
    X = [all_f(f, fc)]
    X = scaler.transform(X)
    return model.predict_proba(X)[0][1]
