#!/usr/bin/python

import threading
import time

total = 4

def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print("added item {}".format(i))
        print("Total Current : {}".format(total))
        total += 1
    print("Creation is done for item")

def creates_items2():
    global total
    for i in range(7):
        time.sleep(1)
        print("added item2 {}".format(i))
        print("Total Current : {}".format(total))
        total += 1
    print("Creation is done for item2")  

def limits_items():
    
    global total
    while True:
        if total > 5:
            print('Overload')
            total -= 3
            print('Subtracted 3')
        else:
            time.sleep(1)
            print('Waiting')
            
creator1 = threading.Thread(target = creates_items)            
creator2 = threading.Thread(target = creates_items2)
limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())

creator1.start()
creator2.start()
limitor.start()


creator1.join()
creator2.join()

print("Our Ending Value total is ", total)


#starttime = time.time()
#
#def sleeper(n,name):
#    print("{} has started".format(name))
#    time.sleep(n)
#    print("{} has finished".format(name))
#    
#
#thread_list = []
#    
#for i in range(5):
#    t = threading.Thread(target = sleeper, name = 'thread{}'.format(i), args = (5, 'thread{}'.format(i)) )
#    thread_list.append(t)
#    t.start()
#    #print('{} has been started'.format(t.name))
#
#    
#for t in thread_list:
#    t.join()
#
#endtime = time.time()    
#    
#print("All threads are finished")
#print("Total Time Taken : {}".format(endtime - starttime))

