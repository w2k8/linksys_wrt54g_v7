#!/usr/bin/env python
import struct
import binascii 
import sys
import os

# # TROC file system
# 0       string      TROC    TROC filesystem,
# >4      lelong      x       %d file entries
# >4      lelong      <1      {invalid}


# 6170706c792e68746d000000000000 02ea    0000087d6c53    01  	apply.htm...........}lS.
# 6261642e68746d0000000000000000 020d 0a 00001c0201e3    01  	bad.htm..................
# 62617369632e68746d000000000000 230c    00001e0cacb1    01  	basic.htm......#........
# 484d41432e68746d00000000000000 040d 0a 0000f091090d 0a 01 	HMAC.htm..................
# 484d616e6167652e68746d00000000 03ed    0000f49bf941    01	    HManage.htm...........A.

# 0000087d01	01	6170706c792e68746d000000000000	02ea	00  ...}..apply.htm.........
# 00087d6c53	01	6170706c79312e68746d0000000000	03d8	00  ..}lS.apply1.htm........
# 000b67f2cb	01	6170706c79322e68746d0000000000	0279	00  ..g...apply2.htm......y.

# due to sometime strange bytes between fileoffset, filesize and filename, the filesize might be wrong. 

trocheader = 8
lengte = 24
filelength = 14
filesize = 3
other = 6
last = 0


start = trocheader
file_list = []

def test_last_byte(blob):
    if blob[-1] == "0x0a":
        blob += f.read(1)
        # print(blob)
    return blob

current_offset = 0
file_len = os.stat('ftp/igwhtm.dat').st_size
tmp = 'Filename','Size','Other','Hexdata'
print('{:14} - {:6} - {:14} - {}'.format(tmp[0], tmp[1], tmp[2], tmp[3]))
# print('Filename - Size - Other - Hexdata')
with open("ftp/igwhtm.dat", "rb") as f:
    try:
        troc_header = f.read(trocheader)
        current_offset += trocheader
        nr_of_files = struct.unpack(">i"  , troc_header[ 4: 8] )
        nr_of_files = int.from_bytes(nr_of_files, "big")
        for i in range(nr_of_files):

            file_name = file_size = file_other = ''
            blob = f.read(24)  
            current_offset += 24
            other = 6
            # Sometimes there is an extra byte
            try:
                if blob[5] != 1:
                    # print(blob[5], blob[6])
                    other = 7
                    blob += f.read(1)
                    current_offset += 1
            except:
                print(blob)

            # Make sure the last byte is a 0x00
            try:
                if blob[-1] != 0:
                    # print(blob[5], blob[6])
                    blob += f.read(1)
                    current_offset += 1
            except:
                print(blob)
            
            # file_name  =  struct.unpack("14c" , blob[ 6: 19] ) 
            # file_size  =  struct.unpack(">i"  , blob[ 19: 23] )
            # file_other =  struct.unpack("6c"  , blob[ 0: 6] ) 

            file_other  = blob[   : other  ]
            file_offset = blob[   : other -1  ]
                
            file_name   = blob[ other : 14 + other ]
            file_size   =  struct.unpack(">i"  , blob[ other + 13: other + 17] )

            file_name = file_name.decode('ascii').strip('\0')

            other = hex(int.from_bytes(file_other[:], "big"))
            file_size = file_size[0]
            blob_string = hex(int.from_bytes(blob, "big"))
            print('{:14} - {:6} - {:14} - {}'.format(file_name, file_size, other, blob_string ))
            
            # print('{}'.format(file_name))
            if file_other[-1] != 1:
                tmp = f.read(1)
    except struct.error:
        pass