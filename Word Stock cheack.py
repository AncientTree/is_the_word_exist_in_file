print('''本工具只查“E:\\additional_chars.dat”''')
while True:
    print('请输入中文字符串：')
    print('tip:输入三个q退出')
    word_stock_file = open('E:\\additional_chars.dat')
    word_stock_string = word_stock_file.read()
    lack_word = []  #用list来记录字库里所没有的字
    
    #print(word_stock_string)
    #print(len(lack_word))
    
    def clean_lack_word(lack_word): #用以清除上面那个list
        times = len(lack_word)
        for i in range(0, times):
            lack_word.pop()

    #下面这几行有在此处错误，但其他场合肯有大用场
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
            print("字库里面还没有")
            print('%s' %lack_word)
            clean_lack_word(lack_word)      #清空list，否则下一句话也会输出上一句话不存在于字库的字
