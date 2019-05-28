#coding: utf-8

import threading

count = 0

def thread(char, n, mutex, barrier):
    with mutex:
        print("RENDEZVOUS %s" % char)


    barrier.release()

    while barrier._value < n:
        pass

    global count
    count += 1
    print("CHAR %s - COUNT + 1 = %d" % (char, count))

def main():
    n = 3
    barrier = threading.Semaphore(0)
    mutex = threading.Semaphore(n)

    t_A = threading.Thread(target=thread, args=('A', n, mutex, barrier))
    t_B = threading.Thread(target=thread, args=('B', n, mutex, barrier))
    t_C = threading.Thread(target=thread, args=('C', n, mutex, barrier))
    t_A.start()
    t_B.start()
    t_C.start()

if __name__ == '__main__':
    main()
