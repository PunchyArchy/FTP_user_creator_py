import os


def get_sudo_execute(command, sudo_pass):
    """ Прнимает команду и выполняет ее от sudo"""
    sudo_command = get_sudo_command(command, sudo_pass)
    execute_command(sudo_command)


def get_sudo_command(command, sudo_pass):
    """ Возвращает команду, которая будет выполняться с автоматической авторизацией по паролю sudo_pass """
    command = "echo {}|sudo -S {}".format(sudo_pass, command)
    return command


def execute_command(command):
    os.system(command)


def launch(username, sudo_pass):
    """ Основной движок """
    # Создать директорию пользователя
    create_user_folder(username, sudo_pass)
    # Ограничить его директорию
    restrict_user_folder(username, sudo_pass)
    # Даем необходимые полномочия пользователю на запись в подпапку
    give_subfolder_credentials(username, sudo_pass)


def create_user_folder(username, sudo_pass):
    """ Создать папку пользователя """
    command = "mkdir -p /home/{}/ftp/files".format(username)
    get_sudo_execute(command, sudo_pass)


def restrict_user_folder(username, sudo_pass):
    """ Ограничить полномчения в папке пользователя"""
    command = "chown nobody:nogroup /home/{}/ftp".format(username)
    get_sudo_execute(command, sudo_pass)


def give_subfolder_credentials(username, sudo_pass, subfoldername='files'):
    command = "chown -R {}:{} /home/{}/ftp/{}".format(username, username, username, subfoldername)
    get_sudo_execute(command, sudo_pass)
    command = "chmod -R 0770 /home/{}/ftp/{}".format(username, subfoldername)
    get_sudo_execute(command, sudo_pass)