"""
    This file is for the most basic actions includeing
        - command handler
        - boot and reboot
        - thread spawning
        - error/log file writeing 
    """

import os
import sys

import discord
from dotenv import load_dotenv

from reqMods.modules.controller import controller
from reqMods.Logger import Logger


def initClient():
    global client
    loadToken()
    client = discord.Client()


def loadToken():
    global TOKEN
    
    if len(sys.argv) >= 2:
        TOKEN = sys.argv[1]
    else:
        load_dotenv(".env")
        TOKEN = os.environ.get("TOKEN")

initClient()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot == True:
        return
    

    message_start = message.content[:message.content.find(" ") if message.content.find(" ") != -1 else len(message.content)]

    # Send message to all daemons
    for module in controller.modules.values():
        if module.paused: return

        for daemon in module.daemons.values():
            await daemon.call(message)


        if message_start.startswith(module.prefix) if module.prefix else False:
            

            for _, command in module.commands.items():

                if (command.public_chats and message.channel.type.name == "text") or (command.dm_chats and message.channel.type.name == "private") or (command.group_chats and message.channel.type.name == "group"): # TODO add way to make a command only work in dm's

                    for call in command.command:
                        

                        if message_start == module.prefix + call:
                            
                            Logger.debug_command(message=message, command=command)
                            await command.call(message)

                            return

if __name__ == "__main__":
    controller.loads()
    controller.reloads()

    client.run(TOKEN)
