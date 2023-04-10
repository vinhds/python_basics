#Bessie the cow is writing an essay. Each word in the essay contains only low-
#ercase or uppercase characters. Her teacher has specified the maximum
#number of characters, not counting spaces, that can occur per line. To sat-
#isfy this requirement, Bessie writes down the words of the essay using the
#following rules:
#• If the next word fits on the current line, add it to the current line.
#Include a space between each pair of words on the line.
#• Otherwise, put this word on a new line; this line becomes the new
#current line.
#Output the essay with the correct words on each line.
#Input
#Read input from the file named word.in.
#The input consists of two lines.
#• The first line contains two integers separated by a space. The first
#integer is n, the number of words in the essay; it’s between 1 and
#100. The second integer is k, the maximum number of characters
#(not counting spaces) that can occur per line; it’s between 1 and 80.
#• The second line contains n words, with a space between each pair of
#words. Each word has at most k characters.
#Output
#Write output to the file named word.out.
#Output the properly formatted essay.



# Idea:
# Go through the list of words
# Have a variable to which words are keep added to
# Keep track of the length of this variable and stop until it is > K
# Subtract the last word from the variable
# Have a variable to keep track of the number of spaces

    
# STEP 1: Write a function to read input from each file and return the input in appropriate format

def input_reader(filename):
    input_file = open(filename, 'r')
    first_line = input_file.readline().rstrip()
    second_line = input_file.readline().rstrip()
    n, k = map(int, first_line.split(' '))
    word_list = second_line.split(' ')
    return n, k, word_list;

# STEP 1': Test the input_reader function
#filename = 'word_bronze_jan20/10.in'
#n, k, word_list = input_reader(filename)
#print(n)
#print(k)
#print(word_list)
#print('Start solving now:')

# STEP 2: Write a function to process the input and return the required output. Essentially, solve the problem.
def essay_formatter(n, k, word_list):
    result = []
    s = ''
    n_spaces = 0
    i = 0
    while i < n:
        previous = s
        s += word_list[i] + ' '
        n_spaces += 1
        l = len(s) - n_spaces
        if l > k:
            result.append(previous.rstrip())
            s = ''
            n_spaces = 0
            if i > 0:
                i-= 1
            if i == (n-2):
                result.append(word_list[i+1])
                break
        i += 1
    return result

# STEP 2': Test the essay_formatter function
#result = essay_formatter(n, k, word_list)
#check = True
#for i in range(len(result)):
#    test_str = ''.join(result[i].split(' '))
#    if len(test_str) > k:
#        check = False
#        print(f'Found a problem at location {i}. Problem is {result[i]}')
#        
#if check == True:
#    print(result)
#else:
#    print('Check the algorithm')

# STEP 3: Write a function to write the result to file

def output_writer(filename, result):

