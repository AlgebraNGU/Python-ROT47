
# Simple ROT47 Cipher

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("cipher",  help="Enter the ciphered text (ROT47)")

args = parser.parse_args()
data = args.cipher

def rot47(data):
        decode = []
        for i in xrange(len(data)):
                encoded = ord(data[i])
                if encoded >= 33 and encoded <= 126:
                        decode.append(chr(33 + ((encoded + 14) % 94)))
                else:
                        decode.append(data[i])
        return ''.join(decode)

print "Encrypted Cipher: {}\nDecrypted Cipher: {}".format(args.cipher, rot47(data))
