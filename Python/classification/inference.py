from keras import backend as K
from keras.models import model_from_json
import scipy

with open('model.json', 'r') as json_file:
    loaded_model = model_from_json(json_file.read())
    loaded_model.load_weights('model.h5')

dense_layer_output = K.function([loaded_model.layers[0].input],
                                  [loaded_model.layers[-5].output])

def model_input_size(model):
    return tuple([int(a) for a in model.layers[0].input.shape.dims[1:]])

def infer(pics):
    size = model_input_size(loaded_model)
    pics_resized = [scipy.misc.imresize(pic, size) for pic in pics]
    return dense_layer_output([pics_resized])[0]
