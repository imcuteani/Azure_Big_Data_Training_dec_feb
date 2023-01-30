# Thread synchronization 

# It's a mechanism defined to ensure that two or more concurrent threads do not simultaneously execute some particular 
# program segment known as critical section. 
# Critical section is the part of OS where all of the shared resources can be accessed. 
# Concurrent accesses to shared resources by multiple threads at the same time leads to race condition (deadlock)
# A race condition occurs when two or more threads can access shared data and they try to change the data at the same time
# As a result, the values of variables may be unpredictable and vary depending of the timings of the context of the process. 
# 

# thread lock to overcome the mutual exclusion/race condition in python multithreading 
 
import threading

# global variable
x = 0 

def increment_val():
    global x 
    x += 1 

def thread_task(lock):                # target function of the threads  
    for _ in range(100000):           # calls the thread upto 1M times 
        lock.acquire()                # to acquire a lock 
        increment_val() 
        lock.release()

def main_task(): 
    global x
    x = 0 

# Create the lock on the thread to overcome the mutual exclusive scenario 

lock = threading.Lock() 

# Creating threads

t1 = threading.Thread(target=thread_task, args=(lock,))
t2 = threading.Thread(target=thread_task, args=(lock,))

# Start the threads 
t1.start()
t2.start() 

# wait for the threads to finish the execution 
t1.join()
t2.join() 

# Define the main method 

if __name__ == "__main__":
    for i in range(10): 
        main_task()
        print("Iteration for {0}: x = {1}".format(i,x))





