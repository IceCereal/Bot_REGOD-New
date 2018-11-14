#Imports
from datetime import datetime
from ast import literal_eval
from time import sleep
import praw
import sys

#Custom Imports
sys.path.append("Modules/Log/")
import Log

sys.path.append("Modules/PopularityIndex/")
import PopularityIndex

sys.path.append("Modules/Setup/")
import Setup


#Create Reddit instance
try:
    with open("TOKEN", 'r') as FileObj:
        credentialsRaw = FileObj.read()
        credentials = literal_eval(credentialsRaw)

except Exception as e:
    print ("\nError 1. Reading TOKEN and Obtaining Credentials")
    print (str(e))
    #errorLog(e, 1)
    sys.exit()

print ("Reddit Instance Creation")
try:
    reddit = praw.Reddit(
                        client_id = credentials['client_id'],
                        client_secret = credentials['client_secret'],
                        user_agent = credentials['user_agent'],
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

        print ("\nBegin Bot_REGOD")
        print ("v1.0.0")
        print ("IceCereal\n")
        sleep(1)


        fi = open("MainLog", 'w')
        print ("\nTime:\t",str(datetime.now()))
        fi.write(str(datetime.now())+"\n")
        fi.close()
        main()

except Exception as e:
    filo = open("MainLog", 'w')
    filo.write(str(datetime.now())+str(e))
    print (e)
