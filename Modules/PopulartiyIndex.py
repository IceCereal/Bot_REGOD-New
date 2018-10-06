class Popularity:
    def __init__(self, popularityMode = None):
        """
            DEFINED IN __INIT__

            popularityMode: To choose which function to use as popularityIndex: 0 (default)
        """

        if popularityMode == None:
            popularityMode = 0

        self.popularityMode = popularityMode


    def popularityIndex(self, ups, downs, numComments, popularityMode = None):
        """
            POPULARITY INDEX CHOOSING FUNCTION

            Chooses a function from the below defined functions
            to choose as a popularity function. If no argument is
            provided, it chooses the self.popularityMode as the
            popularityMode. If another number is passed as an argument,
            it will use that function only during that function
            call.
        """

        if popularityMode == None:
            popularityMode = self.popularityMode

        if popularityMode == 0:
            return popularityIndex_0(ups, downs, numComments)

        if popularityMode == 1:
            return popularityIndex_1(ups, downs)

        return -1


    def popularityIndex_0(self, ups, downs, numComments):
        """
            POPULARITY INDEX 0

            Returns the value of Upvotes + Downvotes, if the
            number of Comments is less than that. Otherwise,
            returns the number of Comments. This is because of
            certain subreddits (AskReddit) having more number
            of comments per post than the number of votes.

            Returns: int
        """

    	if ( (ups+downs) > numComments):
    		return (ups+downs)
    	return numComments


    def popularityIndex_1(ups, downs):
        """
            POPULARITY INDEX 1

            Returns the value of Upvotes + Downvotes

            Returns: int
        """

        return  (ups, downs)
