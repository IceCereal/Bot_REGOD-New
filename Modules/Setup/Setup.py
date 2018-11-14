import sys
import subprocess
from ast import literal_eval

#Import
sys.path.append("../Log/")
import Log

class Setup:
    def __init__(self):
        """
            SETUP: Bot_REGOD

            Runs:
                > existSubreddit_File
                > convertData
                > createDirs:
                    * SubredditData
                    * Logs

            Returns:
                > A list of 100 subreddits
        """

        print ("Running SETUP: Bot_REGOD")

        #CREATE DIRECTORIES
        if (self.createDirs() == -1):
            print ("Setup Fail")
            sys.exit()

        Log.Log("createDirs: Complete")
        #CREATE DIRECTORIES COMPLETE

        Log.Log("SETUP: START")

        #EXISTENCE OF LIST_OF_SUBREDDITS
        if (self.existSubdreddit_File() == -1):
            Log.Log("SETUP: FAIL")
            sys.exit()

        Log.Log("existSubreddit_File: Complete")
        #COMPLETE EXISTENCE OF LIST_OF_SUBREDDITS

        #CONVERT DATA
        self.subreddits = self.convertData()

        if (self.subreddits == -1):
            Log.Log("SETUP: FAIL")
            sys.exit()

        Log.Log("convertData: Complete")
        #CONVERT DATA COMPLETE

        Log.Log("SETUP: COMPLETE")


    def existSubdreddit_File(self):
        """
            EXISTENCE OF THE LIST_OF_SUBREDDITS FILE

            fileName:   The name of the file that contains the subreddit data:  ListOfSubreddits
        """

        fileName = 'ListOfSubreddits'

        try:
            fileObj = open("Modules/Setup/"+fileName, 'r')
            fileObj.close()

            return 1

        except Exception as e:
            print ("\nError 1: Opening ListOfSubreddits")
            print (str(e))

            #errorLog(str(e), 1)

            return -1


    def convertData(self):
        """
            Convert the Subreddit Data File to Readable Data

            fileName:   The name of the file that contains the subreddit data:  ListOfSubreddits
        """

        fileName = 'ListOfSubreddits'

        try:
            fileObj = open("Modules/Setup/"+fileName, 'r')

            subredditsRaw = fileObj.read()
            subreddits = literal_eval(subredditsRaw)

            fileObj.close()

            return subreddits

        except Exception as e:
            print ("\nError 2: Converting raw data to readable data")
            print (str(e))

            #errorLog(str(e), 2)

            return -1

    def createDirs(self):
        """
            Creates Directories:
                ../Log/Logs
                ../SubredditData/
        """

        try:
            subprocess.run(['mkdir', '../Log/Logs/'])
            subprocess.run(['mkdir', '../SubredditData/'])

            return 1

        except Exception as e:
            print ("\nError *: Making Directories: Logs, SubredditData")
            print (str(e))

            #errorLog(str(e), *)

            return -1

    def returnSubreddits(self):
        return self.subreddits
