#coding=utf8

def my_replace(my_str, replace_dict):
    for key, value in replace_dict.items():
        my_str = my_str.replace(key, value)
    return my_str

my_dict = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

filename_r = '004.txt'
filename_w = '004_result.txt'
mode_r = 'r'
mode_w = 'w'
with open(filename_r, mode_r, encoding='utf-8') as file_r, open(filename_w, mode_w, encoding='utf-8') as file_w:
    for i_str in file_r.readlines():
        file_w.write(my_replace(i_str,my_dict))