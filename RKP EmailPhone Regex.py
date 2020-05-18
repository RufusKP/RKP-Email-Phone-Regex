# Initiated: 5/14/20 2100 PST
# Completed: 5/17/20 1707 PST

# I completed this project as a part of my continuing endeavor of learning Python.  This specific project was an
# exercise from Al Sweigart's book  "Automate the Boring Stuff with Python: Practical Programming for Total Beginners".
# The way this program works is that it takes the data that is copied on the clipboard by pressing Ctrl-C or Cmd-C,
# and uses Regular Expressions (regexes) to find emails and phone numbers that may be contained within the data from
# the clipboard.



# Importing the Regular expression operations (re) module and the pyperclip module (developed by Al Sweigart).
# The pyperclip module will allow the contents of the clipboard to be used for the program
import re
import pyperclip


# This stores the contents of the clipboard in the variable "rawtext" on which the phone and email regex will be applied
rawtext = str(pyperclip.paste())


# This is the Regular Expression Object (regex Object) for finding phone numbers within the string data stored in "rawtext".  A Brief
# description of the various components of the regex can be seen adjacent to each constraint.
phoneregex = re.compile(r'''(
    \(?\d{3}\)? #areacode with or without brackets
    \.?-?\s?    #divider
    \d{3}       #second part of number
    \.?-?\s?    #divider
    \d{4}       #third part of number
    )''', re.VERBOSE)


# This stores the phone numbers found from "rawtext" in the variable "phonematchesfound"
phonematchesfound = phoneregex.findall(rawtext)


# This function takes phone number of various formats and puts it into a single format.  The formats that this function
# will work with are: xxx.xxx.xxxx, xxx-xxx-xxxx, xxx xxx xxxx, (xxx)xxxxxxx.  The single format that this function
# will convert the phone numbers to is: xxxxxxxxxx
def removedivider():
    index = (len(phonematchesfound))
    y = 0
    while y != index:
        oldstr = phonematchesfound[y]
        if "." in oldstr:
            newstr = oldstr.replace(".", "")
            phonematchesfound[y] = newstr
        if "-" in oldstr:
            newstr = oldstr.replace("-", "")
            phonematchesfound[y] = newstr
        if " " in oldstr:
            newstr = oldstr.replace(" ", "")
            phonematchesfound[y] = newstr
        if "(" in oldstr:
            oldstr1 = oldstr.replace("(", "")
            if ")" in oldstr1:
                newstr = oldstr1.replace(")", "")
                phonematchesfound[y] = newstr
            else:
                phonematchesfound[y] = newstr
        else:
            newstr = oldstr
        y += 1


# This is the Regular Expression Object (regex Object) for finding emails within the string data stored in "rawtext".  A brief
# description of the various components of the regex can be seen adjacent to each constraint.
emailregex = re.compile(r'''(
    \S+         #before @
    @           #@
    \w+         #after @
    \.
    \w{1,3}     #final part
    )''', re.VERBOSE)


# This stores the emails found from "rawtext" in the variable "emailmatchesfound"
emailmatchesfound = emailregex.findall(rawtext)


# This function puts all the found email and phone matches into one List.  Then, it specifies whether matches were
# found for emails, phone numbers, both, or neither.  Further, it places just the matches into the clipboard.  Hence,
# replacing the original clipboard contents with only the matches.
def tabularfinal():
    phonematches = []
    emailmatches = []
    m = 0
    e = 0
    for match in phonematchesfound:
        phonematches.append(phonematchesfound[m])
        m += 1
    for match in emailmatchesfound:
        emailmatches.append(emailmatchesfound[e])
        e += 1
        '\n'.join(emailmatches)
    emaillength = len(emailmatches)
    phonelength = len(phonematches)
    if phonelength > 0 and emaillength > 0:
        print("The following are the phone matches:")
        print('\n'.join(phonematches), "\n")
        print("The following are the email matches:")
        print('\n'.join(emailmatches))
        phonematches.extend(emailmatches)
        pyperclip.copy('\n'.join(phonematches))
        print("\n\nAll matches have been put onto your clipboard.")
    elif phonelength > 0 and emaillength == 0:
        print("The following are the phone matches:")
        print('\n'.join(phonematches), "\n")
        print("There were no  email matches found.")
        pyperclip.copy('\n'.join(phonematches))
        print("\n\nAll matches have been put onto your clipboard.")
    elif emaillength > 0 and phonelength == 0:
        print("The following are the email matches:")
        print('\n'.join(emailmatches), "\n")
        print("There were no  phone matches found.")
        pyperclip.copy('\n'.join(emailmatches))
        print("\n\nAll matches have been put onto your clipboard.")
    elif emaillength == 0 and phonelength == 0:
        print("There were no phone or email matches found.")


# This function contains that necessary sub-functions outlined above.
def emailphoneregex():
    removedivider()
    tabularfinal()

# This initiates the program to find emails and phone numbers from the data contained in the clipboard.
emailphoneregex()
