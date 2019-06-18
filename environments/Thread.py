from threading import Thread
import time
import subprocess as sub

def myfunc(domain):
    #print(domain)
    cmd = 'dig '+ domain +' +short'
    Result = sub.getoutput(cmd)
    print(domain + " : " + Result)

    #print("sleeping 5 sec from thread %d" % i)
    #time.sleep(5)
    #print("finished sleeping from thread %d" % i)



DomainsList = ["writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net"]


TotalNumber = len(DomainsList)

while TotalNumber > 0:
    for domain in DomainsList:
        
        t = Thread(target=myfunc, args=(domain, ))
        t.start()
        TotalNumber -= 1 # OR TotalNumber = TotalNumber - 1
    while Thread(activeCount()) > 1:
        pass
    else:
        exit()



#import threading
#import time
#  
#  
#lock = threading.Lock()
#  
#def thread_test(num):
#    phrase = "I am number " + str(num)
#    with lock:
#        print(phrase)
#        time.sleep(5)
#        f.write(phrase + "\n")
# 
#  
#threads = []
#f = open("text1.txt", 'w')
#for i in range (100):
#    t = threading.Thread(target = thread_test, args = (i,))
#    threads.append(t)
#    t.start()
#  
#while threading.activeCount() > 3:
#    pass
#else:
#    f.close()