# In computing, A thread is an entity within a process which can be scheduled for execution. Also, the thread is 
# the smallest unit of processing which can be performed in an OS. 
# Features of thread - 
# 1. A thread is a sequence of such instructions within a program which can be executed independely of other code
# 2. A thread is simply a subset of process. 
# 3. A thread contains all the information in a Thread Control Block (TCB). 
# Components of the thread 
# a) Thread identifier - unique Id is assigned to every new thread 
# b) Stack identifier - Points to thread's stack in the process. Stack contains the local variables under the 
# thread's scope. 
# c) Program Counter - A register contains the address of the memory instructions currently being executed by the thread. 
# d) Thread's register set - Registers which are assigned to thread for computation. 
# e) Parent's process pointer - A pointer on the process control block (PCB) of the process which the thread lives. 

# print the thread name and the corresponding process for each task

import threading
import os 

def task1():
    print("Task1 is assigned to thread: {}".format(threading.current_thread().name))
    print("ID of the process of task1: {}".format(os.getpid()))


def task2():
    print("Task2 is assigned to the thread: {}".format(threading.current_thread().name))
    print("ID of the process of task2: {}".format(os.getpid()))    


if __name__ == "__main__":
    #print the ID of the current process
    print("ID of the process running main program: {}".format(os.getpid()))

    # print the main thread 
    print("Main thread name: {}".format(threading.current_thread().name))

    # Creating threading 
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # start the thread
    t1.start()
    t2.start() 


    # wait until all the threads finish 
    
    t1.join()
    t2.join()

        