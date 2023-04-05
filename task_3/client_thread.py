import sys
import socket
import logging
import time
from kirim_data import kirim_data

if __name__=='__main__':
    for i in range(1,12):
        kirim_data(i)
