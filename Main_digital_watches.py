from watch_numbers import numbers
from watch_functions import current_time, time_position_detecter, position_to_number, point_generator, string_assmbler, string_show_screen, generated_dot
import datetime, os, time






def main():
    while True:
        curr_time = current_time()              #текущее время в строке
        time_numbers = time_position_detecter(curr_time)           # раскидали время в переменные int
        watch_numbers = position_to_number(time_numbers)
        #show_watch_numbers(watch_numbers)       # старый вариант, сейчас так никто не делает
        show_strings = string_assmbler(watch_numbers)
        string_show_screen(show_strings)            #печатаем строку
        

main()