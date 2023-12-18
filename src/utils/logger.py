from rich.console import Console
from rich.theme import Theme
from .timestamp import gen_timestamp

class Logger:
    leveldict = {
            "fatal": 0,
            "error": 1,
            "warn": 2,
            "info": 3,
            "debug": 4
        }

    def __init__(self, name, color, loglevel=3):
        self.name = name
        self.theme = Theme({
            "fatal": "bold #003049",
            "error": "bold #D62828",
            "warn": "bold #F77F00",
            "info": "bold #FCBF49",
            "debug": "bold #EAE2B7",
            "name": f"bold {color}",
            "text": "#F5F2E3",
            "debugtext": "dim #F5F2E3",
        })
        self.console = Console(theme=self.theme)
        self.currentlevel = loglevel
        self.log("debug", "Logger initialized")

    def log(self, level, *args):
        level = self.leveldict[level.lower()]
        timestamp = gen_timestamp()

        match level:
            case 0:
                prefix = f"{timestamp} [fatal]FTL[/fatal] @ [name]{self.name}[/name]:"
            case 1:
                prefix = f"{timestamp} [error]ERR[/error] @ [name]{self.name}[/name]:"
            case 2:
                prefix = f"{timestamp} [warn]WRN[/warn] @ [name]{self.name}[/name]:"
            case 3:
                prefix = f"{timestamp} [info]INF[/info] @ [name]{self.name}[/name]:"
            case 4:
                prefix = f"{timestamp} [debug]DBG[/debug] @ [name]{self.name}[/name]:"

        if level <= self.currentlevel:
            if level < 4:
                self.console.print(prefix, f"[text]{' '.join([*args])}[/text]")
            else:
                self.console.print(prefix, f"[debugtext]{' '.join([*args])}[/debugtext]")
    
    def set_level(self, level):
        self.currentlevel = level
        self.log("debug", f"Log level set to {level}")
        