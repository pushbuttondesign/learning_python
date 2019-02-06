#!/usr/bin/env python3
# shebang for linux

"""
simple hashtable

hashtable implementation using trivial hash function
data is stored as a dictionary of key value pairs

REFFERENCE: - https://en.wikipedia.org/wiki/Hash_function#Hash_function_algorithms
"""

# import std lib
import sys
import random

# import 3rd party lib
# import usr lib

# global var

# start debugging
#import pdb
#pdb.set_trace()
DEBUG = 0;


def hash_init(size):
    """
    initialises new hash table

    INPUTS: size of 1D hash table, int
            size should be greater than length of data * 2 in order to reduce conflicts
    OUTPUTS: hash table

    EXAMPLES:
    >>> hash_init();
    """

    #initialise
    KV = {"key": "", "value": None};
    hash = [];

    #create 1D matrix
    for i in range(size):
        hash.append([KV]);

    return hash;


def hash_example(hash):
    """
    fills initialised hash table with random data

    INPUTS: - hashtable variable
            - item in format {"key": "string", "value": int};
    OUTPUTS: index of new item

    EXAMPLES:
    >>> hash_example(hash, 1, 1);
    """

    for i in range(len(hash)):
        for ii in range(len(hash[0])):
            hash[i][ii]["key"] = "test_name";
            hash[i][ii]["value"] = random.random();

    return hash;


def hash_add(hash, item):
    """
    adds key value pair to hashtable

    INPUTS: - hashtable variable
            - item in format {"key": 0, "value": 0};
    OUTPUTS: - index of new item

    EXAMPLES:
    >>> hash_add(hash, item);
    """

    #convert item key to index using trivial hash function
    string = "";
    for i in item["key"]:
        string += str(ord(i));
    index = int(string) % len(hash);

    #add data
    if hash[index][0]["key"] == "": #if index unused, add item
        hash[index][0] = item;
    else:                           #if index used, add new row for item
        hash[index].append(item);
        

    return index;


def hash_retrieve(hash, key):
    """
    retrieves key value pair from hashtable

    INPUTS: - key, string
    OUTPUTS: - value, string

    EXAMPLES:
    >>> hash_add(hash, item);
    """
    
    #convert key to index using trivial hash function
    string = "";
    for i in key:
        string += str(ord(i));
    index = int(string) % len(hash);
    
    #search block
    
    i = 0;
    found = "";
    
    while found != key:
        found = hash[index][i]["key"];
        i += 1;
        
    value = hash[index][i-1]["value"];
    
    return value;


def main(argv):
    """
    tests simple hashtable library

    INPUTS: none
    OUTPUTS: return 0 on success

    EXAMPLES:
    >>> main();
    0
    """

    hash = hash_init(100);
    hash = hash_example(hash);

    item = {"key": "new_name", "value": 7};
    index = hash_add(hash, item);

    item_out = hash_retrieve(hash, "new_name");

    #check for errors
    if item["value"] != item_out:
        raise UserWarning("hash not working");

    return 0;


# script autorun
if __name__ == "__main__":

    #run program
    try:
        main(sys.argv);
    except UserWarning as err:
        print("%s" % (err), file=sys.stderr);
        exit(1);

    if DEBUG == 1:
        # unit test
        import doctest;
        doctest.testmod();
