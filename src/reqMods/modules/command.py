class Command:
    def __init__(self, name, module, module_name, module_prefix, config):
        self.name = name
        self.module = module
        self.module_name = module_name
        self.module_prefix = module_prefix
        self.config = config

        self.command = self.config["command"]
        self.target = self.config["target"]
        self.dm_chats = self.config["dm_chats"] if "dm_chats" in self.config.keys() else False
        self.public_chats = self.config["public_chats"] if "public_chats" in self.config.keys() else True
        self.group_chats = self.config["public_chats"] if "group_chats" in self.config.keys() else False
        pass

    async def call(self, message):
        await getattr(self.module, self.target)(message)
