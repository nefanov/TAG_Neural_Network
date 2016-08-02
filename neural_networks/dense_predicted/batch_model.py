from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping
import numpy
import sys

#Fix random to ensure consistent results during testing
#seed = 4
#numpy.random.seed(seed)

#Get arguments from command line
#Arguments represnt model parameters
if len(sys.argv) != 4:
    print "Usage: python allFeatures_model.py [number_of_layers] [number_of_nodes] [activation_function]"
    print "Activation function options: "
    print "softmax, softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, linear"
    sys.exit(1)

number_of_layers = int(sys.argv[1])
number_of_nodes = int(sys.argv[2])
activation_function = sys.argv[3]

'''
io_info_train = open("io_dimensions_train_form.txt", "r")
io_info_test = open("io_dimensions_test_form.txt", "r")
one = io_info_train.readline().split()
two = io_info_test.readline().split()

input_dimensions = int(one[0])
output_dimensions = int(one[1])
i_dimensions = int(two[0])
o_dimensions = int(two[1])
'''
input_dimensions = 376
output_dimensions = 17
i_dimensions = 376
o_dimensions = 17

#Ensure test and train data have same form
if input_dimensions!= i_dimensions:
    sys.stderr.write("There is a mismatch in input dimensions\n")
    sys.exit(1)
if output_dimensions!= o_dimensions:
    sys.stderr.write("There is a mismatch in output dimensions\n")
    sys.exit(1)

#Get train data
print "Getting data ..."
X_train = numpy.load("X_train_example.npy")
Y_train = numpy.load("Y_train_example.npy")

#Create model
print "creating model ..."

if number_of_layers == 3:
    model = Sequential()
    model.add(Dense(number_of_nodes, input_dim = input_dimensions, init='uniform'))
    model.add(Activation(activation_function))
    model.add(Dense(number_of_nodes))
    model.add(Activation(activation_function))
    model.add(Dense(output_dimensions))
    model.add(Activation('softmax'))

if number_of_layers == 2:
    model = Sequential()
    model.add(Dense(number_of_nodes, input_dim = input_dimensions, init='uniform'))
    model.add(Activation(activation_function))
    model.add(Dropout(0.50))
    model.add(Dense(output_dimensions))
    model.add(Activation('softmax'))

#Compile model
model.compile(loss='binary_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit(X_train, Y_train, callbacks=[early_stopping], nb_epoch=50, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get test data
print "getting test data..."
X_test = numpy.load("X_dev_example.npy") 
Y_test = numpy.load("Y_dev_example.npy")


#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))