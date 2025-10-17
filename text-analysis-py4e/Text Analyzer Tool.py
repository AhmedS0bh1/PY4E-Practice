# This project was made during my learning phase to practice file handling and text analysis in Python.
#########################################################################################################
# Request file name from user
file_name = input("Enter file name: ") 
try:
    # reading file and make a file handle object for it
    handle = open(file_name, "r")
#exception if the file wasn't exist 
except FileNotFoundError: 
    print("File not found.")
    quit()
# Initialize variables will be needed
number_of_lines = 0 # to get the number of lines of the file
word_counts = dict() # A dictionary works as a frequency array to get each word as a key and its frequency as a value
total_length = 0 # will help in calculating the average of the length of the words in the file
# Loop to take file line by line
for line in handle:
    line = line.rstrip() # remove the white spaces in the end of the line to avoid any error in analyzing
    number_of_lines += 1 # Calculating the number of the lines by increasing the value for the variable by one
    words = line.split() # make a list of words in the line by splitting it by white spaces between words
    # Loop to fill the frequency array with the words and its frequency
    # And to calculate the total length of all words in the file
    for word in words:
        word_counts[word] = word_counts.get(word,0)+1 # If the word was in the dict it will be increased by 1 else it will be initailized by zero
        total_length += len(word) # add the length of the word to the total length of all words to help in calculating the average
total_words = sum(word_counts.values()) # Calculating how many word in the file
unique_words = len(word_counts) # Calculating the number of the unique values by counting the keys of the dictionary
avg = total_length/total_words # Calculating the average of the words lenght by dividing the length of all words on the number of the total_words in the file
maximum_word, maximum_word_count = max(word_counts.items(),key= lambda x:x[1]) # Max function will return a tuple which has the maximum value in the second element of the tuples from the items in words_count dictionary and then assign the word to the maximum word and assign the value to the maximum_word_count

print(f'''
File analyzed: {file_name}
Lines: {number_of_lines}
Total words: {total_words}
Unique words: {unique_words}
Most frequent word: "{maximum_word}" ({maximum_word_count} times)
Average word length: {avg:.2f}
''')
