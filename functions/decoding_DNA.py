#DNA is made up of two twisted strands that encode genes using long combinations of four bases:
#    Adenine, Cytosine, Guanine and Thymine. The strands are complementary to one another,
#    meaning that Adenine and Thymine are always opposite each other, and Cytosine and Guanine are always opposite each other, like this.
#A double strand of DNA: 	
#
#ATCAAGGCCTATTCCGGGAAAGG
#TAGTTCCGGATAAGGCCCTTTCC
#
#In order for the information in a gene to be used, it has to be transcribed into a strand of RNA.
#During this process, a portion of one strand of DNA is transcribed – this portion is known as the transcription unit.
#The start of the sequence to be transcribed is signaled by a sequence of bases known as a promoter, and the end is signaled by a sequence known as the terminator. For our purposes, the promoter is the sequence TATAAT, which begins 10 bases before the start of the transcription unit, and the terminator consists of two distinct, complementary, reversed sequences of at least length 6 that cause the RNA molecule to coil back on itself and pinch off the transcribed strand. If TATAAT appears twice on a strand, only the first occurrence counts as the promoter. An example is shown below.
#Copy
#
#AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
#
#In this example the promoter and terminator sequences are boldfaced, and the transcription unit is underlined.
#The resulting RNA will be complementary to the transcription unit, except that in RNA Uracil takes the place of Thymine.
#For this example, the result looks like this:
#Copy
#
#CCUAAAUCUAACUGGG
#
#The input will contain five single strands of DNA, one on each line.
#Write a program to output the RNA sequence that results from the transcription process.
#The sequences should be numbered starting at 1 , with a colon and a single space character following the number, as shown below.
#Sample Input
#Copy
#
#AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
#AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA
#TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT
#
#Sample Output
#Copy
#
#1: CCUAAAUCUAACUGGG
#2: UAGCGCUGCUUUAU
#3: CUCUCUGGCUCACAAAUUC

# Plan:
# FIRST STEP: Let's start by writing a function that will transcribe the transcription unit

def complementary(dna_str, rna=False):
    """
    dna_str is a string that consists of characters 'A', 'C', 'G' and 'T' 
    rna is a boolean variable (default = False) which indicates whether to transcribe dna_str to 
    a complementary strand (rna=False) or an RNA strand (rna=True)

    Return the resulting strand which is complementary to the transcription unit
    A ---> U, T ---> A, C <---> G if rna=True
    A <---> T, C <---> G if rna = False
    """
    s = ''
    for char in dna_str:
        if char == 'A':
            if rna == True:
                s += 'U'
            else:
                s += 'T'
        elif char == 'T':
            s += 'A'
        elif char == 'C':
            s += 'G'
        else:
            s += 'C'
    return s

# Test the function transcribe
# print(complementary('GGATTTAGATTGACCC'))
# print(complementary('GGATTTAGATTGACCC', True))

# SECOND STEP: Write a function to that takes a string and determine whether there exists a terminator.
# Plan: Start at the beginning and vary two things: the location and the length (>=6) of a subtring.
# Then do complementary and reverse of that substring and determine whether the resulting sequence 
# exists in the remaining part of the original string.

def find_terminator(dna_str):
    """
    dna_str is a string that consists of characters 'A', 'T', 'C', 'G'

    Return the location of the terminator
    The terminator consists of two distinct, complementary, reversed sequences of at least length 6
    The location is the location of the first sequence
    """
    start = 0
    while start < len(dna_str):
        check = False
        length = 6
        while start + length < len(dna_str):
           # print(f'Check with start = {start}, and length = {length}')
            sequence = dna_str[start:(start+length)]
           # print(f'sequence = {sequence}')
            comp_seq = complementary(sequence)
            match = comp_seq[::-1]
           # print(f'match = {match}')
            if dna_str[(start+length+1):].find(match) != -1:
           #     result = sequence
                check = True
           #     print('Find match')
                break
            else:
                length += 1
           #     print('NEXT')
        if check == True:
           # print('Done')
            break
        else:
            start += 1   
           # print(f'Next Start = {start}')
    return start
    
# Test find_terminator
# print(find_terminator('ACCCGTCATGCAAGTCCATGCATGACAGC'))
def find_promoter(dna_str, promoter='TATAAT'):
    return dna_str.find(promoter)

# Test find_promoter
#print(find_promoter('AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC', 'TATAAT'))

# THIRD STEP: Write a function that take a DNA sequence and transcribe it
def transcriber(dna_str):
    promoter_loc = find_promoter(dna_str, 'TATAAT')
    #print(promoter_loc)
    terminator_loc = promoter_loc + 11 + find_terminator(dna_str[(promoter_loc+11):]) 
    #print(terminator_loc)
    transcription_unit = dna_str[(promoter_loc+10):(terminator_loc)]
    #print(transcription_unit)
    return complementary(transcription_unit, rna=True)

# Test transcriber
# print(transcriber('AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC'))

# Solve the problem
for i in range(5):
    dna_str = input()
    print(i+1, end=': ')
    print(transcriber(dna_str))
