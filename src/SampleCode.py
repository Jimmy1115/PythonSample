import time
from src.ExcelProcess import MSExcel


ms_excel = MSExcel("sales.xlsx")
ms_excel.open_file(True)
print(ms_excel.get_row_data())

def test_code():

    def ex_type():
        """ 範例 """
        ex_list = ['test', '123']
        print(type(ex_list))

        ex_tuple = ('test', 123)
        print(type(ex_tuple))

        """
        空集合可以用 ex_dict = {}
        """
        ex_dict = {11: 'jimmy', 22:'test'}
        print(type(ex_dict))

        """ 
        元素不可變(所以元素不可以是list)
        內容不重複
        如果有有重複的元素，會自動刪除
        空集合要用 ex_set = set()
        """
        ex_set = {"test", 123}
        print(type(ex_set))

        ex_set1 = set('aest')
        print(type(ex_set1))
        print(ex_set1)


    def ex():
        print("12312312")
        james = [1, 2, 3, 4, 5, 6]
        g1, g2, g3, g4, g5, g6 = james
        str1 = " Jimmy "
        print("/%s/" % str1)
        str2 = str1.rstrip()
        print("/%s/" % str2)
        print("列印", g1, g2, g3, g4, g5, sep="  ")
        del james[0:6:2]
        print(james)

        fruits = {'西瓜': 100}
        print(fruits["西瓜"])

        seq1 = ['name', 'city']
        seq2 = ['jimmy', 'keelong']
        tup_dict = dict.fromkeys(seq1 , seq2)
        print(tup_dict)


    ex_type()


    def oddfn(x):
        return x if (x % 2 == 1) else None

    mylist = [5, 10, 15, 20, 25]

    fo = filter(oddfn, mylist)
    print([item for item in fo])


    class Bank():
        title = "Taipei Bank"

        def __init__(self, uname, money):
            self.name = uname
            self.__balance = money

        def get_balance(self):
            return self.__balance

        def set_balance(self, money):
            self.__balance += money
            return self.__balance


    aa = Bank("jimmy", 1000)

    print(aa.name.title(), "存款餘額:", aa.get_balance())
    aa.set_balance(200)
    print(aa.name.title(), "存款餘額:", aa.get_balance())
    print(aa.title)
    print(time.localtime())

