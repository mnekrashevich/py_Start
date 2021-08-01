# coding=utf8


with open('001.txt','w') as f_obj:
    while True:
        my_str = input('Для завершения ввода пустая строка :')
        if my_str:
            f_obj.write(my_str + '\n')
        else:
            break