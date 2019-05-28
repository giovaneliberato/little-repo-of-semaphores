#coding: utf-8

import threading
import time

count = 0

def thread(char, n, mutex, barrier):
    with mutex:
        print("\tRENDEZVOUS %s" % char)

    barrier.release()
    while barrier._value < n: pass

    global count
    count += 1
    print("\tCHAR %s - COUNT + 1 = %d" % (char, count))

def main():
    chars = "ABCDEFGHIJ"
    n = len(chars)
    barrier = threading.Semaphore(0)
    mutex = threading.Semaphore(n)

    context_thread = lambda ch: threading.Thread(target=thread, args=(ch, n, mutex, barrier))

    threads = []
    for ch in chars:
        threads.append(context_thread(ch))

    print("---- STARTING %d THREADS" % n)
    [t.start() for t in threads]

    while count < n: pass
    time.sleep(1)
    print("---- FINAL VALUE OF COUNT %d" % count)


if __name__ == '__main__':
    main()
