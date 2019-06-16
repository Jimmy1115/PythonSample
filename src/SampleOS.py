import os
import glob     # 可使用萬用字元, (*,?)
import zipfile
import logging

# logging.disable(logging.DEBUG)  # 停用logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s : %(message)s")
# logging.basicConfig(filename="debugLOG.txt",level=logging.DEBUG, format="%(asctime)s - %(levelname)s : %(message)s")    # log 輸出至檔案


def work_path():
    print("目前工作目錄:" + os.getcwd())

    print("絕對路徑:" + os.path.abspath("."))
    print("絕對路徑:" + os.path.abspath(".."))
    print("絕對路徑:" + os.path.abspath("SampleOS"))

    print("特定路段的對相路徑:" + os.path.relpath("C:\\"))
    print("特定路段的對相路徑:" + os.path.relpath("C:\\Users\\Jimmy Chen\\IdeaProjects\\PythonSample"))
    print("特定路段的對相路徑:" + os.path.relpath("C:\\", "SampleOS"))

    # 這裡 print 如果要用 + 號串，需要轉型成 str ； 因為 exists 的型態是 boolean
    print("檔案或目錄是否存在:" + str(os.path.exists("C:/Users/Jimmy Chen/IdeaProjects/PythonSample/src/SampleOS.py")))
    print("檔案或目錄是否無絕對路徑:" + str(os.path.isabs("C:/Users/Jimmy Chen/IdeaProjects/PythonSample/src/SampleOS.py")))
    print("是否為目錄:" + str(os.path.isdir("C:/Users/Jimmy Chen/IdeaProjects/PythonSample/src")))
    print("是否為檔案:" + str(os.path.isfile("C:/Users/Jimmy Chen/IdeaProjects/PythonSample/src/SampleOS.py")))

    print("SampleOS" + " 的檔案大小:", os.path.getsize("SampleOS.py"))

    for dirName, sub_dirName, fileName in os.walk("C:/Users/Jimmy Chen/IdeaProjects/PythonSample"):
        print("目前工作目錄名稱", dirName)
        print("目前子目錄名稱串列", sub_dirName)
        print("目前檔案名稱串列", fileName, "\n")

    print("\n列出所有的檔案")
    for file in os.listdir("."):
        print(file)

    print("\n使用 glob 列出所有的檔案")
    for file in glob.glob('Sample??.py'):
        print(file)


def test_dir():

    dir_path = "testDir"

    if os.path.exists(dir_path):
        print(dir_path + " 已經存在")
        del_flag = input("是否要刪除:" + dir_path + "\n")

        if del_flag == "Y" or del_flag == "y":
            os.rmdir(dir_path)
    else:
        print("建立:" + dir_path )
        os.mkdir(dir_path)


def test_file_read():
    logging.debug("test")

    if False:
        fn = "test.txt"
        file_obj = open(fn)
        data = file_obj.read()
        file_obj.close()
        print(data)

    # 使用 with 開啟檔案可以不用關檔
    if True:
        fn = "test.txt"
        try:
            with open(fn) as file_obj:
                data = file_obj.read()
        except FileNotFoundError:
            print(fn, " 檔案不存在")
            # file_obj.close()
        else:   # 如果正當才執行
            print(data.rstrip())    # 去除最後面的空行
            word_list = data.split()
            print(fn, " 內容字數: ", len(word_list))

            data_str = ''
            for line in data:
                data_str += line.rstrip()
            print(fn, " 內容字數: ", len(data_str))
            print(data_str)

    if False:
        fn = "test.txt"
        with open(fn) as file_obj:
            for line in file_obj:
                print(line.rstrip())    # 去除每行的換行

    if False:
        fn = "test.txt"
        with open(fn) as file_obj:
            obj_list = file_obj.readlines()     # 讓檔案內容可以在 with 以外的地方用

        for line in obj_list:
            print(line.rstrip())


def test_file_write():
    fn = "write.txt"
    data = "I love Python"
    with open(fn, "w") as file_obj:
        file_obj.write(data)


# import zipfile
def test_zipfile():
    # 加壓縮
    if False:
        file_zip = zipfile.ZipFile("../out.zip", 'w')
        file_path = "C:/Users/Jimmy Chen/IdeaProjects/PythonSample/src/*"
        for name in glob.glob(file_path):
            file_zip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        file_zip.close()
    # 讀壓縮檔
    if False:
        file_zip = zipfile.ZipFile("../out.zip", 'r')
        print(file_zip.namelist(), "\n")

        for info in file_zip.infolist():
            print(info.filename, info.file_size, info.compress_size, info.date_time)
    # 解壓縮
    if True:
        file_zip = zipfile.ZipFile("../out.zip")
        file_zip.extractall("../out_dir")
        file_zip.close()


# work_path()

# test_dir()

test_file_read()

# test_file_write()

# test_zipfile()

