from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("pic.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Rachit", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("Rachit_poudel")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()