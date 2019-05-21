import os


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

    print("\n列出所有的檔案")
    for file in os.listdir("."):
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


work_path()

# test_dir()
