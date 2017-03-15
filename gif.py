import requests
import datetime
import praw

reddit_application_name = "gifreddit"
client_id = "PrEiGobRwi4Hxw"
client_secret = "wSSeHDB4iLuI1mgLryt6vgVF4Os"
url_application = "http://gifreddit.heroku.com/"
redirect_url = "http://gifreddit.heroku.com/redirect"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='gifreddittelegrambot',
                     username='',
                     password='')

# def main():
    # print reddit.read_only
    # for submission in reddit.subreddit('funny').hot(limit=10):
        # print(submission.url)













class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        self.timeout = timeout
        self.offset = offset
        params = {'timeout': self.timeout, 'offset': self.offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler("306413636:AAGZittTDC9og0ExX0Q7wgIBNhw7RE-4nCY")
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            for submission in reddit.subreddit('funny').hot(limit=10):
                greet_bot.send_message(last_chat_id,submission.url)
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            for submission in reddit.subreddit('funny').hot(limit=10):
                greet_bot.send_message(last_chat_id,submission.url)
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            for submission in reddit.subreddit('funny').hot(limit=10):
                greet_bot.send_message(last_chat_id,submission.url)
            today += 1

        new_offset = last_update_id + 1




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

