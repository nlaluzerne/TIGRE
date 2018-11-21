from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, concatenate
from keras import backend as K
from concat import image_info_gen

# Specify image and training information
img_width, img_height = 100, 100
train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
preprocessing_feature_count = 3
nb_train_samples = 4
nb_validation_samples = 4
epochs = 1
batch_size = 1

# Create image network
image_net_input = Input(shape=(img_width, img_height, 3))
image_net = Conv2D(32, (3, 3))(image_net_input)
image_net = Activation('relu')(image_net)
image_net = MaxPooling2D(pool_size=(2, 2))(image_net)
image_net = Flatten()(image_net)
image_net = Dense(64)(image_net)
image_net = Activation('relu')(image_net)
image_net = Dropout(.5)(image_net)
image_net = Dense(1)(image_net)
image_net = Activation('sigmoid')(image_net)

# Create preprocessing features network
preprocess_net_input = Input(shape=(preprocessing_feature_count,))
preprocess_net = Dense(100)(preprocess_net_input)

# Concatenate networks
merged = concatenate([image_net, preprocess_net])
final = Dense(1,)(merged)
model = Model(inputs=[image_net_input, preprocess_net_input], outputs=final)
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Create generators for training and testing
train_generator = image_info_gen(train_data_dir)
validation_generator = image_info_gen(validation_data_dir)

# Fit data and perform validation check
model.fit_generator(
  train_generator,
  steps_per_epoch=1,
  epochs=epochs,
  validation_data=validation_generator,
  validation_steps=1)
