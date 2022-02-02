import discord
import os
import random
import json


def get_joke():
    with open('jokes.json', 'r') as outfile:
        jokes_data = json.load(outfile)
    jokes = jokes_data['with_author'] + jokes_data['without_author']
    return random.choice(jokes)

client = discord.Client()
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('joke'):
        joke = get_joke()
        await message.channel.send(joke)

if __name__ == '__main__':
    token = os.getenv('TOKEN')
    client.run(token)
