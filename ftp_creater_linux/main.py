""" Модуль для создания ограниченных пользователей FTP (LINUX) """
from ftp_creater_linux import functions


def start():
    username = input('Input new FTP username: ')
    userpass = input('Input password for username: ')
    sudopass = input('Inuput your sudo password: ')
    functions.launch(username, userpass, sudopass)
