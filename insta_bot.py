from instabot import Bot
bot = Bot()
bot.login(username="_rachit_poudel", password="R@chit2060@$")

######  upload a picture #######
#bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("ezsnippet")

#####  send a message #######
#bot.send_message("Hello from Rachit how are u man its a bot message donot rply this its a code scripted message so dont rply  and it is made of the code so be careful ", ['username'])

######  get follower info #######
# my_followers = bot.get_user_followers("usename")
# for follower in my_followers:
#     print(follower)

# bot.unfollow_everyone()