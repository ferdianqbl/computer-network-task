from sys import maxsize
from multiprocessing import Process
from kirim_data import kirim_data


def runThreadProcess():
    processes = []
    for k in range(maxsize):
        processes.append(Process(target=kirim_data, args=(k,)))
        processes[k].start()
    for k in range(processes):
        processes[k].join()


if __name__ == '__main__':
    runThreadProcess()
