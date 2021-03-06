#Imports
from datetime import datetime
from ast import literal_eval
from time import sleep
import praw
import sys

#Custom Imports
sys.path.append("Modules/Log/")
from Log import Log

sys.path.append("Modules/PopularityIndex/")
from PopularityIndex import Popularity

sys.path.append("Modules/Setup/")
from Setup import Setup


def createRedditInstance():
    #Creating A Reddit Instance

    Log.Log("createRedditInstance: Begin")

    try:
        with open("TOKEN", 'r') as FileObj:
            credentialsRaw = FileObj.read()
            credentials = literal_eval(credentialsRaw)

    except Exception as e:
        print ("\nError *. Reading TOKEN and Obtaining Credentials")
        print (str(e))
        #errorLog(e, 1)
        sys.exit()

    print ("Authenticating the Reddit Credentials")

    try:
        reddit = praw.Reddit(
                            client_id = credentials['client_id'],
                            client_secret = credentials['client_secret'],
                            user_agent = credentials['user_agent'],
                            )

    except Exception as e:
        print ("\nError *: Authentication")
        print (str(e))

        #errorLog(e, 3)

        sys.exit()

    print ("\tAuthentication Complete\n")

    return reddit
    #### REDDIT INSTANCE CREATED ####

#Main Loop
def main(reddit, subreddits):
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
                popularity = PopularityIndex.popularityIndex(int(postVars['ups']), int(postVars['downs']), int(postVars['num_comments']))

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
            subRFileObj = open("Modules/SubredditData/"+subr, 'a')
            subRFileObj.write("$"+str(outputFileList))
            subRFileObj.close()

            Log.SubredditLog(subr)

            #Nap for 9 seconds
            sleep(9)

#Begin Main Loop
if __name__ == '__main__':

    print ("\nBegin Bot_REGOD")
    print ("v1.0.0")
    print ("IceCereal\n")
    sleep(1)

    setup = Setup()
    subreddits = setup.returnSubreddits()

    Log = Log()

    Log.Log("BEGIN: Bot_REGOD")

    PopularityIndex = Popularity()

    reddit = createRedditInstance()

    main(reddit, subreddits)
