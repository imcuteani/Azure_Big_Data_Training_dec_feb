# multi-threading in Python 

# process - it's a heavyweight instance of a computer program which is being executed. Any process has three basic 
# components, 
# a) An executable program
# b) an associated data required by the program (variables, buffers etc.)
# c) the execution context of the program (state of process)

# A process in OS consists of multiple threads. Thread is the basic entity within the process which can be scheduled
# for execution, also, it's the smallest unit of processing which can be performed on any OS. 
# A thread contains all of the information within the thread control block (processID, threadID, info) etc. 
# A thread is a sequence of such instructions within a program which can be executed independently of the code. 


import threading

# create two threads t1 and t2 & perform cube and square operations 

def print_cube(num): 
    print("Cube block: {}".format(num * num * num))


def print_square(num):
    print("Square of number: {}".format(num * num))


if __name__ =="_main_":
    #creating thread 
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))


    #starting thread t1
    t1.start()
    #starting thread t2
    t2.start()

    # wait until the thread t1 is being finished execution 

    t1.join()

    #wait until the thread t2 is being finished execution 

    t2.join()

    # both of the threads are finished with execution 

    print("Multi-Thread execution is done")

 
 