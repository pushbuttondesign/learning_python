/* rpass                                                */
/* Generates a random secure password of >=4 characters */
/* Inputs: int password length                          */
/* Outputs: pointer to char string                      */

#ifndef rpass_h
    #define rpass_h

    //include & define
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    #include <unistd.h>
    #include <string.h>

    //function decliration
    char* rpass(int);

#endif
