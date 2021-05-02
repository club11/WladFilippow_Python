import datetime, os, time
from watch_numbers import numbers




def current_time():
    current_time_show = datetime.datetime.now()
    str_time = current_time_show.strftime('%H: %M: %S')
    return str_time


def time_position_detecter(curr_time):
    for i in curr_time:
        first_hour = int(curr_time[0]) 
        second_hour = int(curr_time[1]) 
        first_minutes = int(curr_time[4]) 
        second_minutes = int(curr_time[5]) 
        first_seconds = int(curr_time[8]) 
        second_seconds = int(curr_time[9]) 
        position = [first_hour, second_hour, first_minutes, second_minutes, first_seconds, second_seconds]
    return position

def position_to_number(pos):
    global numbers
    first_watch_number = numbers[pos[0]]
    second_watch_number = numbers[pos[1]]
    first_minutes_number = numbers[pos[2]]
    second_minutes_number = numbers[pos[3]]
    first_secs_number = numbers[pos[4]]
    second_secs_number = numbers[pos[5]]
    watch_numbers = [first_watch_number, second_watch_number, first_minutes_number, second_minutes_number, first_secs_number, second_secs_number]               #словарь или список....
    return watch_numbers
    


def string_assmbler(wn):
    num = 0
    while num < 4:
        screen_string1 = str(wn[0][num]) + str(wn[1][num]) + str(wn[2][num]) + str(wn[3][num]) + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string2 = str(wn[0][num]) + str(wn[1][num]) + str(wn[2][num]) + str(wn[3][num]) + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string3 = str(wn[0][num]) + str(wn[1][num]) + str(wn[2][num]) + str(wn[3][num]) + str(wn[4][num]) + str(wn[5][num])  
        num  += 1  
        screen_string4 = str(wn[0][num]) + str(wn[1][num]) + str(wn[2][num]) + str(wn[3][num]) + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string5 = str(wn[0][num]) + str(wn[1][num]) + str(wn[2][num]) + str(wn[3][num]) + str(wn[4][num]) + str(wn[5][num]) 
    clock_face =  screen_string1 + '\n' + screen_string2 + '\n' + screen_string3 + '\n' + screen_string4 + '\n' + screen_string5
    return clock_face

def string_show_screen(wn):
    print(wn)
    time.sleep(1)
    os.system('cls')


'''
def show_watch_numbers(wn):
    num = 0
    while num < 4:
        print(wn[0][num],wn[1][num],wn[2][num],wn[3][num],wn[4][num],wn[5][num])
        num  += 1 
        print(wn[0][num],wn[1][num],wn[2][num],wn[3][num],wn[4][num],wn[5][num]) 
        num  += 1 
        print(wn[0][num],wn[1][num],wn[2][num],wn[3][num],wn[4][num],wn[5][num])  
        num  += 1  
        print(wn[0][num],wn[1][num],wn[2][num],wn[3][num],wn[4][num],wn[5][num]) 
        num  += 1 
        print(wn[0][num],wn[1][num],wn[2][num],wn[3][num],wn[4][num],wn[5][num]) 
    return 
'''