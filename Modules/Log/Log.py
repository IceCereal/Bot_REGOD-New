from datetime import datetime

class Log:
    def __init__(self, fileName_regular = None, writeMode_regular = None, fileName_error = None, writeMode_error = None):
        """
            DEFINED IN __INIT__

            fileName_regular:   Name of the regular log file:   Bot_REGOD-log (default)
            writeMode_regular:  a:  append (default)
            fileName_error:     Name of the error log file:     Bot_REGOD-Error-Log (default)
            writeMode_error:    a:  append (default)

            fileName_subreddit: Name of the Subreddit Logger:   Bot_REGOD-Subreddit-Log (immutable)
            writeMode_subreddit:    a:  append (immutable)
        """

        if fileName_regular == None:
            fileName = "Bot_REGOD-log"

        if writeMode_regular == None:
            writeMode = 'a'

        if fileName_error == None:
            fileName = "Bot_REGOD-Error-log"

        if writeMode_error == None:
            writeMode = 'a'

        self.fileName_regular = fileName_regular
        self.writeMode_regular = writeMode_regular
        self.fileName_error = fileName_error
        self.writeMode_error = writeMode_error

        self.fileName_subreddit = "Bot_REGOD-Subreddit-Log"
        self.writeMode_subreddit = 'a'


    def errorLog(self, exception : str, number : int):
        """
            ERROR LOGGING FUNCTION

            Writes it as:
            TIMESTAMP
            Error Number: LOCATION NUMBER
            Error:  ERROR
            ------------------
        """

        fileObj = open("Modules/Log/Logs/" + self.fileName_error, self.writeMode_error)

        fileObj.write("\n\n"+str(datetime.now()))
        fileObj.write("\nError Number:\t"+str(number))
        fileObj.write("\nError:\t"+exception)
        fileObj.write("\n------------------\n")

        fileObj.close()

    def Log(self, loggingString: str):
        """
            NORMAL LOGGING FUNCTION

            Writes it as:
            [TIMESTAMP] | [Logging String]
        """

        fileObj = open("Modules/Log/Logs/" + self.fileName_regular, self.writeMode_regular)

        fileObj.write("\n[" + str(datetime.now()) + "] | [" + loggingString + "]")

        fileObj.close()

    def SubredditLog(self, subreddit : str):
        """
            LOGGING FUNCTION TO LOG ONLY SUBREDDIT'S

            Writes it as:
            |{[TIMESTAMP], [Subreddit]}
        """

        fileObj = open("Modules/Log/Logs/" + self.fileName_subreddit, self.writeMode_subreddit)

        fileObj.write("|{[" + str(datetime.now()) + "], [" + subreddit + "]}")

        fileObj.close()
