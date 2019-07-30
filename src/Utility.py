import os
import logging
import time

log_file_data = time.strftime("%Y-%m-%d", time.localtime())         # %H:%M:%S
log_file_name = "./errlog/" + log_file_data + "-Log.txt"
# log_file_name = None
# ToolFile.check_dir(log_file_name)
# TODO:調整資料夾檢查
logging.basicConfig(level=logging.DEBUG,         # DEBUG INFO WARNING ERROR CRITICAL
                    format='%(asctime)s - %(levelname)s : %(message)s', filename=log_file_name)


class ToolFile:
    def __init__(self, file_name):  # 建構元
        self.__file_name = file_name

    @staticmethod
    def check_dir(file_name):
        if os.path.exists(file_name):
            logging.info("%s 已存在", file_name)
        else:
            if file_name[-1] == "/" or file_name[-1] == "\\":
                if not os.path.exists(file_name):
                    logging.info("檔案路徑:%s 不存在，建立資料夾", file_name)
                    os.mkdir(os.path.dirname(file_name))
                else:
                    logging.debug("檔案路徑%s 已存在，這裡應該不會進來")
            else:
                dir_name = os.path.dirname(file_name)
                if not os.path.exists(dir_name):
                    logging.info("檔案及資料夾路徑:%s 不存在，建立資料夾:%s", file_name, dir_name)
                    os.mkdir(os.path.dirname(file_name))
                else:
                    logging.info("檔案不存在: %s", file_name)
                    return False
        return True

        """
        try:
            file = open(file_name)
            file.close()
        except FileNotFoundError:
            print("No such file or directory: '%s'" % file_name)
            if os.path.isdir(file_name):
                print("資料夾路徑:", file_name)
            elif os.path.isfile(file_name):
                print("檔案路徑:", file_name)
            else:
                print("檔案路徑異常!!")
                if file_name[-1] == "/":
                    os.mkdir(os.path.dirname(file_name))
        except IsADirectoryError:
            print("Is a directory: '%s'" % file_name)
        except PermissionError:
            print("Permission denied: '%s'" % file_name)
        else:
            print("File is exist: '%s'" % file_name)
        """
