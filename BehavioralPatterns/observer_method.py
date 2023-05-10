from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, user, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, tweet):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, author, tweet):
        pass


class UserAccount(Subject):  # Observable
    def __init__(self, username):
        self.username = username
        self.tweets = []
        self.followers = {}

    def attach(self, user,  observer):
        self.followers[user] = observer

    def detach(self, observer):
        del observer.followers[self]

    def notify(self, tweet):
        for follower in self.followers.values():
            follower.update(self.username, tweet)

    def follow(self, user):
        follower = Follower(self)
        user.attach(follower.user, follower)

    def unfollow(self, user):
        self.detach(user)

    def tweet(self, text):
        self.tweets.append(text)
        self.notify(text)

    def untweet(self, index):
        del self.tweets[index-1]


class Follower(Observer):  # Observer
    def __init__(self, user):
        self.user = user

    def update(self, author, tweet):
        print(f'{self.user.username} received a notification: {author} tweeted: {tweet}')


if __name__ == '__main__':
    user1 = UserAccount('John Donatello')
    user2 = UserAccount('Jane Smith')
    user3 = UserAccount('Bob Johnson')

    # User2 and User3 follow of User1
    user2.follow(user1)
    user3.follow(user1)

    user1.tweet('Hello World!')
    print()
    user1.untweet(1)

    user1.tweet('How are we?')
    print()

    # User1 and User3 follow of User2
    user1.follow(user2)
    user3.follow(user2)

    user2.tweet('I\'m having a great day!')
    print()

    # User3 unfollow of User2
    user3.unfollow(user2)
    user2.tweet('Goodbye!')
