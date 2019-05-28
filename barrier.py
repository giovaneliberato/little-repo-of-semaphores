#coding: utf-8

import threading


def wait_for_all(threads):
    while True:
        for i in range(len(threads)):
            if threads[i].acquire():
                threads.pop(i)
        break

def thread(char, done, correlated_done):
    print("STATEMENT %s1" % char)
    print("RELEASE %s" % char)
    done.release()
    print("WAIT OTHERS %s" % char)
    wait_for_all(correlated_done)
    print("STATEMENT %s2" % char)

def main():
    multiplex = threading.Semaphore(0)
    c_arrived = threading.Semaphore(0)

    t_A = threading.Thread(target=thread, args=('A', a_arrived, [b_arrived, c_arrived]))
    t_B = threading.Thread(target=thread, args=('B', b_arrived, [a_arrived, c_arrived]))
    t_C = threading.Thread(target=thread, args=('C', c_arrived, [a_arrived, b_arrived]))
    t_A.start()
    t_B.start()
    t_C.start()

if __name__ == '__main__':
    main()
