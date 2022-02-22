# A list based hash table implementation for strings.
# Initial bucket size is 10, we then double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets

# Adds word to word set if not already added
def add(word_set, word):                                         
    global size                                                                                                        
    hashsum = calc_hashsum(word_set,word)  # Calculate bucket index for word
    
    if word not in word_set[hashsum]:  # If the word is not in the bucket , put word in bucket and increase size by 1
        word_set[hashsum].append(word)                                                                     
        size += 1                                                                                                                                                                                                               
                    
    if size == len(word_set):                                         
        rehash_up(word_set)  
          
# Returns current number of elements in set
def count(word_set):
    return size

# Returns current size of bucket list
def bucket_list_size(word_set):
    return len(word_set)

# Returns a string representation of the set content
def to_string(word_set):
    string = ""
    for bucket in word_set:
        for word in bucket:
            string += word + " "
    return string        
                
# Returns True if word in set, otherwise False    
def contains(word_set, word):
    hashsum = calc_hashsum(word_set,word)
    return word in word_set[hashsum]
    
# Removes word from set if there,  
# does nothing if word not in set
def remove(word_set, word):
    global size
    hashsum = calc_hashsum(word_set,word)
    if word in word_set[hashsum]:
        word_set[hashsum].remove(word)
        size -= 1
        if size < len(word_set)/2:           # shrinks bucketlist to half size if elements are fewer than buckets                                     
            rehash_down(word_set)

# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    deepest = 0
    for bucket in word_set:
        if deepest < len(bucket):
            deepest = len(bucket)
    return deepest    
 
# Calculate hashsum witch is used as index number for the word   
def calc_hashsum(word_set,word):                                         # for each char in key:
    hashsum = 0                                                          # hashsum += (char index + key lenght)^char code 
    for letter in word:                                                  # hashsum = hashsum % capacity
        hashsum += ((word.index(letter) + len(word))**ord(letter))       
    hashsum = hashsum % len(word_set)
    return hashsum

# Doubles the size of the bucket list when adding and nElements = bucketSize
def rehash_up(word_set):
    global size
    size = 0                                 # resets size count 

    word_set_copy = word_set.copy()
    word_set.clear()
    for _ in range(len(word_set_copy)*2):    # Doubles the size of the bucket list 
        word_set.append([])    

    for bucket in word_set_copy:    
        for word in bucket:                 
            add(word_set,word)                # Adds all the old elements        
    
# Shrinks the size of the bucket list when removing and nElements < bucketSize/2
def rehash_down(word_set):
    global size
    size = 0                                 # Resets size count

    word_set_copy = word_set.copy()
    word_set.clear()
    for _ in range(len(word_set_copy)//2):    # Shrinks the size of the bucket list to half of its size 
        word_set.append([])    

    for bucket in word_set_copy:    
        for word in bucket:                   # Adds all the old elements
            add(word_set,word)                     
    
    
     
    


