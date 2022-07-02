from reqMods.modules.controller import controller

async def commandPause(message):

    module_name = message.content.split(" ")[1]

    controller.pause(module_name)

    pass

async def commandReload(message):

    module_name = message.content.split(" ")[1]

    controller.reload(module_name)

    await message.channel.send(f"Reloaded {module_name}")

    pass

async def commandList(message):

    content = ""

    for name in controller.modules.keys():
        content += name + "\n"

    await message.channel.send(content)
    pass