import numpy
import sys

def transform_fann(input_train_file, X_train_file, Y_train_file):
    train_fann = open(input_train_file, 'r')

    info = train_fann.readline().split()
    train_output_dimensions = int(info[2])
    #Extract train
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    sys.stderr.write("Getting lines...\n")
    for line in train_fann:
        line = line.split()
        line = map(int, line)
        if len(line) != train_output_dimensions and len(line) != 0:
            x_tmp += line
        elif len(line) == train_output_dimensions:
            y.append(line)
            x.append(x_tmp)
            x_tmp = []
            
    X_train = numpy.array(x, dtype=numpy.uint8)
    Y_train = numpy.array(y, dtype=numpy.uint8)

    #Save output
    sys.stderr.write("Saving information...\n")
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    #Close files
    train_fann.close()
    return info[1], info[2]

if __name__ == "__main__":
    sys.stderr.write("starting A train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/A_train.fann"
    X_train_file = "./data/X_train_A.npy"
    Y_train_file = "./data/Y_train_A.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "A train", input_dim, output_dim
    sys.stderr.write("starting A test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/A_dev.fann"
    X_train_file = "./data/X_test_A.npy"
    Y_train_file = "./data/Y_test_A.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "A test", input_dim, output_dim

    sys.stderr.write("starting B train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/B_train.fann"
    X_train_file = "./data/X_train_B.npy"
    Y_train_file = "./data/Y_train_B.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "B train", input_dim, output_dim
    sys.stderr.write("starting B test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/B_dev.fann"
    X_train_file = "./data/X_test_B.npy"
    Y_train_file = "./data/Y_test_B.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "B test", input_dim, output_dim

    sys.stderr.write("starting C train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/C_train.fann"
    X_train_file = "./data/X_train_C.npy"
    Y_train_file = "./data/Y_train_C.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "C train", input_dim, output_dim
    sys.stderr.write("starting C test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/C_dev.fann"
    X_train_file = "./data/X_test_C.npy"
    Y_train_file = "./data/Y_test_C.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "C test", input_dim, output_dim

    sys.stderr.write("starting D train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/D_train.fann"
    X_train_file = "./data/X_train_D.npy"
    Y_train_file = "./data/Y_train_D.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "D train", input_dim, output_dim
    sys.stderr.write("starting D test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/D_dev.fann"
    X_train_file = "./data/X_test_D.npy"
    Y_train_file = "./data/Y_test_D.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "D test", input_dim, output_dim

    sys.stderr.write("starting E train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/E_train.fann"
    X_train_file = "./data/X_train_E.npy"
    Y_train_file = "./data/Y_train_E.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "E train", input_dim, output_dim
    sys.stderr.write("starting E test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/E_dev.fann"
    X_train_file = "./data/X_test_E.npy"
    Y_train_file = "./data/Y_test_E.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "E test", input_dim, output_dim

    '''
    sys.stderr.write("starting F train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/F_train.fann"
    X_train_file = "X_train_F.npy"
    Y_train_file = "Y_train_F.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "F train", input_dim, output_dim
    sys.stderr.write("starting F test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/F_dev.fann"
    X_train_file = "X_test_F.npy"
    Y_train_file = "Y_test_F.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "F test", input_dim, output_dim
    '''