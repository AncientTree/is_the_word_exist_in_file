#2016.8.10


strings = list("「」~！@#￥%……&*（）—+、？《　， 。》；：‘’“”｛｝【】!=")
input_path = r'E:\缺氧.txt'
output_path = r'除换行符的结果.txt'

class desk:
    def __init__(self, path):
        self.text_path = path
        self.text_file = open(self.text_path, 'r', encoding='utf-8')
        self.text_lines = self.text_file.readlines()
        self.text_file.close()      

    def changePath(self, path):
        self.text_path = path
        self.text_file = open(self.text_path, 'r', encoding='utf-8')
        self.text_lines = self.text_file.readlines()
        self.text_file.close()

    def claenLineBreak(self):
        pass

class pen:
    def __init__(self, path, desk):
        self.lines = desk.text_lines
        self.paper = open(path, 'w+', encoding='utf-8')
        self.cleanLineBreak()
        self.writeDown()
        

    def cleanLineBreak(self):
        for index in range(0, len(self.lines)):
            for i in strings:
                self.lines[index]=self.lines[index].replace('\n', '')
                self.lines[index]=self.lines[index].replace(i, '')
            
            #或者self.lines[index]=self.lines[index].strip()
    def writeDown(self):
        self.paper.writelines(self.lines)
        self.paper.close()
        
    def clean_others(lack_word):  #用来清除输出的字符串里面常见的分汉字字符
        temp = []
        strings = list("1234567890qwer―tyuiopas％①②③④／－　dfghjklzx～cvbnm,./;·'×\[]<>?:{}|=-_+!@「」QWERTYUIOPASDFGHJKLZXCVBNM#$%^&*()~！@#￥%……&*（）—+、？《， 。》；：‘’“”｛｝【】")
        for i in lack_word:
            if not i in strings:
                temp.append(i)
        return temp

    def clean_repeat_word(lack_word):   #用来在输出缺少的所有字之前清除list(lack_word)里面重复的，只留一个
        temp = []
        for i in lack_word:
            if not i in temp:
                temp.append(i)
        return temp


a = desk(input_path)

pen = pen(output_path, a)
print(pen.lines[1])
#pen.cleanLineBreak()
#pen.writeDown()
