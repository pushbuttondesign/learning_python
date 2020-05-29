#!/usr/local/bin/python3
# shebang for mac osx

#!/usr/bin/env python3
# shebang for linux

"""
one time pad encryption and decryption
https://en.wikipedia.org/wiki/One-time_pad
secrets module is used for generating cryptographically strong random numbers
files opened in binary format

Inputs:
    decrypt mode and encripted file and password
    or encrypt mode and un-encripted file
    or help command

Outputs:
    decripted file
    or encripted file and password
"""

# import std lib
import secrets
import sys
import string

def main(argv):
    #check arguments
    if argv[1] == 'help' or argv[1] == 'Help':
        print("Usage: otp_encryption.py [mode] [file] [password]");
        exit(0);
    if len(argv) != 4:
        raise UserWarning("Usage: otp_encryption.py [mode] [file] [password]");

    #select mode
    try:
        if argv[1] == '0':
            encrypt(argv);
        elif argv[1] == '1':
            decrypt(argv);
        else:
            raise UserWarning("Usage: otp.py [mode] [file] [password]");
    except FileNotFoundError as err:
        raise UserWarning("%s" % err);

    return;

def encrypt(argv):
    #open file
    with open(argv[2],'rb') as fp:
        bcontent = fp.read();

    with open('before.txt', 'w') as a:
        a.write(str([x for x in bcontent]));

    #create password
    password = secrets.randbits(len(bcontent) * 8); # * 8 converts bytes to bits
    bpass = bytearray();
    for d in [int(d) for d in str(password)]:
        bpass.append(d);

    #get filename
    for i in reversed(range(len(argv[2]))):
        if argv[2][i] == '.':
            break;

    #save password
    with open(argv[2][:i] + "_otp_password" + argv[2][i:], 'wb') as pp:
        pp.write(bpass);

    #encrypt file
    with open(argv[2][:i] + "_otp_encrypted" + argv[2][i:], 'wb') as ep:
        bencrypt = bytearray();
        for i, d in enumerate(bcontent):
            #wrap at 255
            if d + bpass[i] > 255:
                wrap = d + bpass[i] - 255 - 1;
                inc = wrap;
            else:
                inc = d + bpass[i];
            bencrypt.append(inc);
        ep.write(bencrypt);

    return;

def decrypt(argv):
        #open file
        with open(argv[2],'rb') as fp:
            bcontent = fp.read();

        #open password
        with open(argv[3], 'rb') as pp:
            bpass = pp.read();

        for i in reversed(range(len(argv[2]))):
            if argv[2][i] == '.':
                break;

        #decrypt file
        with open(argv[2][:i] + "_otp_decrypted" + argv[2][i:], 'wb') as dp:
            bencrypt = bytearray();
            for i, d in enumerate(bcontent):
                #wrap
                if d - bpass[i] < 0:
                    wrap = 255 + d - bpass[i] + 1;
                    inc = wrap;
                else:
                    inc = d - bpass[i];
                bencrypt.append(inc);
            dp.write(bencrypt);

        with open('after.txt', 'w') as a:
            a.write(str([x for x in bencrypt]));

        return;

if __name__ == "__main__":
    try:
        main(sys.argv);
    except UserWarning as err:
        print("%s" % err, file=sys.stderr);
        exit(1);
