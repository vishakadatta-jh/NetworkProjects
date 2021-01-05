import sys
import random
from ip_subnet_valid import *

subnet_octet_binary = []
for i in subnet_octet:
    binary_octet = bin(int(i).lstrip('Ob'))
    subnet_octet_binary.append(binary_octet.zfill(0))