import functools
import time


@functools.lru_cache(maxsize=None) #Cache to perform same task...
def calculate():
    r = 0
    for i in range(10**8):
        r += 1
    return r




def main():
    # Process 1
    start = time.time()
    result = calculate()
    stop = time.time()

    # Process 2
    start1 = time.time()
    result1 = calculate()
    stop1 = time.time()

    # Print process 1 with TOtal time taken
    print(f"Result value is :{result}")
    print(f"time taken {stop-start}")

    # Print process 1 with TOtal time taken
    print(f"Result value is :{result1}")
    print(f"time taken {stop1-start1}") 

if __name__=='__main__':
    main()