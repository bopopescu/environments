#!/usr/bin/python

import subprocess as sub
DomainsList = ["writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net","writergem.com", "factorsure.com", "brosra.com", "communityio.net" ,"dasdasdasfsfsdfeal" , "domesticdeal.net"]
#print(DomainsList)


for domain in DomainsList:
    cmd = 'dig '+ domain +' +short'
    Result = sub.getoutput(cmd)
    print(domain + " : " + Result)