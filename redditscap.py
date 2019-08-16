import praw
import json
import requests


class Reddit_bot:
    def __init__(self):
        self.scrape_picture('malefashionadvice')
    def loadAccount(self,cred,json_file = "settings.json",json_key ="redditcred"):
        with open(json_file) as f:
            data = json.load(f)

            user_values = data[json_key]
            username = user_values['username'],
            password = user_values['password'],
            client_id = user_values['client_id'],
            client_secret = user_values['client_secret'],
            user_agent = user_values['user_agent'],
            if cred == "username":
                uname= ''.join(username) 
                return uname
            elif cred== "password":
                pword= ''.join(password)
                return pword
            elif cred== "client_id":
                cid= ''.join(client_id)
                return cid
            elif cred== "client_secret":
                cse= ''.join(client_secret)
                return cse
            elif cred== "user_agent":
                ua= ''.join(user_agent)
                return ua
            return uname +","+pword +","+ cid+","+ cse +","+ua

    def download_picture(self,listedurl):
        url = listedurl
        # directory = "/home/fuego/Programming/unixwebscrape/pictures/"
        directory = "/Users/ross/Programming/Python/Igbot/IGREDBot/pictures/"
        filename = directory + url.split("/")[-1]
        r = requests.get(url, timeout=0.5)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(r.content)
    def connect_to_sub(self, subreddit):
        
        reddit = praw.Reddit(
            username=self.loadAccount("username"), password=self.loadAccount("password"),
            client_id =self.loadAccount("client_id"),client_secret=self.loadAccount("client_secret"),user_agent=self.loadAccount("user_agent")
            )
        subred = reddit.subreddit(subreddit)
        return subred

    def scrape_picture(self, sub):
        subred = self.connect_to_sub(sub)
        hot = subred.hot(limit = 11)
        new = subred.new(limit = 10)
        controv = subred.controversial(limit = 10)
        top = subred.top(limit = 10)
        gilded = subred.gilded(limit = 10)
        x =next(hot)  

        listedurl = []
        listedTitle =[]
        for i in hot:
            if i.url.endswith(".jpg"):
                self.download_picture(i.url)
            elif i.url.endswith(".png"):
                self.download_picture(i.url)
            elif i.domain.endswith('imgur.com'):
                self.download_picture(i.short_link)

if __name__ == '__main__':
    

    Reddit_bot = Reddit_bot()
    

