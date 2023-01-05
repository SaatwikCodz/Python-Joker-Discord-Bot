import random


def handle_response(message) -> str:
  p_message = message.lower()
  if p_message == 'hello':
    return 'Hey there!'
  if p_message == 'roll':
    return str(random.randint(1, 6))
  if p_message == '!help':
    return "`You can ask the moderators for help`"
  if p_message == 'ban me':
    return "Sorry I can only do it if the server owners tell me to"
  if "python" in p_message:
    return "To paste Python Code use 6 backticks and then py in between them to beautify your code"
  if p_message == "hey there":
    return 'Hey there!'
  if p_message == "gg":
    return "Keep Up, appreciate people more"
  if p_message == "hi":
    return "Hello"
  if p_message == "rules":
    return "No Swearing"
