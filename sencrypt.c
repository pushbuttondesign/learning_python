/* sencript                                                     */
/* An inplementation of one time pad encryption for ASCII input */
/* Inputs:                                                      */
/*      decrypt mode and encripted file and password            */
/*      or encrypt mode and un-encripted file or help command   */
/* Outputs: decripted file or encripted file and password       */
/* TODO:                                                        */                                   
/*  1. speed up random number generator, implement sodium       */
/*  2. read as binary not ASCII                                 */

//include & define
#include "rpass.h"

//global variables
char *version = "v0.1.0";

//typedef
typedef struct {
    char *programname;
    char *operation;
    char *filename;
    char *passwordfile;
} inarguments;

//function declaration
int checkarguments(int, inarguments*);
int count_in_char(FILE*);

//main
int main(int argc, char *argv[]) {
    inarguments arguments = {
        .programname = argv[0],
        .operation = argv[1],
        .filename = argv[2],
        .passwordfile = argv[3],
        }, *arg = &arguments;
    
    checkarguments(argc, arg);
    printf("\nsencript %s\n***************\n", version);
    
    //encrypt operation
    if (*arg->operation == 'E' || *arg->operation == 'e') {
        printf("Encrypt mode\n");
        //open decrypted file input and create new password and encrypted file outputs
        char *out_filename = (char*)malloc(sizeof(char) * (strlen(arg->filename) + 11));
        strcpy(out_filename, arg->filename);              //create out_filename from in_filename
        strncat(out_filename, "_encrypted", 10);
        FILE *fp_out = fopen(out_filename, "w");          //create new file for encryption output
        char *out_filename2 = (char*)malloc(sizeof(char) * (strlen(arg->filename) + 10));
        strcpy(out_filename2, arg->filename);
        strncat(out_filename2, "_password", 9);
        FILE *fp_pass = fopen(out_filename2, "w");        //create new file for password
        FILE *fp_in = fopen(arg->filename, "r");          //open input file
        if(fp_in == NULL || fp_out == NULL || fp_pass == NULL){
            fprintf(stderr, "ERROR: Cannot open file\n");
            exit(EXIT_FAILURE);
        }
        
        //count input file characters
        int cc = count_in_char(fp_in);
        fseek(fp_in, 0, SEEK_SET);
        
        //generate one time pad random secure password
        char *pass;
        pass = rpass(cc);
        
        //convert password to numbers
        int *pass_as_number = (int*)malloc(sizeof(int) * cc), i = 0;
        while (i < cc) {
            pass_as_number[i] = pass[i];
            ++i;
        }

        //shift characters by one time pad and save out
        int in_char;
        char e_char;
        i = 0;
        printf("> Encrypting...\n");
        while (i < cc) {
            in_char = fgetc(fp_in);
            e_char = in_char + pass_as_number[i];
            fputc(e_char, fp_out);
            i++;
        }
        printf("> Encrypted file saved\n");
        fprintf(fp_pass, "SENcript %s\nPassword for file: %s\n**********\n", version, out_filename);
        fprintf(fp_pass, "%s", pass);
        printf("> Password file saved\n");
        
        //free memory & close files
        free(out_filename);
        free(out_filename2);
        free(pass_as_number);
        fclose(fp_out);
        fclose(fp_in);
        fclose(fp_pass);
    }
    
    //decrypt operation
    if (*arg->operation == 'D' || *arg->operation == 'd') {
        printf("Decrypt mode\n");
        //open encripted file and password file inputs and create new decrypted file output
        FILE *fp_in = fopen(arg->filename, "r");
        FILE *fp_pass = fopen(arg->passwordfile, "r");
        char *out_filename = (char*)malloc(sizeof(char) * (strlen(arg->filename) + 11));
        strcpy(out_filename, arg->filename);
        strncat(out_filename, "_decrypted", 10);
        FILE *fp_out = fopen(out_filename, "w");
        if(fp_in == NULL || fp_out == NULL || fp_pass == NULL){
            fprintf(stderr, "ERROR: Cannot open file\n");
            exit(EXIT_FAILURE);
        }

        //count input file characters
        int cc = count_in_char(fp_in);
        fseek(fp_in, 0, SEEK_SET);
        
        //convert password to numbers
        char a;
        int i = 0;
        while (i != 3) {
            a = fgetc(fp_pass);
            if (a == '\n') {
                i++;
            }
        }
        int *pass_as_number = (int*)malloc(sizeof(int) * cc);
        i = 0;
        while (i < cc) {
            pass_as_number[i] = fgetc(fp_pass);
            ++i;
        }
        
        //shift characters by one time pad and save out
        int in_char;
        char d_char;
        i = 0;
        printf("> Decrypting...\n");
        while (i < cc) {
            in_char = fgetc(fp_in);
            d_char = in_char - pass_as_number[i]; //?
            fputc(d_char, fp_out);
            i++;
        }
        printf("> Decrypted file saved\n");
        
        //free memory & close files
        free(out_filename);
        free(pass_as_number);
        fclose(fp_out);
        fclose(fp_in);
        fclose(fp_pass);
    }
    printf("\n");
    return 0;
}

//functions
int checkarguments(int argc, inarguments *arg){
    if (argc <= 1){
        printf("ERROR: Arguments required\nRun with 'help' to see avalible arguments\n");
        exit(EXIT_FAILURE);
    } else if (strcmp(arg->operation, "help") == 0) {
        printf("\nSENcript %s Help Menu\n*************************\n", version);
        printf("Argument format for Encrypt mode is: e input_filepath\nArgument format for Decrypt mode is: d input_filepath input_password_filepath\n\n");
        exit(EXIT_SUCCESS);
    } else if (*arg->operation != 'E' && *arg->operation != 'e' && *arg->operation != 'D' && *arg->operation != 'd') {
        printf("ERROR: First argument must be either 'E' for encrypt mode, 'D' for decrypt mode or 'help' to see avalible arguments and format\n");
        exit(EXIT_FAILURE);
    } else if ((*arg->operation == 'e' && argc > 3) || (*arg->operation == 'E' && argc > 3)) {
        printf("ERROR: Only two arguments expected.\nRun with 'help' to see avalible arguments\n");
        exit(EXIT_FAILURE);
    } else if ((*arg->operation == 'd' && argc > 4) || (*arg->operation == 'D' && argc > 4)) {
        printf("ERROR: Only three arguments expected.\nRun with 'help' to see avalible arguments\n");
        exit(EXIT_FAILURE);
    } else if ((*arg->operation == 'e' && argc < 3) || (*arg->operation == 'E' && argc < 3)) {
        printf("ERROR: Two arguments expected in encrypt mode.\nRun with 'help' to see avalible arguments\n");
        exit(EXIT_FAILURE);
    } else if ((*arg->operation == 'd' && argc < 4) || (*arg->operation == 'D' && argc < 4)) {
        printf("ERROR: Three arguments expected in decrypt mode.\nRun with 'help' to see avalible arguments\n");
        exit(EXIT_FAILURE);
    }
    return 0;
}

int count_in_char(FILE *fp_in){
    int cc = 0;
    char c = '1';
    while (c != EOF) {
        c = fgetc(fp_in);
        (cc)++;
    }
    return cc-1;
}
