import smtplib
from email.mime.text import MIMEText


from_addr = "turncloudtest@gmail.com"                       # 寄件人
pwd = input("請輸入 %s 的密碼:" % from_addr)            # 發信用人的帳號密碼
to_addr_list = ["jimmy-ch@yahoo.com.tw"]                # 收件人

if True:    # 帶有中文的處理方式
    # msg = MIMEText("mail的內容帶有中文的處理方式", "plain", "utf-8")        # 第二個參數，參考 26-14
    # 定義HTML文件
    htmlstr = """
    <!doctype html>
    <html>
    <head>
       <meta charset="utf-8">
       <title>ch3_1.html</title>
    </head>
    <body>
    李白    月下獨酌
    花間一壺酒，
    獨酌無雙親；
    舉杯邀明月，
    對影成三人。
    </body>
    </html>
    """
    msg = MIMEText(htmlstr, 'html', 'utf-8')
    msg["subject"] = "中文 mail test"
    msg["From"] = "俊"
    msg["To"] = "me"
    msg["cc"] = "測試"
else:
    msg = "subject: mail test\n\
    From: Jimmy\n\
    To: J\n\
    Cc: m\n\
    Jimmy test"                  # mail 主旨和內容

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)            # 587 ：TLS 連結埠號
# mySMTP = smtplib.SMTP_SSL("xxx.xxx.xxx", 465)           # 465 ：SSL 連結埠號
mySMTP.ehlo()                                           # 啟動對話
mySMTP.starttls()                                       # 執行TLS加密

mySMTP.login(from_addr, pwd)
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 中文的處理方式 mag => msg.as_string()
if status == {}:                                        # 成功會是 {}
    print("發送mail成功")
else:
    print("發送mail失敗")

mySMTP.quit()


