import sys

class Setup:
    def __init__(self):
        print ("Running SETUP: Bot_REGOD")
        Log.Log("START SETUP")

        if (self.existSubdreddit_File() == -1):
            Log.Log("SETUP FAIL")
            sys.exit()

        Log.Log("existSubreddit_File: Complete")



    def existSubdreddit_File(self):
        """
            EXISTENCE OF THE LIST_OF_SUBREDDITS FILE

            fileName:   The name of the file that contains the subreddit data:  ListOfSubreddits
        """

        fileName = 'ListOfSubreddits'

        print ("Checking Existence of ", fileName, "...")

        try:
            fileObj = open('ListOfSubreddits', 'r')
            fileObj.close()

            return 1

        except Exception as e:
            print ("\nError 1: Opening ListOfSubreddits")
            print (str(e))

            #errorLog(str(e), 1)

            return -1
