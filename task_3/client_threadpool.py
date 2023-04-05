from sys import maxsize
from concurrent.futures import ThreadPoolExecutor
from kirim_data import kirim_data


def runThreadpool():
    pools = []
    with ThreadPoolExecutor() as executor:
        for k in range(maxsize):
            pools = [executor.submit(kirim_data, nama=f"thread ke -{k}")]

        for pool in pools:
            pool.result()


if __name__ == '__main__':
    runThreadpool()
