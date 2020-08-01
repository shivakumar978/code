# Threading:
# It is used to run multiple threads (function calls, tasks) at the same time

import time # I have imported time method
start = time.perf_counter()

def do_exercise(): # I am calling a function called do_exercise
    print("Exercising 1 minute..")
    time.sleep(1)
    print("Done Exercising...")


do_exercise() # running the function

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} minute(s)") # print the "finished" with total number of minutes

#----------------------------------------------------------------

# Above I ran the function one time, If I need to run the function 2 times:

import time 
start = time.perf_counter()

def do_exercise(): 
    print("Exercising 1 minute..")
    time.sleep(1)
    print("Done Exercising...")


do_exercise()
do_exercise() # the second time

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} minute(s)")


# It looks like :
# function(do_exercise)....1 minute....function(do_exercise)....1 minute...Finished

#---------------------------------------------------

# now lets do threading to so that the above called functions (do_exercise) 2 times runs simultaneously:

import threading
import time 
start = time.perf_counter()

def do_exercise(): 
    print("Exercising 1 minute..")
    time.sleep(1)
    print("Done Exercising...")
    
# Now I will create 2 threads:
t1 = threading.Thread(target=do_exercise) # target here is the function I want to run
# No () at the end of do_exercise because I just want to pass the function not execute it.
t2 = threading.Thread(target=do_exercise)

t1.start() # we use the start method to run the thread
t2.start()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} minute(s)")

#------------------------------------------------------

# To tell one thread to wait for another thread to finish, you call .join().

# In the above example, If I want the threads to finish before:
# 1. I calculate the finish time and
# 2. before I print out the script was finished
# To do this I will use join method: before the finish statement

import threading
import time 
start = time.perf_counter()

def do_exercise(): 
    print("Exercising 1 minute..")
    time.sleep(1)
    print("Done Exercising...")

t1 = threading.Thread(target=do_exercise)
t2 = threading.Thread(target=do_exercise)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} minute(s)")






