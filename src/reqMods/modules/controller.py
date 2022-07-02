import os
import sys
import importlib
import toml
from reqMods.modules.module import Module




class controller:
    modules = {}
    sys.path.insert(1, os.path.abspath("../mods"))

    """
        loads all modules
    """
    @classmethod
    def loads(cls):
        importlib.invalidate_caches()

        modules_dirs = os.listdir("../mods")
        for module_dir in modules_dirs:
            
            with open(os.path.abspath("../mods/" + module_dir + "/config.toml"), "r") as file:
                config = toml.load(file)
            
            import_str = f"{module_dir}.{module_dir}" if os.path.exists(f"../mods/{module_dir}/{module_dir}.py") else f"{module_dir}.main"

            cls.modules[module_dir] = Module(name=module_dir, module=importlib.reload(importlib.import_module(import_str)), config=config)

        pass

    @classmethod
    def load(cls, module_name):
        importlib.invalidate_caches()

        with open(os.path.abspath("../mods/" + module_name + "/config.toml"), "r") as file:
                config = toml.load(file)
            
        import_str = f"{module_name}.{module_name}" if os.path.exists(f"../mods/{module_name}/{module_name}.py") else f"{module_name}.main"

        cls.modules[module_name] = Module(name=module_name, module=importlib.reload(importlib.import_module(import_str)), config=config)

        pass


    """
        clears all modules
    """
    @classmethod
    def clears(cls):

        cls.modules = {}

        pass

    @classmethod
    def reloads(cls):

        cls.clears()
        cls.loads()

        pass

    @classmethod
    def clear(cls, module_name):

        cls.modules.pop(module_name)

        pass


    @classmethod
    def reload(cls, module_name):

        cls.clear(module_name)
        cls.load(module_name)

        pass

    @classmethod
    def pause(cls, module_name):

        cls.modules[module_name].paused = not cls.modules[module_name].paused

        pass
