from os.path import isfile

print('''本工具可自行输入路径，如E盘根目录的文件“E:\\\\additional_chars.dat”''')
'''
E:\\additional_chars.dat在作为一个字符串打印出来时，显示的是E:\\\\additional_chars.dat
因为在字符串中，'\\'将被认为是字符\（以转义字符的形式存在），也就是说用户看到的是两个斜杠，
他们就只会输入两个斜杠

eg
>>> import os
>>> os.path.isfile(E:\\additional_chars.dat)
SyntaxError: invalid syntax
>>> os.path.isfile(E:\additional_chars.dat)
SyntaxError: invalid syntax
>>> os.path.isfile('E:\additional_chars.dat')
False
>>> os.path.isfile('E:\\additional_chars.dat')
True

E:\\additional_chars.dat

C:\\Users\thexe_000\Documents\GitHub\project_aeii\android\assets\lang\additional_chars.dat

'''
print('请输入文件路径：')
while True:
    file_path = "C:\\Users\\thexe_000\\Documents\\GitHub\\project_aeii\\android\\assets\\lang\\additional_chars.dat"
    if isfile(file_path):
        break
    else :
        print('您输入的并不是一个可用的文件路径，请检查一下是否有输入错误或者全角字符。\n注意，不要用中文输入法输入路径里的符号、英文字母、数字。\n请重新输入路径：')

def clean_others(lack_word):  #用来清除输出的字符串里面常见的分汉字字符
    temp = []
    strings = list("1234567890qwertyuiopasdfghjklzx～cvbnm,./;·'×\[]<>?:{}|=-_+!@「」QWERTYUIOPASDFGHJKLZXCVBNM#$%^&*()~！@#￥%……&*（）—+、？《， 。》；：‘’“”｛｝【】")
    for i in lack_word:
        if not i in strings:
            temp.append(i)
    return temp


while True:
    print('请输入中文字符串：')
    word_stock_file = open(file_path, 'r', encoding='utf-8')
    word_stock_string = word_stock_file.read()
    word_stock_file.close()
    lack_word = []  #用list来记录字库里所没有的字
    
    #print(word_stock_string)
    #print(len(lack_word))

    def clean_repeat_word(lack_word):   #用来在输出缺少的所有字之前清除list(lack_word)里面重复的，只留一个
        temp = []
        for i in lack_word:
            if not i in temp:
                temp.append(i)
        return temp
    def strfy(lack_word):
        lack_word_str = ''
        for i in lack_word:
            lack_word_str = lack_word_str + i
        return lack_word_str
    
    def clean_lack_word(lack_word): #用以清除上面那个list(lack_word)
        times = len(lack_word)
        for i in range(0, times):
            lack_word.pop()

    #下面这几行有在此处错误，但其他场合肯有用场
    """
        def clean_lack_word(lack_word): #用以清除上面那个list
            for i in lack_word:
                lack_word.pop()
    """


    while True:
        word_input_string = input() #每次while循环都要求一个新的字符串，同时防止不停刷屏
        for index_of_input_word in word_input_string:
            count = 0   #用来记录这个字是否（1/0）存在与字库
            for index_of_word_stock in word_stock_string:
                           
                if index_of_word_stock == index_of_input_word:
                    count = 1
            if count == 0:
                    lack_word.append(index_of_input_word)   #如果不存在则添加到lack_word这个list里面
        if len(lack_word) > 0:
            lack_word = clean_repeat_word(lack_word)    #清除list(lack_word)里面重复的，只留一个
            lack_word = clean_others(lack_word)
            if len(lack_word) > 0:
                lack_word_str = strfy(lack_word)
                print("字库里面还没有：")
                print('%s' %lack_word_str)
                clean_lack_word(lack_word)      #清空list，否则下一句话也会输出上一句话不存在于字库的字
            else :
                print('这几个字都已经有了啦~')
