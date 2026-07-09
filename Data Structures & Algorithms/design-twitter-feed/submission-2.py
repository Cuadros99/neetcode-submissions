class Twitter:

    def __init__(self):
        self.users_map = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.users_map:
            followees = self.users_map[userId]
        else:
            followees = { userId }

        timeline = []
        i = len(self.posts) - 1
        while i >= 0 and len(timeline) < 10:
            author, post_id = self.posts[i]
            if author in followees:
                timeline.append(post_id)
            i -= 1

        return timeline
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users_map:
            self.users_map[followerId].add(followeeId)
        else:
            self.users_map[followerId] = { followerId }
            self.users_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users_map and followerId != followeeId:
            self.users_map[followerId].discard(followeeId)
        
