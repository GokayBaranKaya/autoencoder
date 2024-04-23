#importing libraries
import tensorflow as tf
import os
import pathlib

#defining a function, since the process needs to be done twice(for training and validation set)
def preprocess_and_save_image(input_file_path, output_file_path):
    #Preprocessing the image
    image = tf.io.read_file(input_file_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [160, 160])
    image = tf.cast(image, tf.uint8)
    
    #Saving the preprocessed images
    tf.io.write_file(output_file_path, tf.image.encode_jpeg(image))

def process_directory(input_dir_path, output_dir_path):
    input_dir_path = pathlib.Path(input_dir_path)
    output_dir_path = pathlib.Path(output_dir_path)

    #Iterating through each directories including sub directories
    for input_file_path in list(input_dir_path.glob('*/*')):
        relative_path = input_file_path.relative_to(input_dir_path)
        output_file_path = output_dir_path / relative_path
        
        #Creating the directory, depending on its existance
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        #Preprocessing and saving the images
        preprocess_and_save_image(str(input_file_path), str(output_file_path))

#Unlike unprocessed images, newly processed images won't be in the subdirectories
input_train_dir = 'C:/Users/GOKAY/Desktop/imagenette2/imagenette2-160/train'
output_train_dir = 'C:/Users/GOKAY/Desktop/imagenette3/preprocessed/train'
input_val_dir = 'C:/Users/GOKAY/Desktop/imagenette2/imagenette2-160/val'
output_val_dir = 'C:/Users/GOKAY/Desktop/imagenette3/preprocessed/val'

#Processing each dataset, (test set splitted manually later on)
process_directory(input_train_dir, output_train_dir)
process_directory(input_val_dir, output_val_dir)
