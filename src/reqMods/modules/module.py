from reqMods.modules.command import Command
from reqMods.modules.daemon import Daemon

class Module:
    def __init__(self, name, module, config):
            self.name = name
            self.module = module
            self.config = config

            self.prefix = self.config["prefix"]["prefix"] if "prefix" in self.config.keys() else None

            self.commands = {}
            self.daemons = {}
            self.paused = False

            self.load_commands()
            self.load_daemons()

            pass

    def load_commands(self):

        if "commands" in self.config.keys():
            for name, config in self.config["commands"].items():
                self.commands[name] = Command(name=name, module=self.module, module_name=self.name, module_prefix=self.prefix, config=config)
                
        pass
    
    def load_daemons(self):

        if "daemons" in self.config.keys():
            for name, config in self.config["daemons"].items():
                self.daemons[name] = Daemon(name=name, module=self.module, module_name=self.name, module_prefix=self.prefix, config=config)
        
        pass
