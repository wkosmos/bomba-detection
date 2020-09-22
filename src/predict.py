import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as K




if __name__ == __main__:
    model = tf.keras.models.load_model('data/models')

    test_dir = 'data/audio/600_chunks_split/test'

    img_width, img_height = 640, 480

    test_datagen = ImageDataGenerator()
    test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=16,
    class_mode='binary')

    loss, acc = model.evaluate()

    predictions = model.predict_generator(test_batches, steps=1, verbose=0)

    test_imgs, test_labels = next(test_batches)
    test_labels = test_labels[:,0]

