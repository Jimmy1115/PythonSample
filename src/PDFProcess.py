import PyPDF2
"""
PyPDT2
內容是中文可能會出顯亂碼
無法讀取圖表和表格
"""


class PDFProcess:
    def __init__(self, file_name):  # 建構元
        """

        :param file_name:
        """
        self.__file_name = file_name    # __:私有化
        self.__pdf_obj = None;
        self.__pdf_rd = None;
        self.__file_pages = None;       # pdf的總數頁
        self.__file_encrypt = None;     # 檔案是否加密

        # p_obj = open(self.__file_name, "rb")
        # prd = PyPDF2.PdfFileReader(p_obj)
        # file_pages = prd.numPages(0)

    def open_file(self):
        self.__pdf_obj = open(self.__file_name, "rb")
        self.__pdf_rd = PyPDF2.PdfFileReader(self.__pdf_obj)
        self.__file_encrypt = self.__pdf_rd.isEncrypted
        self.__file_pages = self.__pdf_rd.numPages

    def read_pdf_page(self, page):
        page_obj = self.__pdf_rd.getPage(page - 1)
        txt = page_obj.extractText()
        return txt


# from src.PDFProcess import PDFProcess

pdf_process = PDFProcess("travel.pdf")
pdf_process.open_file();
print(pdf_process.read_pdf_page(2))
