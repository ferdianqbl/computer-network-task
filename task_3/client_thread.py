from threading import Thread
from kirim_data import kirim_data
import sys

def client():
    threads = []
    try:  
        for i in range(sys.maxsize):
            threads.append(Thread(target=kirim_data))
            
            threads[i].start()

        for thread in threads:
            thread.join()

    except Exception:
        print("limit reached")

if __name__ == "__main__":
    client()
