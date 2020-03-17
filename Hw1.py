# Part. 1
#=======================================
# Import module
# csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107000119.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.


#for row in data:
#if row['TEMP']==-99 or row['TEMP']==-999:
# remove row

#=======================================1

#target_data = data[:10]
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   #print(tmp)
   if tmp > max:
    max = tmp

out_list = []
if tmp == -99 or tmp == -999:
   out_list.append(['C0A880','None'])
else:
   out_list.append(['C0A880',max])

#print (out_list)


#=======================================1

#=======================================2

#target_data = data[:10]
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   #print(tmp)
   if tmp > max:
    max = tmp

if  tmp == -99 or tmp == -999:
   out_list.append(['C0F9A0','None'])
else:
   out_list.append(['C0F9A0',max])

#print (out_list)

#print (max)


#=======================================2


#=======================================3

#target_data = data[:10]
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   #print(tmp)
   if tmp > max:
    max = tmp

if tmp == -99 or tmp == -999:
   out_list.append(['C0G640','None'])
else:
   out_list.append(['C0G640',max])

#print (out_list)

#print (max)


#=======================================3


#=======================================4

#target_data = data[:10]
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   #print(tmp)
   if tmp > max:
    max = tmp

if  tmp == -99 or tmp == -999:
   out_list.append(['C0R190','None'])
else:
   out_list.append(['C0R190',max])

#print (out_list)

#print (max)


#=======================================4


#=======================================5

#target_data = data[:10]
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
max = 0

for row in target_data:
   tmp = float(row['TEMP'])
   #print(tmp)
   if tmp > max:
    max = tmp

if tmp == -99 or tmp == -999:
   out_list.append(['C0X260','None'])
else:
   out_list.append(['C0X260',max])

print (out_list)

#print (max)


#=======================================5


# Part. 4
#=======================================
# Print result
# print(target_data)
#========================================