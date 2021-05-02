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
    

def point_generator(st):
    while True:
        for step in range(0, 5, 1):
            num = step
            yield num 
            if step  == 4:
                for i in range(3, 0, -1):
                    num = i
                    yield num
                    if i == 0:
                        step = 0
                        break
    point_position = point_generator(56755)
    time.sleep(0.2)
    return  point_position  


generated_dot = point_generator(1)



def string_assmbler(wn):
    global generated_dot
    dots_place = ['\u2B1B', '\u2B1B', '\u2B1B', '\u2B1B', '\u2B1B']
    count = next(generated_dot)
    for dots_place[count] in range(4):
        dots_place[count] = '\u2B1C'
    num = 0
    while num < 4:
        screen_string1 = str(wn[0][num]) + str(wn[1][num]) + f'{dots_place[0]}' + str(wn[2][num]) + str(wn[3][num]) + f'{dots_place[0]}' + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string2 = str(wn[0][num]) + str(wn[1][num]) + f'{dots_place[1]}' + str(wn[2][num]) + str(wn[3][num]) + f'{dots_place[1]}' + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string3 = str(wn[0][num]) + str(wn[1][num]) + f'{dots_place[2]}' + str(wn[2][num]) + str(wn[3][num]) + f'{dots_place[2]}' + str(wn[4][num]) + str(wn[5][num])  
        num  += 1  
        screen_string4 = str(wn[0][num]) + str(wn[1][num]) + f'{dots_place[3]}' + str(wn[2][num]) + str(wn[3][num]) + f'{dots_place[3]}' + str(wn[4][num]) + str(wn[5][num])
        num  += 1 
        screen_string5 = str(wn[0][num]) + str(wn[1][num]) + f'{dots_place[4]}' + str(wn[2][num]) + str(wn[3][num]) + f'{dots_place[4]}' + str(wn[4][num]) + str(wn[5][num]) 
    clock_face =  screen_string1 + '\n' + screen_string2 + '\n' + screen_string3 + '\n' + screen_string4 + '\n' + screen_string5
    return clock_face 

def string_show_screen(wn):
    print(wn)
    time.sleep(1)
    os.system('cls')