from datetime import datetime

class c:
    escape_char = "\033"
    BLACK = f"{escape_char}[30m"
    RED = f"{escape_char}[31m"
    GREEN = f"{escape_char}[32m"
    YELLOW = f"{escape_char}[33m"
    BLUE = f"{escape_char}[34m"
    MAGENTA = f"{escape_char}[35m"
    CYAN = f"{escape_char}[36m"
    WHITE = f"{escape_char}[37m"
    RESET = f"{escape_char}[0m"
    BOLD = f"{escape_char}[1m"

class Logger:

    @classmethod
    def debug_command(csl, message, command):
        output = f"""\n
{c.BOLD}{c.MAGENTA if message.channel.type.name != "private" else c.YELLOW}{message.guild.name if message.channel.type.name != "private" else "DM"}{c.RESET}({message.guild.id if message.channel.type.name != "private" else None}){c.BOLD}>{c.MAGENTA}{message.channel if message.channel.type.name != "private" else message.author.name}{c.RESET}({message.channel.id})

{c.BOLD}{message.author}{c.RESET} ({message.author.id})\t\t({datetime.now().date()} {datetime.now().time()})
    {c.BLUE}{message.content}{c.RESET}\n    """

        output += "│"

        output += " " * (len(command.module_prefix) - 1)
        
        output += "│"

        output += " " * (len(message.content[0]) - len(command.module_prefix))

        output += "\n    │"

        output += " " * (len(command.module_prefix) - 1)
        
        message_start_len = message.content.find(" ") if message.content.find(" ") != -1 else len(message.content)

        output += f"└─{message.content[:message_start_len].lstrip(command.module_prefix)} targeted: {command.target}"
        
        output += "\n    │"

        output += f"\n    └─module: {command.module_name}"

        print(output)