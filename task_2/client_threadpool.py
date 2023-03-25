import sys
import socket
import logging
import time
from concurrent.futures import ThreadPoolExecutor 
from kirim_data import kirim_data

def runThreadpool():
    catat_awal = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        for k in range(10):
            # print(f"mendownload {urls[k]}")
            #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
            executor.submit(kirim_data,nama=f"thread ke -{k}")

    catat_akhir = time.perf_counter()
    selesai = round(catat_akhir - catat_awal,2)
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


if __name__=='__main__':
    runThreadpool()
        
