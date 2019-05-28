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





