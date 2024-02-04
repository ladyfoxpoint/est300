from .timestamp import get_timestamp


log_levels = {
    'debug': 'dbg',
    'info': 'inf',
    'warning': 'wrn',
    'error': 'err',
    'critical': 'crt',
}

enum_level = {
    "dbg": 1,
    "inf": 2,
    "wrn": 3,
    "err": 4,
    "crt": 5,
    "unk": 6
}

class Logger:
    def __init__(self, name, color, level=2):
        self.name = name
        self.color = self._hex_to_rgb(color)
        self.locklevel = level
    
    def log(self, level, text):
        try:
            level = log_levels[level.lower()]
        except:
            level = 'unk'
        
        if  self.locklevel > enum_level[level]:
            return
        
        
        message = ""

        match level:
            case 'dbg':
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#335C67', level)} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"
            case 'inf':
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#FFF3B0', level)} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"
            case 'wrn':
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#E09F3E', level)} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"
            case 'err':
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#9E2A2B', level)} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"
            case 'crt':
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#540B0E', level)} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"
            case _:
                message = f"{self.colorize('#EDFBFF', get_timestamp())} {self.colorize('#EDFBFF', 'unk')} @ {self.colorize(self.color, self.name)}: {self.colorize('#E6E6E6', text)}"

        print(message)

        # print(f"{self.colorize("", get_timestamp())} {self.colorize("", level)} @ {self.colorize(self.color, self.name)}: {message}")


    def colorize(self, color, text):
        if type(color) == str:
            color = self._hex_to_rgb(color)
        return f"\033[38;2;{';'.join(str(i) for i in color)}m{text}\033[0m"

    def _hex_to_rgb(self, hex_code):
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
