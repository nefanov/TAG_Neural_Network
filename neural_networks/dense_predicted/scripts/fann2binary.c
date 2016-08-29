/******************************************************************
 * This function takes as input a fann file, the feature model for 
 * that fann file, a filename for saving the input data, a filename
 * for saving the output data and a file name for io info which is
 * used by load_fann_bin.py to load the binary file to a numpy array
 *
 * Forrest Davis
 * August 29, 2016
 * 
 *****************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* TODO:
 * Write now I just have a fann to binary function for a fann file
 * with one feature with the exact order s0 s1 s2 s3 b0 b1 b2 b3.
 * Need to write a general fann to binary for multiple features
 * and for a different order of stack and buffer.
 */

void transformFANN_Optimized(const char *fann_name, 
        const char *saved_input_filename, 
        const char *saved_output_filename,
        const char *io_info_filename);

int main(int argc, char **argv){
    if(argc!=6){
        fprintf(stderr, "Usage: ./fann2binary <fann_file> "
                "<feature_model> <saved_input_filename> " 
                "<saved_output_filename> <io_info_filename>\n");
        exit(1);
    } 
                 
    const char *fann_name = argv[1];
    const char *fm_name = argv[2];
    const char *saved_input_filename = argv[3];
    const char *saved_output_filename = argv[4];
    const char *io_info_filename = argv[5];

    const char comment = '#';
    //If this is the exact order of stack and buffer elements
    //used for the same feature then the transformFANN_Optimized 
    //function to create a binary file can be used
    char *s_b_order[] = {"s0","s1","s2",
        "s3","b0","b1","b2","b3"};
    char buffer[100];

    //Open feature model file 
    FILE *fm = fopen(fm_name, "r");
    if(fm == NULL){
        fprintf(stderr, "Unable to open %s file.\n", fm_name);
        exit(1);
    }

    int i = 0;
    int isOptimized = 1;
    //Read each line of the fm file
    while(fgets(buffer, sizeof(buffer), fm)!=NULL){
        //If first character is #, ignore
        if(buffer[0] != comment){
            //Get feature location information i.e s0
            char subarray[2];
            memcpy(subarray, buffer, 2);
            //If each of the optimized stack/buffer order 
            //is not in order in the fm file than the Optimized
            //function cannot be used
            if(strcmp(subarray, s_b_order[i++])!=0)
                isOptimized = 0;
        }
    }

    if(isOptimized)
        transformFANN_Optimized(fann_name, 
                saved_input_filename, saved_output_filename,
                io_info_filename);

    fclose(fm);
    return 0;
}

//This is the fastest way I could come up with to transform 
//the fann file into binary.
//It reads the one hot encodings from the fann file and if the 
//data are input it writes it to the saved_input file. If the data
//are output it writes it to the saved_output file. In the fann file
//format the first line is comprised of three numbers. The first
//is number of input/output pairs. The second is the dimensions of the 
//input. The third is the dimension of the output. This line is read first
//and saved to the io_info file for use by the python program that loads
//the binary file as a numpy array.
//Furthermore, I am using char for the data to decrease the numpy array
//size later on.
void transformFANN_Optimized(const char *fann_name, 
        const char *saved_input_filename, 
        const char *saved_output_filename,
        const char *io_info_filename){
    FILE *fann = fopen(fann_name, "r");

    //Open files
    if(fann == NULL){
        fprintf(stderr, "Unable to open %s file.\n", fann_name);
        exit(1);
    }
    FILE *saved_output = fopen(saved_output_filename, "wb");
    if(saved_output == NULL){
        fprintf(stderr, "Unable to open %s file.\n", saved_output_filename);
        exit(1);
    }
    FILE *saved_input = fopen(saved_input_filename, "wb");
    if(saved_input == NULL){
        fprintf(stderr, "Unable to open %s file.\n", saved_input_filename);
        exit(1);
    }
    FILE *io_info_file = fopen(io_info_filename, "w");
    if(io_info_file == NULL){
        fprintf(stderr, "Unable to open %s file.\n", io_info_filename);
        exit(1);
    }
    
    char buffer[8000];
    int isOutput = 0;
    int numNew = 0;
    int i;
    int j;

    printf("Transforming fann file to binary...\n");
    
    //Read first line and save to io info file
    fgets(buffer, sizeof(buffer), fann);
    fputs(buffer, io_info_file);

    //Read the rest of the lines
    //The format of the fan file is one blank line between 
    //input and output and two between the output and the new 
    //input/output pair. Thus if only one blank line is found the 
    //following one hot encoding is written to the saved output
    //file. Then the next one hot encodings are input so they are
    //written to the saved input file
    while(fgets(buffer, sizeof(buffer), fann)!=NULL){
        if(buffer[0] == 10){
            numNew++;
        }
        else{
            if(numNew == 1)
                isOutput = 1;
            if(isOutput){
                j = 0;
                //Get size of line. Due to format of fann files
                //I know each int is seperated by a space so the 
                //actually length of the one hot encoding is half
                int len = strlen(buffer);
                char value[len/2];
                for(i=0; i<len; i++){
                    char tmp;
                    //First append all data from line to array
                    //this is faster than writing each value to file
                    if((tmp=(buffer[i++]-48))== 0 || tmp == 1)
                        value[j++] = tmp;
                    
                }
                fwrite(value, sizeof(value), 1, saved_output);
                isOutput = 0;
            }
            else{
                j = 0;
                //Get size of line. Due to format of fann files
                //I know each int is seperated by a space so the 
                //actually length of the one hot encoding is half
                int len = strlen(buffer);
                char value[len/2];
                for(i=0; i<len; i++){
                    char tmp;
                    //First append all data from line to array
                    //this is faster than writing each value to file
                    if((tmp=(buffer[i++]-48))== 0 || tmp == 1)
                        value[j++] = tmp;
                    
                }
                fwrite(value, sizeof(value), 1, saved_input);
            }
            numNew = 0;
        }
    }

    //Close files
    fclose(fann);
    fclose(saved_output);
    fclose(saved_input);
    fclose(io_info_file);
}
