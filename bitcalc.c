//
//  bitcalc.c
//  bitcaculator
//
//  Caculates the maximum number of binary bits a decimal number with a given number of digets will require
//
//  INPUTS: int number of digets in decimal number
//  OUTPUTS: int maximum number of binary bits

#include "bitcalc.h"

int bitcalc(int digets) {
    int maxbits;
    
    maxbits = ceil(digets * (log(10) / log(2)));
    //printf("decimal number with %d digets requires a maximum of %d bits\n", d, maxbits);
    
    return maxbits;
}