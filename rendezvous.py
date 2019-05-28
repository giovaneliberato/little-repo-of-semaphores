#coding: utf-8

import threading


def thread(char, done, correlated_done):
    print("STATEMENT %s1" % char)
    done.release()
    correlated_done.acquire()
    print("STATEMENT %s2" % char)

def main():
    a_arrived = threading.Semaphore(0)
    b_arrived = threading.Semaphore(0)

    t_A = threading.Thread(target=thread, args=('A', a_arrived, b_arrived))
    t_B = threading.Thread(target=thread, args=('B', b_arrived, a_arrived))
    t_A.start()
    t_B.start()

if __name__ == '__main__':
    main()
