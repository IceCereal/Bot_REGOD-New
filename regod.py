#Imports
from datetime import datetime
from ast import literal_eval
from time import sleep
import praw
import sys

#Logger Function
def errorLog(exception : str, number : int):
    fileObj = open("Bot_REGOD-log", 'a')
    fileObj.write("\n"+str(datetime.now()))
    fileObj.write("\nError Location:\t"+str(number))
    fileObj.write("\nError:\t"+e)
    fileObj.write("\n------------------\n")
    fileObj.close()

#Popularity Index Function
def popularityIndex(ups, downs, numComments):
	if ( (ups+downs) > numComments):
		return (ups+downs)
	return numComments

print ("\nBegin Bot_REGOD\nv1.0.0\nIceCereal\n\nObjective: To Collect Data\n")
sleep(1)

#Check If Subreddits-File Exists
print ("ListOfSubreddits verification")
try:
    fileObj = open('ListOfSubreddits', 'r')

except Exception as e:
    print ("\nError 1: Opening ListOfSubreddits")
    print (str(e))
    errorLog(str(e), 1)
    sys.exit()

#Convert The Subreddit Data to Readable Data
print ("Convert Subreddit Data to Readable Data")
try:
    subredditsRaw = fileObj.read()
    #subreddits = literal_eval(subredditsRaw)
    fileObj.close()
    word = []
    subrs = []
    for char in subredditsRaw:
        if char == "\n":
            subrs.append(''.join(word))
            word = []
            continue
        else:
            word.append(char)
    subreddits = subrs[0:len(subrs)-1]
    print (subreddits)
    print (len(subreddits))
    #print ("\n\nEnter?")
    #a = input()

except Exception as e:
    print ("\nError 2: Converting raw data to readable data")
    print (str(e))
    errorLog(str(e), 2)
    sys.exit()

#Create Reddit instance
print ("Reddit Instance Creation")
try:
    reddit = praw.Reddit(
                        #THIS IS A SECRET
                        )

except Exception as e:
    print ("\nError 3: Authentication")
    print (str(e))
    #errorLog(e, 3)
    sys.exit()

#### SETUP COMPLETE ####
print ("Setup Complete\n")

#Main Loop
def main():
    print ("Begin Main Loop")

    #Infinite Loop
    while True:

        #All the subreddits - loop over them
        for subr in subreddits:

            print ("Process on:\t"+subr)

            #outputFileList - List that is being written to the file
            #popularityList - Sub-List of outputFileList that contains the valuable data that's required
            outputFileList = []
            popularityList = []

            #Inner Loop - Goes through posts in subreddit
            for post in reddit.subreddit(subr).top('hour'):

                #Get the variables of the post
                postVars = vars(post)

                #Check the popularity of given post #Params Passed: Upvotes, Downvotes, Number of Comments
                popularity = popularityIndex(int(postVars['ups']), int(postVars['downs']), int(postVars['num_comments']))

                #Append the popularity to the popularityList
                popularityList.append(popularity)


            #Rectify the Popularity List
            #Case 1: When less than 10 posts are there per hour
            #Solution 1: Add 0's to make the list have 10 elements
            popularityList.sort(reverse=True)
            if len(popularityList) < 10:
                for i in range(len(popularityList),10,1):
                    popularityList.append(0)

            #Case 2: When more than 10 posts are present in an hour
            #Solution 2: Sort the list in Descending order and take top 10
            if len(popularityList) > 10:
                popularityList.sort(reverse=True)
                popularityList = popularityList[0:10]

            #Write popularityList to outputFileList
            outputFileList.append(str(datetime.now()))
            outputFileList.append(popularityList)

            #Write The outputFileList to the File
            subRFileObj = open("SubredditData/"+subr, 'a')
            subRFileObj.write("$"+str(outputFileList))
            subRFileObj.close()

            #Nap for 9 seconds
            sleep(9)

#Begin Main Loop
try:
    if __name__ == '__main__':
        fi = open("MainLog", 'w')
        print ("\nTime:\t",str(datetime.now()))
        fi.write(str(datetime.now())+"\n")
        fi.close()
        main()

except Exception as e:
    filo = open("MainLog", 'w')
    filo.write(str(datetime.now())+str(e))
    print (e)
