### Mutex
**Puzzle:** Add semaphores to the following example to enforce mutual exclusion to shared variable `count`

Thread A
```
count = count + 1
```

Thread B
```
count = count + 1
```

**Answer:**

Main
```
count = 0
mutex = Semaphore(1)
a(mutex)
b(mutex)
```

Thread A
```
mutex.acquire()
count = count + 1
mutex.release()
```

Thread B
```
mutex.acuire()
count = count() + 1
mutex.release()
```
------------------------------------

### Multiplex

**Puzzle:** Generalize the previous solution so that it allows multiple threads to run in the critical section at the same time, but it enforces an upper limit on the number of concurrent threads. In other words, no more than `n` threads can run in the critical section at the same time.

**Answer:**

Main
```
count = 0
mutex = Semaphore(n)
a(mutex)
b(mutex)
...
n+x(mutex)
```

Thread X
```
mutex.acquire()
critical section
mutex.release()
```


