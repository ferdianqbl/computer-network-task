from threading import Thread
import sys
from kirim_data import kirim_data


def client_thread():
    threads = []
    count = 0
    try:
        # count = AtomicCounter()

        for i in range(sys.maxsize):
            threads.append(Thread(target=kirim_data))
            # count.increment()
            count += 1
            threads[i].start()

        print(f"client {count}")
        for thread in threads:
            thread.join()
    except Exception:
        print("limit reached")


if __name__ == '__main__':
    client_thread()
