#!/usr/bin/python3

import sys
import os
import re

def checkArgs ():
    """
    It checks the number of input arguments and prints a diagnostic error message which states the correct usage of the python program
    :return: The name of input and output files given on command line
    """
    if len(sys.argv) != 3: # Checks if the length of argument is less  than 3
        sys.stderr.write("Usage: ./prog5.py inFile outFile\n\n") # If the condition is true then print the uage of the python program
        sys.exit() # Aborts the program if the program does not have correct number of arguments
    return sys.argv[1], sys.argv[2] # It retursn the name of input and output files

def openFiles (files):
    """
    It opens the input and output files.If the file cannot be opened then prints a diagnosticerror message 
    :param files: Contains the name of the files
    :return: The generated file objects for the files is returned
    """
    try:
        inputFile = open(files[0])# Opens the input file in read mode
    except IOError: # Enters this loop if the file cannot be opened
        print ("Can't Open File: " +  files[0] + '\n') # If the file cannot be opened it prints a error message
        sys.exit() # It aborts the program if the file cannot be opened
    finally:
        try:
            outputFile = open(files[1], 'w') # Opens the output file in write mode
        except IOError: # Enters the loop if the file cannot be opened
            print ("Can't Open File: " +  files[1] + '\n') # Prints an error message if the file cannot be opned
            sys.exit() # It aborts the program if the file cannot be opned
    return (inputFile, outputFile) # Returns the input and output files

def closeFiles ( fobjects ):
    """
    It close the input and output files.If the file cannot be closed it prints a diagnostic error message
    :param fobjects: Contains the file objects generated from the files
    """
    try:
        fobjects[0].close() # Closes the input file
    except IOError: # Enters the loop if the file cannot be closed
        print ("Can't Close File: " +  fobjects[0] + '\n') # Prints an error message if the input file cannot be closed
        sys.exit() # Aborts the program if the file cannot be closed
    finally:
        try:
            fobjects[1].close() # Closes the output file 
        except IOError: # Enters the loop if the output file cannot be closed
            print ("Can't Close File: " +  fobjects[1] + '\n') # Prints an error message if the output file cannot be closed
            sys.exit() # Aborts the program if the file cannot be closed

def createList (inFileObj):
    """
    It creates a list of words from the text stored in the input file and splits them using whitespaces and dashes
    :param inFileObj: Object for the file
    :return : Final list is returned
    """
    text = inFileObj.read() # inFileObj contents are read as a whole  and stored in the variable text
    return re.split(r'-|\s|"', text) # The final list where all the words are splitted based o the whutespaces are then returned

def createDictionary ( words ):
    """
    It removes all non-alphabetical characters from each word and puts each word in its corresponding frequency in the dictionary excluding the empty words
    :param words: LIst in which all the whitespaces are removed
    : return: The dictionary with the frequency is returned
    """
    dictionary = {} # It creates a dictionary
    for values in words: # for loop to check for the values in words
        values=values.lower() # Convert all the values in lowercase
        values = re.sub('^[^a-zA-Z]+|[^a-zA-Z]+$',"", values) # It replaces the string that matches the regular expression that starts with a and ends with z instead of perfect match
        values = re.sub('[^a-zA-Z-].*',"", values) #It replaces the string in the regular expression which atarts with a and see if there are zero or more occurances it replaces with spaces
        values = re.findall('[a-zA-Z]+',values) # If there are one or more occurances of words between a and z findall returns a list containing all matches
        for word in values: # For loop to check for word in values
            dictionary[word]=dictionary.get(word,0)+1 # Look for occurance of word in dictionary if present increment it by one and return else it is not incremented
    return dictionary # Return the dictionary that conatins the count of the words

def main ():
    """
    It prints the size of the dictionay and its contents also call all the other functions.It is the entry point in the program
    :return: None
    """
    files = openFiles(checkArgs()) # It calls the function openFiles which give a call to the checkArgvs function
    files[0] # The infile is reffered as file[0]
    files[1] # The outfile is reffered as file[1]
    dictionary = createDictionary(createList(files[0])) # Taking the list genertaed from the input file we create a dictionary 
    files[1].write('Output Values for Data: ' +files[0].name + "\n") # Print the output value of the data for the input file
    files[1].write("-" * 57) # The representation of dashed lines is done
    files[1].write('\n' + "size = " + str(len(dictionary)) + '\n\n') # The size of the file is printed based on the length of the dictionary
    count_of_line = 0 # Intially the count variable is set to 0
    for word in sorted(dictionary.keys()): # For loop is taken for sorted order of keys in dictionary
        if count_of_line < 3: # If the count value is less than 3
            files[1].write(format(word, "<16") + format(": ", ">") + format(dictionary[word], ">2") + '\t')# Contents of dictionary are printed with words on left and frequency on the right
            count_of_line = count_of_line + 1 # The value of count variable is increased
        else: # If the count value is not less than three we print the following line
            files[1].write('\n' + format(word, "<16") + format(": ", ">") + format(dictionary[word], ">2") + '\t') # The words in the dictionary are printed
            count_of_line = 1 # The count value remains 1
    closeFiles(files) # The call to the closeFile function closes the opned files

main() # The main function is called without any arguments
