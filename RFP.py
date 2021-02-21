#!/usr/bin/python3

#Rayburn File Program RFP.py

import os

def main():

    directory = input("Please enter the directory to save your file : ")
    filename = input("Please enter a filename : ")
    name = input("Please enter your name : ")
    address = input("Please enter your address : ")
    phone_number = input("Please enter your phone number : ")

#This will check for the directory

    if os.path.isdir(directory):

#This will create and then open the file

        writeFile = open(os.path.join(directory,filename),'w')

#This writes the data

        writeFile.write(name+','+address+','+phone_number+'\n')

#This will close the file

        writeFile.close()

        print("File contents:")

#This will read back the file content

        readFile = open(os.path.join(directory,filename),'r')

        for line in readFile:

            print(line)

        readFile.close()

    else:

        print("Please enter a directory that already exists.")

main()
