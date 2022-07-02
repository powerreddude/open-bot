async def commandHelloWorld(message):
    await message.channel.send("Hello world!")

#when sending variable output must check it to make sure its not '' or any type thats not a string
async def commandEcho(message):
    #await sendMessage(message.channel, ' '.join(message.content[1:]))
    await message.channel.send(message.content[message.content.find(' '):])


