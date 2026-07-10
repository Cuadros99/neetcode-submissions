class Twitter:

    def __init__(self):
        self.followers_map = {}
        self.posts_map = defaultdict(list)
        self.posts_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_counter += 1
        self.posts_map[userId].append((self.posts_counter, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        timeline = []
        if userId not in self.followers_map:
            self.followers_map[userId] = { userId }
        followees = self.followers_map[userId]

        for followee in followees:
            posts = self.posts_map[followee]
            if posts:
                index = len(posts)-1
                counter, last_post = posts[index]
                max_heap.append((-counter, last_post, followee, index))
        
        heapq.heapify(max_heap)

        while max_heap and len(timeline) < 10:
            counter, post_id, user_id, index = heapq.heappop(max_heap)
            timeline.append(post_id)
            index -= 1
            if index >= 0:
                next_counter, next_post = self.posts_map[user_id][index]
                heapq.heappush(max_heap, (-next_counter, next_post, user_id, index))

        return timeline

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers_map:
            self.followers_map[followerId].add(followeeId)
        else:
            self.followers_map[followerId] = { followerId }
            self.followers_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers_map and followerId != followeeId:
            self.followers_map[followerId].discard(followeeId)
        
