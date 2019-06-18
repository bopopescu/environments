import csv

with open('teamTest.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #DictReader => it is used for key as header and column in pair
    
    for line in csv_reader:
        print(line)
    
    
    with open('newTestcreateTab.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')
    
        #print(csv_reader)
    
        for i in csv_reader:
            csv_writer.writerow(i)
            #print(i[4])
        