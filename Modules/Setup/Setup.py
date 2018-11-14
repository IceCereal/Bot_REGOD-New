def existSubdreddit_File(fileName = None):
    """
        EXISTENCE OF THE LIST_OF_SUBREDDITS FILE

        fileName:   The name of the file that contains the subreddit data:  ListOfSubreddits (default)
    """

    if fileName == None:
        fileName = 'ListOfSubreddits'

    print ("Checking Existence of ", fileName, "...")

    try:
        fileObj = open('ListOfSubreddits', 'r')
        fileObj.close()

        return 1

    except Exception as e:
        print ("\nError 1: Opening ListOfSubreddits")
        print (str(e))

        errorLog(str(e), 1)

        return -1

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
