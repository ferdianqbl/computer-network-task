import time
import datetime
from multiprocessing import Process
from kirim_data import kirim_data


def runThreadProcess(d=0):
    procs = []
    catat_awal = datetime.datetime.now()
    for k in range(d):
        waktu = time.time()
        # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        procs.append(Process(target=kirim_data, args=(k,)))
        procs[k].start()
    # setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in range(d):
        procs[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


if __name__ == '__main__':
    runThreadProcess(10)
