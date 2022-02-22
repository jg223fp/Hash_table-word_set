#libraries and pythonfile imports
import os
import word_set as ws
import text_divider as td
import time
import matplotlib.pyplot as plt


#lists and variables
add_time_for_1000 = [0]
max_depth_for_each_1000 = [0]
size_for_each_1000 = [0]
bucket_list_size_for_each_1000 = [0]
count = 0
path = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\data\eng_news_100K-sentences.txt"


# Program starts 
word_set = ws.new_empty_set()  # Creates a word set with 10 empty buckets

print("Spliting words...")
split_time_start = time.time()
try:
    word_list = td.word_splitter(path)  # Split words and put in a list
except FileNotFoundError:
    print("File not found. Terminating...")
    quit()  
      
split_time_stop = time.time()
print("Total amount of words:",len(word_list))

no_duplicates = set(word_list)      # Makes sure that we dont have any duplicates so we actually add all items
print("\nAdding words to set...")
tot_add_time_start = time.time()
every_1000_start = time.time()
for word in no_duplicates:
    count += 1

    ws.add(word_set,word)                    # add word via addfunction 
    
    if count == 1000:                        # collects data for plots for every 1000 element
        add_1000_time = time.time()           
        add_time_for_1000.append(add_1000_time - every_1000_start)
        max_depth_for_each_1000.append(ws.max_bucket_size(word_set))
        size_for_each_1000.append(ws.size)
        bucket_list_size_for_each_1000.append(ws.bucket_list_size(word_set))
        count = 0                                   # reset count
        every_1000_start = time.time()              # reset timer

tot_add_time_stop = time.time()    

         
   
# Hash specific data
print("Elements in set:",ws.count(word_set))
mx = ws.max_bucket_size(word_set)
print("Max bucket:", mx)                
buckets = ws.bucket_list_size(word_set) 
print("Bucket list size:", buckets)     
# Time data
time_word_split = split_time_stop - split_time_start
time_set_add = tot_add_time_stop - tot_add_time_start
print("Time for word split:",time_word_split)
print("Time for adding to set:",time_set_add)


#plot 1
# x-axis: size_for_each_1000
# y-axis: bucket_list_size_for_each_1000
x = [x for x in size_for_each_1000]
y = [q for q in bucket_list_size_for_each_1000]
plt.xlabel('Size')
plt.ylabel('Bucket size')
plt.plot(x, y)
plt.show()

#plot 2
# x-axis: size_for_each_1000
# y-axis: add_time_for_1000
x = [x for x in size_for_each_1000]
y = [q for q in add_time_for_1000]
plt.xlabel('Size')
plt.ylabel('Time')
plt.plot(x, y)
plt.show()

#plot 3 
# x-axis: size_for_each_1000
# y-axis: max_depth_for_each_1000
x = [x for x in size_for_each_1000]
y = [q for q in max_depth_for_each_1000]
plt.xlabel('Size')
plt.ylabel('Depth')
plt.plot(x, y)
plt.show()