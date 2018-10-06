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
