#https://www.101computing.net/pomodoro-timer/
from time import sleep
def displayTimer(time):
    while time > 0:
        mins, secs = divmod(time, 60)
        timer = f'{mins}:{secs}'
        print(timer, end='\r')
        sleep(1)
        time-=1
def pomodoroTimer(mins, longBreak, shortBreak):
    task = input('Enther the task you want to work on: ')
    print('Your task:', task)
    checkMarks = 0
    running = True
    while running:
        print(f'Starting pomodoro timer for [{mins}] minutes...')
        displayTimer(mins*60)
        print(f'Hoop! Your {mins} Minutes is up!')
        checkMarks += 1
        if checkMarks == 4:
            print('Take a long break, You deserve it!')
            print(f'Starting your break for [{longBreak}] minutes...')
            displayTimer(longBreak*60)
            print(f'Hoop! your {longBreak} of break is up!')
        else:
            print('Take a short break, You deserve it!')
            print(f'Starting your break for [{shortBreak}] minutes...')
            displayTimer(shortBreak*60)
            print(f'Hoop! your {shortBreak} of break is up!')
        continues = input('Would you like to contine (Y/N)? ').upper()
        running = True if continues == 'Y' else False
    print('Sorry to see you go. Hope you enjoyed our Pomodoro timer!!')

pomodoroTimer(0.2, 0.5, 0.2) #test values :D
