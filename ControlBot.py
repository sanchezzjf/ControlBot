import os
import subprocess
import webbrowser


print("Hello I'm CommanderBot, to know how I work type 'help me'")
print("")

def ping(task):
    os.system("ping "+task)

def killProcess(process):
    os.system("taskkill /f /im "+process)

def helpMe():
    print('')
    print( 'Here are all the things I can do.')
    print("Just remember that I'm still in development.")
    print('')
    print("open <app-name>      -opens an app |ex: open notepad")
    print("open <site-url>      -opens the site |ex: open youtube.com")
    print("kill <task>          -closes the task |ex: kill notepad")
    print("ping <ip-address>    -pings the IP")
    print("help me              -opens this guide")
    print('')

def openSomething(app):
    print('Opening...')
    chromedir = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' ##windows usa UNIX-like path, entao usa / e nao \
    try:
        subprocess.Popen(app)
    except:
        app = str.replace(app, '.exe', '')
        webbrowser.get(chromedir).open(app)

def prompt():
    try:
        command, task = input('Commander >> ').split()
        
        if command == 'kill':
            task += '.exe'
            killProcess(task)
        
        elif command == 'open':
            task += '.exe'
            openSomething(task)
        
        elif command == 'help':
            helpMe()
        
        elif command == 'ping':
            ping(task)

        else:
            print('')
            print("Sorry, I can't do this, try another command.")
            print('')

    except ValueError as error:
        print(error)
        prompt()

while True:
    prompt()
