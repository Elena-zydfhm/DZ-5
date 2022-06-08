# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк» 

# !!! ВЫПОЛНЕНО СОВМЕСТНО В ГРУППЕ!!!
#def extra_text(text):             # функция проверяет техт на наличие "абв"
#    if not "абв" in text:
#       return True
#text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
#text_list = text.lower().split()   # .lower() переводит текст в нижний регистр
                                   # .split() разбивает текст на список
#clear_text = filter(extra_text,text_list) 

#print(list(clear_text))

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, 
# # причем чтобы сыграть в нее можно было в одиночку.

# from itertools import repeat
# import random
# from random import randint
# import time

# def pause():
#     time.sleep(1)
    

# def raw(raw = None):
#     while True:
#         raw = input('Выберите строку (от 1 до 3) ')
#         if not raw.isdigit() or int(raw) < 1 or int(raw) > 3:
#             print('Вы ввели недопустимое значение, попробуйте снова ')
#         else:
#             print()
#             return int(raw)

# def comp_raw(raw = None):
#     raw = randint(0, 2)
#     return raw
    
# def column(column = None):
#     while True:
#         column = input('Выберите ряд ')
#         if not column.isdigit() or int(column) < 1 or int(column) > 3:
#             print('Вы ввели недопустимое значение, попробуйте снова ')
#         else:
#             return int(column)

# def comp_column(column = None):
#     column = randint(0, 2)
#     return column

# def player_change(raw, column, field):
#       if raw == 1:
#         for i in range(len(field)+1):
#             if column == 1:
#                 field[0][0] = field[0][0].replace('___','_x_')
#             if column == 2:
#                 field[0][1] = field[0][1].replace('___','_x_')
#             if column == 3:
#                 field[0][2] = field[0][2].replace('___','_x_')
#             return field
#       elif raw == 2:
#             for i in range(len(field)+1):
#                 if column == 1:
#                     field[1][0] = field[1][0].replace('___','_x_')
#                 if column == 2:
#                     field[1][1] = field[1][1].replace('___','_x_')
#                 if column == 3:
#                     field[1][2] = field[1][2].replace('___','_x_')
#                 return field
#       elif raw == 3:
#             for i in range(len(field)+1):
#                 if column == 1:
#                     field[2][0] = field[2][0].replace('   ',' x ')
#                 if column == 2:
#                     field[2][1] = field[2][1].replace('   ',' x ')
#                 if column == 3:
#                     field[2][2] = field[2][2].replace('   ',' x ')
#                 return field

# def comp_change(raw, column, field):
#       if raw == 0:
#         for i in range(len(field)):
#             if column == 0:
#                 field[0][0] = field[0][0].replace('___','_0_')
#             if column == 1:
#                 field[0][1] = field[0][1].replace('___','_0_')
#             if column == 2:
#                 field[0][2] = field[0][2].replace('___','_0_')
#             return field
#       elif raw == 1:
#             for i in range(len(field)):
#                 if column == 0:
#                     field[1][0] = field[1][0].replace('___','_0_')
#                 if column == 1:
#                     field[1][1] = field[1][1].replace('___','_0_')
#                 if column == 2:
#                     field[1][2] = field[1][2].replace('___','_0_')
#                 return field
#       elif raw == 2:
#             for i in range(len(field)):
#                 if column == 0:
#                     field[2][0] = field[2][0].replace('   ',' 0 ')
#                 if column == 1:
#                     field[2][1] = field[2][1].replace('   ',' 0 ')
#                 if column == 2:
#                     field[2][2] = field[2][2].replace('   ',' 0 ')
#                 return field
                
# def x_win(field):
#     if (field[0][0] == ('_x_') and field[0][1] == ('_x_') and field[0][2] == ('_x_')):
#         return True
#     elif (field[1][0] == ('_x_') and field[1][1] == ('_x_') and field[1][2] == ('_x_')):
#         return True
#     elif (field[2][0] == (' x ') and field[2][1] == (' x 2') and field[2][2] == (' x ')): 
#         return True
#     elif (field[0][0] == ('_x_') and field[1][1] == ('_x_') and field[2][2] == (' x ')):
#         return True
#     elif (field[0][2] == ('_x_') and field[1][1] == ('_x_') and field[2][0] == (' x ')):
#         return True
#     elif (field[0][2] == ('_x_') and field[1][2] == ('_x_') and field[2][2] == (' x ')):
#         return True
#     elif (field[0][1] == ('_x_') and field[1][1] == ('_x_') and field[2][1] == (' x ')):
#         return True
#     elif (field[0][0] == ('_x_') and field[1][0] == ('_x_') and field[2][0] == (' x ')):
#         return True
#     else:
#         return False

# def o_win(field):
#     if (field[0][0] == ('_0_') and field[0][1] == ('_0_') and field[0][2] == ('_0_')):
#         return True
#     elif (field[1][0] == ('_0_') and field[1][1] == ('_0_') and field[1][2] == ('_0_')):
#         return True
#     elif (field[2][0] == (' 0 ') and field[2][1] == (' 0 ') and field[2][2] == (' 0 ')): 
#         return True
#     elif (field[0][0] == ('_0_') and field[1][1] == ('_0_') and field[2][2] == (' 0 ')):
#         return True
#     elif (field[0][2] == ('_0_') and field[1][1] == ('_0_') and field[2][0] == (' 0 ')):
#         return True
#     elif (field[0][2] == ('_0_') and field[1][2] == ('_0_') and field[2][2] == (' 0 ')):
#         return True
#     elif (field[0][1] == ('_0_') and field[1][1] == ('_0_') and field[2][1] == (' 0 ')):
#         return True
#     elif (field[0][0] == ('_0_') and field[1][0] == ('_0_') and field[2][0] == (' 0 ')):
#         return True
#     else:
#         return False
# def no_win(field):
#     if field[0][0]!= ('___') and field[0][1] != ('___') and field[0][2] != ('___')\
#         and field[1][0] != ('___') and field[1][1] != ('___')and field[1][2] == ('___')\
#         and field[2][0] == ('   ') and field[2][1] == ('   ') and (field[2][2] == ('   ')):
#         return True
# def print_field(field):
#     print(field[0])
#     print(field[1])
#     print(field[2])

# def starting(field,start_raw=0, start_column=0):
#     while True:
#         start_raw = input('Выберите строку (от 1 до 3) ')
#         if not start_raw.isdigit() or int(start_raw) < 1 or int(start_raw) > 3:
#             print('Вы ввели недопустимое значение, попробуйте снова ')
#             print()
#         else:
#             start_raw = int(start_raw)
#             while True:
#                 start_column = input('Выберите ряд (от 1 до 3) ')
#                 if not start_column.isdigit() or int(start_column) < 1 or int(start_column) > 3:
#                     print('Вы ввели недопустимое значение, попробуйте снова ')
#                 else:
#                     start_column = int(start_column)
#                     if(start_raw == 3):
#                         field[start_raw-1][start_column-1] = (' x ')
#                     else:
#                         field[start_raw-1][start_column-1] = ('_x_')
#                     return field

# def player_turn(player):
#     if player == 'Игрока ->':
#        player = 'Компьютера ->'
#        print()
#        print(f'Ход {player }')
#     else:
#         print()
#         player = 'Игрока ->'
#         print(f'Ход {player }')
#     return player

#     print()
# print('Вас приветствует игра Крестики - Нолики. Вы играете против компьютера, Ваш ход первый ')
# print()
# field = ['___','___','___'],['___','___','___'],['   ','   ','   ']
# start = starting(field)
# player = 'Игрока ->'
# print()
# print_field(field)
# player = player_turn(player)
# while True:
#     if player == 'Компьютера ->':
#             if no_win(field):
#                 print('В этой игре - ничья ')
#                 exit(0)
#             else:
#                 comp_change_raw = comp_raw() 
#                 comp_change_column = comp_column()
#             if(field[comp_change_raw][comp_change_column] == ('_x_') or field[comp_change_raw]\
#                 [comp_change_column] == (' x ')) or field[comp_change_raw][comp_change_column]\
#                      == ('_0_') or field[comp_change_raw][comp_change_column] == (' 0 '):
#                 None
#             else:
#                 comp_move = comp_change(comp_change_raw,comp_change_column,field)
#                 pause()
#                 print_field(field)
#                 if o_win(field):
#                     print_field(field)
#                     print('Невероятно, но Вы, к сожалению, проиграли')
#                     exit(0)
#                 else:
#                     player = player_turn(player)
#     else:
#         while True:
#                     change_raw = raw()
#                     change_column = column()
#                     if no_win(field):
#                             print('В этой игре - ничья ')
#                             exit(0)
#                     elif(field[change_raw-1][change_column-1] == ('_x_') or field[change_raw-1]\
#                             [change_column-1] == (' x ')) or field[change_raw-1][change_column-1]\
#                                 == ('_0_') or field[change_raw-1][change_column-1] == (' 0 '):
#                             print('Эта ячейка занята, пожалуйста выберите другую ячейку ')
                    
#                     else:
#                         player_move = player_change(change_raw, change_column, field)
#                         pause()
#                         print_field(player_move)
#                         if x_win(field):
#                             print()
#                             print("Поздравляем, вы победили!")
#                             exit(0)
#                         else:
#                             player = player_turn(player)
#                             break

# Текст

# from encodings import utf_8

# parasites = { 1:'«Ну,', 2:'короче.', 3:'короче,',4:'В',5:'общем,',6:'говоря,',7:'кажется,',
#               8:'кажется.', 9:'Ну,эээ,', 10:'Как', 11:'бы', 12:'эээээ….', 13:'Ясен',14:'ясен',
#               15:'пень', 16:'Кстати,', 17:'Ээээ...короче,', 18:'ээээ…', 19:'короче', 20:'пень.',
#               21:'общем.'}

# def parasites_clear(text, dictionary):
#     new_text = text.copy()
#     for i in range (len(text)):
#         for key in dictionary.keys():
#             if text[i] == dictionary[key]:
#                 new_text.remove(text[i])   
#     return new_text

# with open('task3.txt', 'r', encoding=('utf-8')) as text:
#     bad_text = text.read().split()
# # print(bad_text)
# new_text = ' '.join(parasites_clear(bad_text, parasites))
# print(new_text)










