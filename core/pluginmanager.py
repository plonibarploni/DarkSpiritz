#!/usr/bin/env python3
import os, sys, configparser
from configparser import ConfigParser

if sys.platform == "linux":
    class colors:
        BLACK  = '\33[30m'
        RED    = '\33[31m'
        GREEN  = '\33[32m'
        YELLOW = '\33[33m'
        BLUE   = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE  = '\33[36m'
        WHITE  = '\33[37m'
        BLACKBG  = '\33[40m'
        REDBG    = '\33[41m'
        GREENBG  = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG   = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG  = '\33[46m'
        WHITEBG  = '\33[47m'
        END      = '\33[0m'

else:
    class colors:
        BLACK  = ''
        RED    = ''
        GREEN  = ''
        YELLOW = ''
        BLUE   = ''
        VIOLET = ''
        BEIGE  = ''
        WHITE  = ''
        BLACKBG  = ''
        REDBG    = ''
        GREENBG  = ''
        YELLOWBG = ''
        BLUEBG   = ''
        VIOLETBG = ''
        BEIGEBG  = ''
        WHITEBG  = ''
        END      = ''

def dashboard():
    print(colors.GREEN)
    print("Key:              Value:")
    print("========================\n")
    for key, value in config.items('DEFAULT'):
        pressed = "{0:17s}{1:12s}".format(key,value).upper()
        print(pressed)
    print(colors.END)
    print("If Config Is Already Set Press Enter To Execute Plugin")
    terminal = colors.RED + "[" + colors.END + "plugin" + colors.BLUE + "]" + colors.END
    print("Use set <key> command to set config.")
    term = input(terminal).lower() or "execute"
    if terminal[0:3] == "set":
        if terminal[4:] == "lhost":
            config['DEFAULT']['LHOST'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[0:] == "set lport":
            config['DEFAULT']['LPORT'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[4:9] == "rhost":
            config['DEFAULT']['RHOST'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[4:9] == "rport":
            config['DEFAULT']['RPORT'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[4:12] == "userlist":
            config['DEFAULT']['USERLIST'] = input("\nEnter Directory: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[4:12] == "passlist":
            config['DEFAULT']['PASSLIST'] = input("\nEnter Directory: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif terminal[4:13] == "interface":
            config['DEFAULT']['PASSLIST'] = input("\nEnter Interface: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
    elif terminal[0:7] == "execute":
        pass

class ask():
    for key, value in config.items('DEFAULT'):
        dat = "%s = '%s'" % (key, value)
    exec(dat)

dashboard()
