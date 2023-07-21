import discord
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def read_data():
    """Reads data from frame data json, returns loaded data file."""
    with open('SF6FrameData.json', 'r') as file:
        data = json.load(file)
    return data

def capitalize_first_letter(user_string):
    """Takes a string with one or more words, returns a string with the first letter capitalized.
    """
    strings = user_string.split()
    cap_strings = [str.capitalize() for str in strings]
    result_string = ' '.join(cap_strings)
    return result_string

def upper_last_word(str):
    """Takes a string with one or more words, returns a string with the last word fully capitalized.
    """
    str_list = str.split()
    str_list[len(str_list)-1] = str_list[len(str_list) - 1].upper()
    str_list = ' '.join(str_list)
    return str_list

def format_message_norm(msg, character_name):
    """Takes an argument for a dictionary holding information on a specific character move and a character name. Returns a formatted message ready to be sent as a response.
    """
    extra_info = msg['extraInfo']

    extra_info = ["- " + extra_info[index] for index in range(len(extra_info))]     # JSON's [extra_info] gives list of comments with extra characters, turning into one processed string here
    extra_info = "\n".join(extra_info)                                              
    
    new_msg = (
            f">>> ### {character_name} - {msg['moveName']}\n"
            f"**Startup:**  {msg['startup']}      **Active:**  {msg['active']}      **Recovery:**  {msg['recovery']}\n"
            f"**On Block:**  {msg['onBlock']}      **On Hit:**  {msg['onHit']}\n"
            f"**__Extra Info:__**\n"  
            f"{extra_info}"
        )
    return new_msg

@client.event
async def on_ready():
    print(f'{client.user} is now running')

@client.event
async def on_message(message):
    """When users send a message, given the message is in appropriate format, replies with a message with the requested frame data. Sends an error message to the user if any part of their request is invalid.
    """
    if message.author == client.user:       # prevents infinite loop
            return
    if message.content.startswith('!'):
        try:
            user_channel = message.channel
            user_message = message.content[1:]         
            
            user_message = capitalize_first_letter(user_message)
            name_and_move = user_message.split(' ', 1)                  # name and move = [character_name, character_move]
            character_name = name_and_move[0]
            move_name = upper_last_word(name_and_move[1])
            
            data = read_data()
            frame_data = data[character_name]['moves']['normal'][move_name]
            
            await user_channel.send(format_message_norm(frame_data, character_name))
        except:
            await user_channel.send(">>> **Unable to process your request.**\n\nPlease enter requests in the format:\n!character stand/crouch action-button")
