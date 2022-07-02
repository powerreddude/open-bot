class Daemon:
    def __init__(self, name, module, module_name, module_prefix, config):
        self.name = name
        self.module = module
        self.module_name = module_name
        self.module_prefix = module_prefix
        self.config = config

        self.target = self.config["target"]
        self.dm = self.config["dm"] if "dm" in self.config.keys() else False
        pass

    async def call(self, message):
        await getattr(self.module, self.target)(message)