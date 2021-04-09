
"""
Created on Mon Nov 10 16:39:45 2018

@author: Taranjit Singh
"""
import numpy
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten,Dropout
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

# initialising the Convolution nural network
classifier = Sequential()

# Step 1 - convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(p=0.2))
# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(p=0.2))

# Step 3 - Flattening
classifier.add(Flatten())
classifier.add(Dropout(p=0.2))

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dropout(p=0.2))


classifier.add(Dense(units = 2, activation = 'softmax')) #units = no of output classes

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images



train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255) #rescaling the pixels of the images of the test set

training_set = train_datagen.flow_from_directory('E:/New folder/ccet/7th sem new/sanjay/nn proj/dataset_updated/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32 ,
                                                 class_mode = 'categorical')


test_set = test_datagen.flow_from_directory('E:/New folder/ccet/7th sem new/sanjay/nn proj/dataset_updated/validation_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')


classifier.fit_generator(training_set,
                         steps_per_epoch=150,
                         epochs = 15,
                         validation_data = test_set,
                         validation_steps=20
                         
                         )

"""
test_steps_per_epoch = numpy.math.ceil(test_set.samples / test_set.batch_size)

predictions = classifier.predict_generator(test_set, steps=test_steps_per_epoch)
# Get most likely class
predicted_classes = numpy.argmax(predictions, axis=1)

true_classes = test_set.classes
class_labels = list(test_set.class_indices.keys())  



cm = confusion_matrix(y_target=true_classes, y_predicted=predicted_classes, binary=False)
print(cm)
"""



