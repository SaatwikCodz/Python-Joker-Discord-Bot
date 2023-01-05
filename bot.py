import os
import discord
from discord.ext import commands
import responses
import re

# Send messages

with open('.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

async def send_message(message, user_message, is_private):
  try:
    response = responses.handle_response(user_message)
    await message.author.send(
      response) if is_private else await message.channel.send(response)

  except Exception as e:
    print(e)


def run_discord_bot():
  Token = ""
  client = discord.Client(command_prefix=">", intents=discord.Intents.all())
  bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())
  @client.event
  async def on_ready():
    print(f'{client.user} is now running!')

  @client.event
  async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')
    await welcome_channel.send(f'Welcome to the server, {member.mention}!')

  @client.event
  async def on_message(message):
    if message.content.startswith('!membercount'):
      guild = message.guild
      member_count = len(guild.members)
      await message.channel.send(f"There are {member_count} members in this server.")
    if message.content.startswith('!ban'):
      roles = message.author.roles
      user = message.mentions[0]
      for role in roles:
        if role.name == 'Moderator':
          user_to_ban = message.mentions[0]
          await message.guild.ban(user_to_ban)
          await message.channel.send(f'{user_to_ban.name} was banished!')
    if message.content.startswith('!kick'):
      roles1 = message.author.roles
      for role in roles1:
        if role.name == 'Moderator':
          user_to_kick = message.mentions[0]
          await message.guild.kick(user_to_kick)
          await message.channel.send(f'{user_to_kick.name} was kicked!')
    # Make sure bot doesn't get stuck in an infinite loop
    if message.author == client.user:
      return

    # Get data about the user
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Debug printing
    print(f"{username} said: '{user_message}' ({channel})")

    # If the user message contains a '?' in front of the text, it becomes a private message
    if user_message[0] == '?':
      user_message = user_message[1:]  # [1:] Removes the '?'
      await send_message(message, user_message, is_private=True)
    else:
      await send_message(message, user_message, is_private=False)

  # Remember to run your bot with your personal TOKEN
  client.run(os.environ[key])

