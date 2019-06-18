#!/usr/bin/python
import __Config
import math
import mysql.connector
from mysql.connector import Error
import subprocess as sub
import threading
import time
    ##error when we failed to connect 

mydb = mysql.connector.connect(
                               host=__Config.DATABASE_CONFIG['host'],
                               user=__Config.DATABASE_CONFIG['user'],
                               passwd=__Config.DATABASE_CONFIG['password'],
                               database=__Config.DATABASE_CONFIG['dbname']
                               )

mycursor = mydb.cursor()
mycursor.execute("select company_domain from domain_inventory ")
myresult = mycursor.fetchall()

DomainsList = []
s = 0
for x in myresult:
    #DomainsList[s] = x
    #part1, part2 = x[0]
    #print('{} - {}'.format(part1, part2))
    DomainsList.append(x[0])
    s += 1


startTime = time.time()


#DomainsList = ["paradisesage.com", "ratingevents.com", "patchlot.com", "shotscycle.net", "ofthedaywind.com", "mafialady.net", "squadpos.com", "viewsclock.com", "transportpics.net", "patrolmaker.net", "mirrorforward.com", "siderocket.net", "wonderski.com", "ranchclip.net", "phoenixmode.net", "specialistsvan.com", "missioncharts.com", "scrapbookroute.com", "pickerpick.com", "optimumpin.net", "uniquerep.net", "worksexperience.com", "utopiafair.net", "updateratings.net", "waysdomain.com", "techsforest.com", "marketsquick.com", "loftcoach.net", "questionsusa.net", "showcaseout.com", "workshopnerd.com", "managersimply.com", "matestrends.com", "sellsregistry.com", "reporterrobot.com", "sessiongator.com", "visionbusy.com", "warriordeal.net", "republiccats.com", "triviadeck.net", "tableflow.net", "shotscompare.com", "trainboom.net", "seriessol.net", "wallfiles.net", "presentpic.net", "transportshot.com", "tracemeeting.com", "ratingsten.com", "metricstext.net"]


count = len(DomainsList)
#print(' '.join(map(str, DomainsList)))
#print(', '.join(DomainsList))
#exit()

instance = 10
total = 0

def creates_items(start, end):
    global total
    
    print("Range from {} to {}".format(start, end))
    
    if len(DomainsList[start:end]) > 0:
        for domain in DomainsList[start:end]:
            #time.sleep(15)
            #print("Total Current : {}".format(total))
            total += 1
            cmd = 'dig ' + domain + ' +short'
            Result = sub.getoutput(cmd)
            print(domain + " : " + Result)
            #print("Total Current : {}".format(total))
            total -= 1
 
        print("Creation is done for item")
    else:
        print("Cancelled from {} : {}".format(start, end))



def limits_items():
    
    global total
    while True:
        time.sleep(1)
        if total > 5:
            print('Maximum Limit Reached')
            time.sleep(1)
        else:
            time.sleep(1)
            print('Waiting')
            

jobs = []
i = 0
start = 0
end = 0
for i in range(count):
    if start > count:
        break
    else:
        #end = start + instance
        if end < 1:
            end = instance
        else:
            end = end + instance
        
        creator = threading.Thread(target=creates_items, args=(start, end))
        jobs.append(creator)
        start = end + 1
        i -= 1
    
            
limitor = threading.Thread(target=limits_items, daemon=True)

for j in jobs:
    j.start()

limitor.start()

for j in jobs:
    j.join()

print("Our Ending Value total is ", total)

endTime = time.time()

print("Total Time Consumed for the exceution {}".format(endTime - startTime))
