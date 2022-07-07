from os import system, name


class misc:
    def getCommand(msg, command, command_list) -> bool:
        if command.lower() in command_list:
            return True
        return False

    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


class glob:
    lang_list = [
        "en",
        "ru"
    ]


class loc:
    welcome = {
        "ru": "Добро пожаловать в рекурсивное судоку!",
        "en": "Welcome to recursive sudoku!"
    }

    game_mode = {
        "ru": "Выберите режим игры (auto, manual): ",
        "en": "Choose the game mode (auto, manual): "
    }