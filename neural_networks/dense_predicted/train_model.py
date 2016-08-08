from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys

io_info = open("./data_1000/io_dimensions_1000.txt", "r")
A_train_input_dim = 0
train_output_dim = 0
B_train_input_dim = 0 
C_train_input_dim = 0
D_train_input_dim = 0
E_train_input_dim = 0
F_train_input_dim = 0
G_train_input_dim = 0
H_train_input_dim = 0
I_train_input_dim = 0
J_train_input_dim = 0
K_train_input_dim = 0
L_train_input_dim = 0
M_train_input_dim = 0
N_train_input_dim = 0
O_train_input_dim = 0
P_train_input_dim = 0
Q_train_input_dim = 0
R_train_input_dim = 0
S_train_input_dim = 0
T_train_input_dim = 0
U_train_input_dim = 0 
pos_train_input_dim = 0
form_train_input_dim = 0

for line in io_info:
    line = line.split()
    if line[0] == "A":
        if line[1] == "train":
	    A_train_input_dim = int(line[2])
	    train_output_dim = int(line[3])
    if line[0] == "B":
        if line[1] == "train":
	    B_train_input_dim = int(line[2])
    if line[0] == "C":
        if line[1] == "train":
	    C_train_input_dim = int(line[2])
    if line[0] == "D":
        if line[1] == "train":
	    D_train_input_dim = int(line[2])
    if line[0] == "E":
        if line[1] == "train":
	    E_train_input_dim = int(line[2])
    if line[0] == "F":
        if line[1] == "train":
	    F_train_input_dim = int(line[2])
    if line[0] == "G":
        if line[1] == "train":
	    G_train_input_dim = int(line[2])
    if line[0] == "H":
        if line[1] == "train":
	    H_train_input_dim = int(line[2])
    if line[0] == "I":
        if line[1] == "train":
	    I_train_input_dim = int(line[2])
    if line[0] == "J":
        if line[1] == "train":
	    J_train_input_dim = int(line[2])
    if line[0] == "K":
        if line[1] == "train":
	    K_train_input_dim = int(line[2])
    if line[0] == "L":
        if line[1] == "train":
	    L_train_input_dim = int(line[2])
    if line[0] == "M":
        if line[1] == "train":
	    M_train_input_dim = int(line[2])
    if line[0] == "N":
        if line[1] == "train":
	    N_train_input_dim = int(line[2])
    if line[0] == "O":
        if line[1] == "train":
	    O_train_input_dim = int(line[2])
    if line[0] == "P":
        if line[1] == "train":
	    P_train_input_dim = int(line[2])
    if line[0] == "Q":
        if line[1] == "train":
	    Q_train_input_dim = int(line[2])
    if line[0] == "R":
        if line[1] == "train":
	    R_train_input_dim = int(line[2])
    if line[0] == "S":
        if line[1] == "train":
	    S_train_input_dim = int(line[2])
    if line[0] == "T":
        if line[1] == "train":
	    T_train_input_dim = int(line[2])
    if line[0] == "U":
        if line[1] == "train":
	    U_train_input_dim = int(line[2])
    if line[0] == "pos":
        if line[1] == "train":
	    pos_train_input_dim = int(line[2])
    if line[0] == "form":
        if line[1] == "train":
	    form_train_input_dim = int(line[2])

#Get train data
print "Getting A data ..."
X_train_A = numpy.load("./data_1000/X_train_A_1000.npy")
Y_train = numpy.load("./data_1000/Y_train_A_1000.npy")

print "Getting B data ..."
X_train_B = numpy.load("./data_1000/X_train_B_1000.npy")

print "Getting C data ..."
X_train_C = numpy.load("./data_1000/X_train_C_1000.npy")

print "Getting D data ..."
X_train_D = numpy.load("./data_1000/X_train_D_1000.npy")

print "Getting E data ..."
X_train_E = numpy.load("./data_1000/X_train_E_1000.npy")

'''
print "Getting F data ..."
X_train_F = numpy.load("./data_1000/X_train_F_1000.npy")

print "Getting G data ..."
X_train_G = numpy.load("./data_1000/X_train_G_1000.npy")
'''

print "Getting H data ..."
X_train_H = numpy.load("./data_1000/X_train_H_1000.npy")

print "Getting I data ..."
X_train_I = numpy.load("./data_1000/X_train_I_1000.npy")

print "Getting J data ..."
X_train_J = numpy.load("./data_1000/X_train_J_1000.npy")

print "Getting K data ..."
X_train_K = numpy.load("./data_1000/X_train_K_1000.npy")

print "Getting L data ..."
X_train_L = numpy.load("./data_1000/X_train_L_1000.npy")

print "Getting M data ..."
X_train_M = numpy.load("./data_1000/X_train_M_1000.npy")

print "Getting N data ..."
X_train_N = numpy.load("./data_1000/X_train_N_1000.npy")

print "Getting O data ..."
X_train_O = numpy.load("./data_1000/X_train_O_1000.npy")

print "Getting P data ..."
X_train_P = numpy.load("./data_1000/X_train_P_1000.npy")

print "Getting Q data ..."
X_train_Q = numpy.load("./data_1000/X_train_Q_1000.npy")

print "Getting R data ..."
X_train_R = numpy.load("./data_1000/X_train_R_1000.npy")

print "Getting S data ..."
X_train_S = numpy.load("./data_1000/X_train_S_1000.npy")

print "Getting T data ..."
X_train_T = numpy.load("./data_1000/X_train_T_1000.npy")

print "Getting U data ..."
X_train_U = numpy.load("./data_1000/X_train_U_1000.npy")

print "Getting pos data ..."
X_train_pos = numpy.load("./data_1000/X_train_pos_1000.npy")

print "Getting form data ..."
X_train_form = numpy.load("./data_1000/X_train_form_1000.npy")

#Create model
print "creating model ..."
model_A = Sequential()
model_B = Sequential()
model_C = Sequential()
model_D = Sequential()
model_E = Sequential()
#model_F = Sequential()
#model_G = Sequential() 
model_H = Sequential()
model_I = Sequential()
model_J = Sequential()
model_K = Sequential()
model_L = Sequential()
model_M = Sequential()
model_N = Sequential()
model_O = Sequential()
model_P = Sequential()
model_Q = Sequential()
model_R = Sequential()
model_S = Sequential()
model_T = Sequential()
model_U = Sequential()
model_pos = Sequential()
model_form = Sequential()
model = Sequential() 

model_A.add(Dense(50, input_dim = A_train_input_dim, init='uniform'))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))
model_A.add(Dense(50))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))

model_B.add(Dense(50, input_dim = B_train_input_dim, init='uniform'))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))
model_B.add(Dense(50))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))

model_C.add(Dense(50, input_dim = C_train_input_dim, init='uniform'))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))
model_C.add(Dense(50))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))

model_D.add(Dense(50, input_dim = D_train_input_dim, init='uniform'))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))
model_D.add(Dense(50))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))

model_E.add(Dense(50, input_dim = E_train_input_dim, init='uniform'))
model_E.add(Activation('relu'))
model_E.add(Dropout(0.50))
model_E.add(Dense(50))
model_E.add(Activation('relu'))
model_E.add(Dropout(0.50))

'''
model_F.add(Dense(50, input_dim = F_train_input_dim, init='uniform'))
model_F.add(Activation('relu'))
model_F.add(Dropout(0.50))
model_F.add(Dense(50))
model_F.add(Activation('relu'))
model_F.add(Dropout(0.50))

model_G.add(Dense(50, input_dim = G_train_input_dim, init='uniform'))
model_G.add(Activation('relu'))
model_G.add(Dropout(0.50))
model_G.add(Dense(50))
model_G.add(Activation('relu'))
model_G.add(Dropout(0.50))

'''
model_H.add(Dense(50, input_dim = H_train_input_dim, init='uniform'))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))
model_H.add(Dense(50))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))

model_I.add(Dense(50, input_dim = I_train_input_dim, init='uniform'))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50))
model_I.add(Dense(50))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50)) 

model_J.add(Dense(50, input_dim = J_train_input_dim, init='uniform'))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))
model_J.add(Dense(50))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))

model_K.add(Dense(50, input_dim = K_train_input_dim, init='uniform'))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))
model_K.add(Dense(50))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))

model_L.add(Dense(50, input_dim = L_train_input_dim, init='uniform'))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))
model_L.add(Dense(50))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))

model_M.add(Dense(50, input_dim = M_train_input_dim, init='uniform'))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))
model_M.add(Dense(50))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))

model_N.add(Dense(50, input_dim = N_train_input_dim, init='uniform'))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))
model_N.add(Dense(50))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))

model_O.add(Dense(50, input_dim = O_train_input_dim, init='uniform'))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))
model_O.add(Dense(50))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))

model_P.add(Dense(50, input_dim = P_train_input_dim, init='uniform'))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))
model_P.add(Dense(50))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))

model_Q.add(Dense(50, input_dim = Q_train_input_dim, init='uniform'))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))
model_Q.add(Dense(50))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))

model_R.add(Dense(50, input_dim = R_train_input_dim, init='uniform'))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))
model_R.add(Dense(50))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))

model_S.add(Dense(50, input_dim = S_train_input_dim, init='uniform'))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))
model_S.add(Dense(50))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))

model_T.add(Dense(50, input_dim = T_train_input_dim, init='uniform'))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))
model_T.add(Dense(50))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))

model_U.add(Dense(50, input_dim = U_train_input_dim, init='uniform'))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))
model_U.add(Dense(50))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))

model_pos.add(Dense(50, input_dim = pos_train_input_dim, init='uniform'))
model_pos.add(Activation('relu'))
model_pos.add(Dropout(0.50))
model_pos.add(Dense(50))
model_pos.add(Activation('relu'))
model_pos.add(Dropout(0.50))

model_form.add(Dense(50, input_dim = form_train_input_dim, init='uniform'))
model_form.add(Activation('relu'))
model_form.add(Dropout(0.50))
model_form.add(Dense(50))
model_form.add(Activation('relu'))
model_form.add(Dropout(0.50))

model.add(Merge([model_A, model_B, model_C, model_D, model_E, model_H, model_I, model_J, model_K, model_L, 
model_M, model_N, model_O, model_P, model_Q, model_R, model_S, model_T, model_U, model_pos, model_form], mode ='concat'))
model.add(Dense(train_output_dim))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit([X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_H, X_train_I, X_train_J, 
X_train_K, X_train_L, X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R, X_train_S, X_train_T, X_train_U, 
X_train_pos, X_train_form], 
Y_train, callbacks=[early_stopping], nb_epoch=50, verbose=1, batch_size=1000, 
         validation_split=0.1)

print "saving model..."
model_json = model.to_json()
with open("example_trained_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("example_trained_model_weights.h5")