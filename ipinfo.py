#!/usr/bin/env python3
# shebang for linux

"""
analyses ipv4 address passed as command line argument and reports information to console

ipv4 only
references:     - https://en.wikipedia.org/wiki/IP_address
                - https://en.wikipedia.org/wiki/IPv4#Addressing
"""

# import std lib
import sys

# import 3rd party lib
# import usr lib

# global var

# start debugging
#import pdb
#pdb.set_trace()
DEBUG = 0;


def ipvalid(ipstring):
    """
    checks string for validity as IP address
    
    input: single string
    output: - list of intergers if valid
            - UserWarning if invalid

    >>> ipvalid("10.0.0.0");
    Analysing ip address
    ip address is valid
    [10, 0, 0, 0]
    """
    iplist = ipstring.split(".", 3);

    if len(iplist) != 4 or iplist[3].find(".") != -1:   #check for 4 sections separated by .
        raise UserWarning("INVALID ip: ip address must have 4 sections seperated by .");

    try:    #conver to int
        ipdigits = [int(iplist[0]), int(iplist[1]), int(iplist[2]), int(iplist[3])];
    except ValueError:
        raise UserWarning("INVALID ip: ip address must consist of decimal intergers seperated by .");

    for i in ipdigits:  #check number size
        if i < 0 or i > 255:
            raise UserWarning("INVALID ip: numbers in ip address cannot be < 0 or > 255");

    return(ipdigits);


def iptype(ipdigits):
    """
    checks list of numbers valid as an ip address against special use reserved ranges

    input:  - list of 4 intergers
    output: - user message string

    >>> iptype([10, 0, 0, 0]);
    Reserved private address - class a
    """
    
    #https://en.wikipedia.org/wiki/IPv4#Addressing
    if (
            ipdigits[0] == 0
        ):
        #https://tools.ietf.org/html/rfc6890
        message = "only valid as source address";
    elif (
            ipdigits[0] == 10
        ):
        #https://tools.ietf.org/html/rfc1918
        message = "reserved for local communication in a private network\nclass a";
    elif (
            ipdigits[0] == 100 and
            64 <= ipdigits[1] <= 127 and
            0 <= ipdigits[2] <= 255 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc6598
        message = "reserved for communications between a service provider and its subscribers when using a carrier-grade NAT";
    elif (
            ipdigits[0] == 127
        ):
        #https://tools.ietf.org/html/rfc6890
        message = "reserved for loopback addresses to the local host";
    elif (
            ipdigits[0] == 169 and
            ipdigits[1] == 254 and
            0 <= ipdigits[2] <= 255 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc3927
        message = "reserved for link-local addresses between two hosts on a single link when no is otherwise specified";
    elif (
            ipdigits[0] == 172 and
            16 <= ipdigits[1] <= 32 and
            0 <= ipdigits[2] <= 255 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc1918
        message = "reserved for local communication in a private network\nclass b";
    elif (
            ipdigits[0] == 192 and
            ipdigits[1] == 0 and
            ipdigits[2] == 0 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc5737
        message = "reserved for TEST-NET-1, documentation and examples";
    elif (
            ipdigits[0] == 192 and
            ipdigits[1] == 0 and
            ipdigits[2] == 2 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc6890
        message = "assigned to IANA reserved for IETF protocol assignments";
    elif (
            ipdigits[0] == 192 and
            ipdigits[1] == 88 and
            ipdigits[2] == 99 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc7526
        message = "reserved, formerly used for IPv6 to ipv4 relay";
    elif (
            ipdigits[0] == 192 and
            ipdigits[1] == 168 and
            0 <= ipdigits[2] <= 255 and
            0 <= ipdigits[3] <= 255
        ):
        #https://tools.ietf.org/html/rfc1918
        message = "reserved for local communication in a private network\nclass c";
    elif (
        ipdigits[0] == 192 and
        18 <= ipdigits[1] <= 16 and
        0 <= ipdigits[2] <= 255 and
        0 <= ipdigits[3] <= 255
    ):
        #https://tools.ietf.org/html/rfc2544
        message = "reserved for benchmark testing of inter-network communications between two separate subnets";
    elif (
        ipdigits[0] == 192 and
        ipdigits[1] == 51 and
        ipdigits[2] == 100 and
        0 <= ipdigits[3] <= 255
    ):
        #https://tools.ietf.org/html/rfc5737
        message = "reserved for TEST-NET-2, documentation and examples";
    elif (
        ipdigits[0] == 203 and
        ipdigits[1] == 0 and
        ipdigits[2] == 113 and
        0 <= ipdigits[3] <= 255
    ):
        #https://tools.ietf.org/html/rfc5737
        message = "reserved for TEST-NET-3, documentation and examples";
    elif (
        224 <= ipdigits[0] <= 239 and
        0 <= ipdigits[1] <= 255 and
        0 <= ipdigits[2] <= 255 and
        0 <= ipdigits[3] <= 255
    ):
        #https://tools.ietf.org/html/rfc5771
        message = "reserved forfor ip multicast\nformer class d";
    elif (
        240 <= ipdigits[0] <= 255 and
        0 <= ipdigits[1] <= 255 and
        0 <= ipdigits[2] <= 255 and
        0 <= ipdigits[3] <= 254
    ):
        #https://tools.ietf.org/html/rfc3232
        message = "reserved for future use\nformer class e";
    elif (
        ipdigits == (255, 255, 255, 255)
    ):
        #https://tools.ietf.org/html/rfc6890
        #https://tools.ietf.org/html/rfc919
        message = "reserved for the limited broadcast destination address";
    else:
        message = "not reserved for special use";

    return message;


def ipcalc(ipdigits, subnet):
    """
    calculates x, y, z from ip address and subnet mask

    inputs: - list of 4 intergers, ipaddress
            - list of 4 intergers, subnet
    outputs: - tuple containing ...

    >>> ipcalc((10, 0, 0, 0), (255, 255, 255, 0));
    """
    return;

def main(argv):
    """
    analyses ipv4 address passed as cmd argument and reports information on stdout

    inputs: - ipv4 address as argv, str
    outputs:    - string stating validity of ip address
                - string classifying ip address
    """

    #get ip & split into 4
    if len(argv) != 2:
        print("usage: ipinfo.py [ip address]");
        exit();
    else:
        ipstring = argv[1];
        print("\nip address analysis for %s" % ipstring);
        ipdigits = ipvalid(ipstring);
        print(iptype(ipdigits));
        ipcalc(ipdigits, (255, 255, 255, 0));
        print("");

        return;


# script autorun
if __name__ == "__main__":

    #run program
    try:
        main(sys.argv);
    except UserWarning as err:
        print("%s" % err, file=sys.stderr);
        exit(1);

    if DEBUG == 1:
        # unit test
        import doctest;
        doctest.testmod();
