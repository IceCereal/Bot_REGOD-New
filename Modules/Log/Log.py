from datetime import datetime

class Log:
    def __init__(self, fileName = None, writeMode = None):
        """
            DEFINED IN __INIT__

            fileName:   Name of the file:   Bot_REGOD-log (default)
            writeMode:  a:  append (default)
        """

        if fileName == None:
            fileName = "Bot_REGOD-log"

        if writeMode == None:
            writeMode = 'a'

        self.fileName = fileName
        self.writeMode = writeMode


    def errorLog(self, exception : str, number : int):
        """
            ERROR LOGGING FUNCTION

            Writes it as:
            TIMESTAMP
            Error Location: LOCATION NUMBER
            Error:  ERROR
            ------------------
        """

        fileObj = open(self.fileName, self.writeMode)

        fileObj.write("\n"+str(datetime.now()))
        fileObj.write("\nError Location:\t"+str(number))
        fileObj.write("\nError:\t"+exception)
        fileObj.write("\n------------------\n")

        fileObj.close()
