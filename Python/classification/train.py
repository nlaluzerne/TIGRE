from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, concatenate
from keras import backend as K

# Specify image and training information
img_width, img_height = 256, 256
train_data_dir = 'new_train_ff'
test_data_dir = 'new_test_ff'
nb_train_samples = 140
epochs = 1
batch_size = 128

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

model = Model(inputs=image_net_input, outputs=image_net)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# Fit data and perform validation check
model.fit_generator(
  train_generator,
  steps_per_epoch=10,
  epochs=epochs,
  validation_data=test_generator,
  validation_steps=10)
