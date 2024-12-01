class Twitter:

    def __init__(self):
        """
        Initialize the Twitter class.
        - `recenttweets`: A list to store all tweets in the order they are posted.
        - `hashtweets`: A dictionary mapping tweet IDs to the user who posted them.
        - `hashfollowers`: A dictionary mapping a user ID to a set of their followers.
        - `posttweets`: A dictionary mapping a user ID to a list of tweets they have posted.
        """
        self.recenttweets = []  # List of all tweets in the order they are posted
        self.hashtweets = {}  # Maps tweet IDs to the user who posted them
        self.hashfollowers = collections.defaultdict(set)  # Maps user IDs to their followers
        self.posttweets  = collections.defaultdict(list)  # Maps user IDs to their list of posted tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a new tweet for a user.
        - Add the tweet ID to the `recenttweets` list.
        - Record the user who posted the tweet in `hashtweets`.
        - Add the tweet to the user's list of tweets in `posttweets`.
        
        Args:
        userId (int): ID of the user posting the tweet.
        tweetId (int): ID of the tweet being posted.
        """
        self.recenttweets.append(tweetId)
        self.hashtweets[tweetId] = userId
        self.posttweets[userId].append(tweetId)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Get the 10 most recent tweets from the user and their followers.
        - Retrieve the user's followers from `hashfollowers`.
        - Iterate through `recenttweets` in reverse (most recent first).
        - Check if the tweet belongs to the user or their followers.
        - Collect up to 10 tweets and return them.
        
        Args:
        userId (int): ID of the user requesting the news feed.
        
        Returns:
        List[int]: A list of up to 10 most recent tweet IDs.
        """
        # If the user has no followers and hasn't posted any tweets, return an empty feed
        if not self.hashfollowers[userId] and not self.posttweets[userId]:
            return []

        followers = self.hashfollowers[userId]  # Get the user's followers
        result = []

        # Iterate over tweets from the most recent to the oldest
        for tweet in self.recenttweets[::-1]:
            # Include tweets from the user or their followers
            if self.hashtweets[tweet] in followers or self.hashtweets[tweet] == userId:
                result.append(tweet)
            # Stop once we have 10 tweets
            if len(result) == 10:
                return result

        return result  # Return the collected tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Make a user follow another user.
        - Add the `followeeId` to the set of followers for `followerId` in `hashfollowers`.
        
        Args:
        followerId (int): ID of the user who wants to follow.
        followeeId (int): ID of the user to be followed.
        """
        self.hashfollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Make a user unfollow another user.
        - Remove the `followeeId` from the set of followers for `followerId` in `hashfollowers`.
        
        Args:
        followerId (int): ID of the user who wants to unfollow.
        followeeId (int): ID of the user to be unfollowed.
        """
        # Remove followeeId only if it exists in the follower's list
        if followeeId in self.hashfollowers[followerId]:
            self.hashfollowers[followerId].remove(followeeId)

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.hashfollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.hashfollowers[followerId]:
            self.hashfollowers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)