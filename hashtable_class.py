#!/usr/bin/env python3
# shebang for linux

"""
simple hashtable module

provides hash table class based on trivial hash function
tests it and provides examples in main

REFFERENCE: - https://en.wikipedia.org/wiki/Hash_function#Hash_function_algorithms
"""

# import std lib
# import 3rd party lib
# import usr lib

# global var

# start debugging
import pdb
#pdb.set_trace()
DEBUG = 0;

class hash():
    """
    simple hashtable class

    hashtable implementation using trivial hash function
    data is stored as a dictionary of key value pairs

    REFFERENCE: - https://en.wikipedia.org/wiki/Hash_function#Hash_function_algorithms
    """


    def __init__(self):
        """
        initialises new hash table as self.ls
        """
        size = 100;
        KV = {"key": "", "value": None};
        self.ls = [];

        #create 1D matrix
        for i in range(size):
            self.ls.append([KV.copy()]);


    def __str__(self):
        """
        prints hashtable
        """
        return str(self.ls);


    def add(self, item):
        """
        adds key value pair to hashtable

        INPUTS: - item in format {"key": 0, "value": 0};
        OUTPUTS: - index of new item
        """

        #convert item key to index using trivial hash function
        string = "";
        
        for i in item["key"]:
            string += str(ord(i));
        
        index = int(string) % len(self.ls);

        #add data
        if self.ls[index][0]["key"] == "": #if index unused, add item
            self.ls[index][0] = item;
        else:                           #if index used, add new row for item
            self.ls[index].append(item);

        return index;


    def example(self):
        """
        fills initialised hash table with random data

        INPUTS: - hashtable variable
                - item in format {"key": "string", "value": int};
        OUTPUTS: index of new item
        """

        import random
        import string

        #generate 100 keys of 5 characters simulating names
        keyls = [];
        for i in range(100):
            l1 = [];
            for i in range(5):
                l1.append(random.choice(string.ascii_letters));
            s1 = "".join(l1);
            keyls.append(s1);

        #use fixed keyls
        #keyls = ["steve","claire","mike","rob","emma","jackie","giles","jill","hugh","dan","lucy","fran","paul","jim","christine"];
        
        #add random data to table, equaling size of original 1D matrix
        for i in range(len(self.ls)):
            item = {"key": "new_name1", "value": 1};
            item["key"] = random.choice(keyls);
            item["value"] = random.randint(0,999);
            self.add(item);


    def retrieve(self, key):
        """
        retrieves key value pair from hashtable

        INPUTS: - key, string
        OUTPUTS:    - value, string
                    - empty value on failture, string 
        """

        #convert key to index using trivial hash function
        string = "";
        for i in key:
            string += str(ord(i));
        
        index = int(string) % len(self.ls);

        #search block
        i = 0;
        found = "";

        for i in range(len(self.ls[index])):
            found = self.ls[index][i]["key"];
            if found == key:
                value = self.ls[index][i]["value"];
                break;
            else:
                value = "";

        return value;


def main(argv):
    """
    tests simple hashtable library

    INPUTS: none
    OUTPUTS: return 0 on success
    """

    #test init
    test = hash();
    
    #test fill with data
    test.example();
    
    #test add more data
    item = {"key": "new_name1", "value": 1};
    test.add(item);

    item = {"key": "new_name2", "value": 2};
    test.add(item);
    
    item = {"key": "new_name3", "value": 3};
    test.add(item);
    
    item = {"key": "new_name4", "value": 4};
    test.add(item);
    
    #test retrieve data
    item_in = {"key": "new_name1", "value": 1};
    item_out = test.retrieve("new_name1");
    
    if item_out != item_in["value"]:
        raise UserWarning("hash not working");

    #check for collisions
    import numpy as np
    histogram = [];
    for i in range(len(test.ls)):
            histogram.append(len(test.ls[i]));

    print("%d collision\n" % (int(sum(histogram)) - len(test.ls)));
    
    import termgraph
    
    print(histogram);

    return 0;


# script autorun
if __name__ == "__main__":

    import sys
    
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
