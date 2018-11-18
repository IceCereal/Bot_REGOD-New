# Bot_REGOD New
`v1.0.0` Stable<br/><br/>

The REddit_Gatherer_Of_Data (REGOD) is a bot developed to get data from the top 100 subreddits.

    Objective:	To get the Popularity of top 10 posts in a subreddit sorted by top - 'hour' every 15 minutes.
    Library:  PRAW6
    PopularityIndex:  Upvotes+Downvotes or Number_of_Comments
    Use Case: This data will be used to figure out what time of the day is the best to post to get maximum number of views
    Deploy Time:  1 Month

The old bot (worked on some other algo) is <a href="https://github.com/IceCereal/Bot_REGOD">here</a><br/><br/>
Main Bot: <a href="https://github.com/IceCereal/Bot_REGOD-New/blob/master/regod.py">REGOD</a><br/>
Subreddit List: <a href="https://github.com/IceCereal/Bot_REGOD-New/blob/master/Modules/Setup/ListOfSubreddits">ListOfSubreddits</a><br/>
PostVars: <a href="https://github.com/IceCereal/Bot_REGOD-New/blob/master/PostVars.txt">A file of all the variables (JSON) that a post has</a><br/><br/>

The data has been collected for 24 hours and accordingly uploaded to <a href="https://github.com/IceCereal/Bot_REGOD-New/tree/master/Modules/SubredditData">`SubredditData/`</a>. Each file contains data taken at 15 minute intervals in the following format:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`$[str(datetime.datetime.now()), [popularity - explained below]]`
    
popularity:
> Popularity is a Python list that contain the subreddits top ten popular values (Popularity Index) of the past hour. They are   arranged in descending order. If there are insufficient values, the rest are replaced by zero.

Example Data collected:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;`$['2018-11-14 21:21:48.136096', [93, 67, 61, 53, 48, 46, 44, 42, 41, 40]]`

