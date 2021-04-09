""" Модуль для создания ограниченных пользователей FTP (LINUX) """
from ftp_creater_linux import functions


def start():
    username = input('Input new FTP username: ')
    sudo_password = input('Input password for username: ')
    functions.launch(username, sudo_password)
