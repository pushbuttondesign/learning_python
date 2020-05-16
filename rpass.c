/* rpass                                                */
/* Generates a random secure password of >=4 characters */
/* Inputs: int password length                          */
/* Outputs: pointer to char string                      */
/* TODO: use a better source of entropy                 */

//include & define
#include "rpass.h"

//typedef
typedef struct {int number; char* numberpos;
                int letter; char* letterpos;
                int capletter; char* capletterpos;
                int symbol; char* symbolpos;} checkpass_counter;
typedef checkpass_counter* lsp; //letter space position


//global variable definition
struct {
    char numbers[11];
    char letters[27];
    char capletters[27];
    char symbols[28];
} char_set = {
    .numbers = "0123456789",
    .letters = "abcdefghijklmnopqrstuvwxyz",
    .capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    .symbols = "@!$%^&*()_+=-{}\?.,<>/\\:;[]#"
};

//function declaration
long s_random(int);     //s_random generates a random number between 0 and max_number argument
lsp checkpass(char*);   //checks password for one item in each character set

//main function rpass
char* rpass(int len) {
    static char *pass;
    pass = (char*)malloc(sizeof(char) * len);
    long r;
    lsp check_score;

    if (len < 4) {
        printf("ERROR: password length must be >3\n");
        exit(EXIT_FAILURE);
    }

    srand((unsigned)time(NULL));

    printf("> Generating password...\n");
    for (int i = 0; i < len; i++) {                //for length of password requested
        r = s_random(3);                           //generate random for number, letter or symbol
        switch (r) {
            case 0:
                r = s_random(10);                  //generate random within character set
                pass[i] = char_set.numbers[r];     //read item and put into password array
                break;
            case 1:
                r = s_random(26);
                pass[i] = char_set.letters[r];
                break;
            case 2:
                r = s_random(26);
                pass[i] = char_set.capletters[r];
                break;
            case 3:
                r = s_random(27);
                pass[i] = char_set.symbols[r];
                break;
            default:
                printf("ERROR: Random number generator failed\n");
                exit(EXIT_FAILURE);
                break;
        }
    }
    check_score = checkpass(pass);        //check *pass has at least one character from each set
    if (check_score->number == 0) {
        r = s_random(10);
        for (int i = 0; i < len; ++i) {                     //find first non-saved position of pass
            if (pass + i != check_score->numberpos && pass + i != check_score->letterpos && pass + i != check_score->capletterpos && pass + i != check_score->symbolpos) {
                *(pass + i) = char_set.numbers[r];          //insert number to position
                i = len;
            }
        }
    }
    if (check_score->letter == 0) {
        r = s_random(26);
        for (int i = 0; i < len; ++i) {
            if (pass + i != check_score->numberpos && pass + i != check_score->letterpos && pass + i != check_score->capletterpos && pass + i != check_score->symbolpos) {
                *(pass + i) = char_set.letters[r];
                i = len;
            }
        }
    }
    if (check_score->capletter == 0) {
        r = s_random(26);
        for (int i = 0; i < len; ++i) {
            if (pass + i != check_score->numberpos && pass + i != check_score->letterpos && pass + i != check_score->capletterpos && pass + i != check_score->symbolpos) {
                *(pass + i) = char_set.capletters[r];
                i = len;
            }
        }
    }
    if (check_score->symbol == 0) {
        r = s_random(27);
        for (int i = 0; i < len; ++i) {
            if (pass + i != check_score->numberpos && pass + i != check_score->letterpos && pass + i != check_score->capletterpos && pass + i != check_score->symbolpos) {
                *(pass + i) = char_set.symbols[r];
                i = len;
            }
        }
    }
    return pass;
}

//functions
long s_random(int max_number){
    long r;

    r = rand() % max_number;
    return r;
}

lsp checkpass(char *pass){
    char *str_result;
    static checkpass_counter letterspace = {0,0,0,0,0,0,0,0};
    lsp check_score = &letterspace;
    char test;

    //numbers
    for (int i = 0; i < 10; ++i) {
        test = char_set.numbers[i];
        str_result = strchr(pass, test);        //compare password string to character in char_set array
        if (str_result != NULL) {               //at first insidence of character from char_set array
            letterspace.number = 1;             //set confirmation bit
            letterspace.numberpos = str_result; //save location
            i = 10;                             //exit for loop immediatly
        }
    }
    //letters
    for (int i = 0; i < 26; ++i) {
        test = char_set.letters[i];
        str_result = strchr(pass, test);
        if (str_result != NULL) {
            letterspace.letter = 1;
            letterspace.letterpos = str_result;
            i = 26;
        }
    }
    //capletters
    for (int i = 0; i < 26; ++i) {
        test = char_set.capletters[i];
        str_result = strchr(pass, test);
        if (str_result != NULL) {
            letterspace.capletter = 1;
            letterspace.capletterpos = str_result;
            i = 26;
        }
    }
    //symbol
    for (int i = 0; i < 27; ++i) {
        test = char_set.symbols[i];
        str_result = strchr(pass, test);
        if (str_result != NULL) {
            letterspace.symbol = 1;
            letterspace.symbolpos = str_result;
            i = 27;
        }
    }
    return check_score;
}
