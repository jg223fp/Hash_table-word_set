def word_splitter(path):
    import os 
    import re
    text_string = ''
    file = open(path, "r",encoding='utf-8')
    for line in file:
        if line == '\n':
            continue
        text_string += line.lower()
    file.close()
    processed_text = re.sub("[^a-zåäö']",' ',text_string)   
    sequenced_words = processed_text.split(" ")
    filtered_list = []
    for item in sequenced_words:
        if len(item) == 1:
            for x in item:
                if x == 'a' or 'i':
                    filtered_list.append(x)
                else:
                    continue
        elif item != "":
            filtered_list.append(item)
    amount = len(filtered_list)
    return filtered_list