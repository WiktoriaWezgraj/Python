class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(self.username)
        for i in self.posts:
            print(i)

def main():
    user = SocialMediaProfile('johndoe')
    user.add_post('Hello, world!')
    user.add_post('Had a great day at the park!')
    user.add_post("What's up, Natalie? How are you?")
    user.display_timeline()
                   
main()
