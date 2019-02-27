"""
Tools intended to assist with image classification.

Much credit to:
    https://keras.io/
    https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
"""

import os
from random import shuffle
import shutil
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.optimizers import SGD, Adam

"""
Tool with the purpose of simplifying the handling of image data.
ImageSet instances allow for the use of a generator on a
Standard Image Collection (defined below).

Standard Image Collection refers to the following structuring of image data:

Images/
    category_1/
        category_1_example_1.jpg
        category_1_example_2.jpg
        ...
    category_2/
        category_2_example_1.jpg
        category_2_example_2.jpg
        ...
    ...

The images do not have to be of consistent size. There are expected to be two or
more image categories.
"""
class ImageSet(object):

    def __init__(self, data_path, aug_dict=dict(), batch_size=64, image_resize_dims=(150, 150)):
        """
        Initialized with image data characteristics.

        Args:
            data_path: Path to a Standard Image Collection
            aug_dict: Dictionary of image augmentations to be applied. Arguement
                format should match Keras's ImageDataGenerator(...)
                https://keras.io/preprocessing/image/
            batch_size: Number of images to be yielded by generator at each
                training step
            image_resize_dims: Dimensions that generator should resize all
                images to
        Raises:
            AttributeError: If provided data_path does not refer to a
                Standard Image Collection
        """

        if not self.is_collection_valid(data_path):
            raise AttributeError("Data path does not refer to a Standard Image Collection")

        self.batch_size = batch_size
        self.image_category_count, self.image_example_count = self.get_collection_info(data_path)

        datagen = image.ImageDataGenerator(**aug_dict)

        if self.image_category_count == 2:
            category_mode = "binary"
        elif self.image_category_count > 2:
            category_mode = "categorical"

        self.generator = datagen.flow_from_directory(data_path,
            target_size=image_resize_dims, batch_size=batch_size,
            class_mode=category_mode)

    @staticmethod
    def is_collection_valid(collection_path):
        """
        Determines whether or not image set is a valid Standard Image Collection

        Args:
            collection_path: Path to collection in question
        Return:
            True only if Path refers to a Standard Image Collection
        """

        # Verify that path passed refers to a directory
        if not os.path.isdir(collection_path):
            return False

        # Verify that path contains directories for more than two categories
        if len(os.listdir(collection_path)) < 2:
            return False

        for category in os.listdir(collection_path):

            category_path = os.path.join(collection_path, category)

            # If non-folder found to exist in collection
            if not os.path.isdir(category_path):
                return False

            # Verify that none of the items in the category_dir are themselves directories
            for image_name in os.listdir(category_path):
                image_path = os.path.join(category_path, image_name)
                if os.path.isdir(image_path):
                    return False

        # Path must point to a Standard Image Collection
        return True

    @staticmethod
    def get_collection_info(collection_path):
        """
        Provides info about a Standard Image Collection.

        Args:
            collection_path: Path to a Standard Image Collection

        Returns:
            Pair (c, e) where c is the number of image categories and e is the
            total number of image examples. If given path is not a Standard
            Image Collection, None will be returned
        """

        if not ImageSet.is_collection_valid(collection_path):
            return None

        image_category_count = 0
        image_example_count = 0
        for image_category in os.listdir(collection_path):
            image_category_count += 1
            for image_example in os.listdir(os.path.join(collection_path, image_category)):
                image_example_count += 1
        return image_category_count, image_example_count

    @staticmethod
    def create_category_dir_shell(src, copy_dir_name):
        """
        Creates empty image category folders matching those in directory passed.
        Images are not copied.

        Args:
            src: Path to a Standard Image Collection
            copy_dir_name: Desired name of new directory
        """
        os.makedirs(copy_dir_name)
        for category_path in os.listdir(src):
            category = os.path.basename(category_path)
            os.makedirs(os.path.join(copy_dir_name, category))

    # TODO:
    # - Consider allowing user to specifiy directory names (currently just split into "Training" and "Validation")
    # - Consider adding alternative partition schema (testing data? How could this be done?)
    @staticmethod
    def partition_image_collection(image_collection_path, validation_example_count):
        """
        Partitions image collection into training and validation data
        directories.

        Args:
            image_collection_path: Path to a Standard Image Collection
            validation_example_count: Number of examples per category to use in
                validation data
        """
        ImageSet.create_category_dir_shell(image_collection_path, "Train")
        ImageSet.create_category_dir_shell(image_collection_path, "Validation")

        for folder in os.listdir(image_collection_path):

            folder_contents = os.listdir(os.path.join(image_collection_path, folder))
            small_content_subset, large_content_subset = ImageSet.partiton_list(folder_contents, validation_example_count)

            cat_folder_src = os.path.join(image_collection_path, folder)
            cat_folder_train = os.path.join("Train", folder)
            cat_folder_validation = os.path.join("Validation", folder)

            ImageSet.copy_dir(cat_folder_src, cat_folder_validation, small_content_subset)
            ImageSet.copy_dir(cat_folder_src, cat_folder_train, large_content_subset)

    @staticmethod
    def copy_dir(src, dst, file_list):
        """
        Copies set of files from src directory into dst directory.

        Args:
            src: Source directory
            dst: Destination directory
            file_list: List of files to be transfered from src to dst. Assumes
                only basenames given (ie. file.txt and not path/to/file.txt)
        """
        for file_path in file_list:
            shutil.copy(os.path.join(src, file_path), dst)

    # TODO:
    # - Consider error throwing on invalid arguments
    @staticmethod
    def partiton_list(the_list, smaller_list_size):
        """
        Randomly partitions list into two subsets.

        Args:
            the_list: Generic list. Has contents popped after method call.
            smaller_list_size: Number of list elements to be partitioned into
                smaller list
        """
        shuffle(the_list)
        small_list = []
        large_list = []
        orig_list_size = len(the_list)
        for i in range(smaller_list_size):
            small_list.append(the_list.pop())
        for i in range(orig_list_size - smaller_list_size):
            large_list.append(the_list.pop())
        return small_list, large_list

"""
Tool allows a pre-trained Keras deep convolutional neural network to have a
new top layer trained on new data.

Training is done in two phases. In the first phase, only the newly added top
layer(s) are made trainable. This can be done with aggressive
regularization (dropout offered here), as imported weights are kept. After
this has been done, a round of fine-tuning can be done on the network. This
involves an additional set of training passes on a much deeper subset of the
network's layers. A slow learning rate is suggested for the latter process.
"""

# TODO:
# - Test
# - Add ability to validate model on image set directly
# - Add ability to predict labels on testing data
# - Consider adding ensembling method
# - Consider allowing trained models to be saved and recovered
# - Consider allowing a grid search to be performed with hyperparameters
class TransferModel(object):

    def __init__(self, base_model, top_model_guide):
        """
        Base model and schema for new learned layers are specified.

        Args:
            base_model: Keras pre-trained and un-compiled model with its top
                layers chopped off
            top_model_guide: List of tuples (wi, di) where each dense layer i
                has its width (wi) and dropout (di) specified.
        """
        self.base_model = base_model
        self.top_model_guide = top_model_guide

    @staticmethod
    def train_model(model, train_set, optimizer, epochs, val_set=None):
        """
        Model is trained on the given data according to the specifications
        passed. Validation data can be supplied as well.

        Args:
            model: Keras pre-trained and un-compiled model with its top layers
                chopped off
            train_set: ImageSet containing the data to be trained on
            optimizer: Training optimizer
            epochs: Number of training epochs
            val_set: ImageSet containing validation data
        """
        if (train_set.image_category_count == 2):
            loss = "binary_crossentropy"
        else:
            loss = "categorical_crossentropy"

        model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])

        # Use validation data if provided
        if val_set is None:
            model.fit_generator(train_set.generator,
            steps_per_epoch=train_set.image_example_count // train_set.batch_size,
            epochs=epochs)
        else:
            model.fit_generator(train_set.generator,
            steps_per_epoch=train_set.image_example_count // train_set.batch_size,
            epochs=epochs,
            validation_data=val_set.generator,
            validation_steps=val_set.image_example_count // val_set.batch_size)

    @staticmethod
    def stack_models(base_model, image_category_count, top_model_guide):
        """
        Stacks a set of Dense layers on top of a model. ReLu activation function
        used for all but output layer. Largely inspired by https://keras.io/applications/

        Args:
            base_model: Keras pre-trained and un-compiled model with its top
                layers chopped off
            image_category_count: Number of image categories
            top_model_guide: List of tuples (wi, di) where each dense layer i
                has its width (wi) and dropout (di) specified.
        Raises:
            AttributeError: If image classes are less than 2
        """
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        for layer_tup in top_model_guide:
            layer_size, dropout = layer_tup
            x = Dense(layer_size, activation="relu")(x)
        if image_category_count == 2:
            predictions = Dense(1, activation="sigmoid")(x)
        elif image_category_count > 2:
            predictions = Dense(image_category_count, activation="softmax")(x)
        else:
            raise AttributeError("Invalid image category count")

        return Model(inputs=base_model.input, outputs=predictions)

    def fit(self, train_set, epochs, optimizers, val_set=None, top_layers_to_unfreeze=-1):
        """
        Fits model to image data passed. Model is first fit with the all layers
        in the base model frozen. After this is done fine tuning can be
        performed on the desired number of layers from top.

        Args:
            train_set: ImageSet containing the data to be trained on
            epochs: tuple (te, fe) where te is transfer learning epochs and fe
                is fine-tuning epochs
            optimizers: tuple (to, fo) where to is training optimizer and fo is
                fine-tuning optimizer
            val_set: ImageSet containing validation data
            top_layers_to_unfreeze: Number of layers to un-freeze during
                fine-tuning
        """

        trans_learn_epochs, fine_tune_epochs = epochs
        trans_learn_optimizer, fine_tune_optimizer = optimizers

        # Freeze layers in base model
        for layer in self.base_model.layers:
            layer.trainable = False

        self.model = self.stack_models(self.base_model, train_set.image_category_count, self.top_model_guide)
        self.train_model(self.model, train_set, trans_learn_optimizer, trans_learn_epochs, val_set=val_set)

        # Un-freeze desired number of layers
        for layer in self.model.layers[:top_layers_to_unfreeze]:
            layer.trainable = False
        for layer in self.model.layers[top_layers_to_unfreeze:]:
            layer.trainable = True

        self.train_model(self.model, train_set, fine_tune_optimizer, fine_tune_epochs, val_set=val_set)
