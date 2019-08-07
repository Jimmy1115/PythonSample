import smtplib


mySMTP = smtplib.SMTP("smtp.gmail.com", 587)            # 587 ：TLS 連結埠號
# mySMTP = smtplib.SMTP_SSL("xxx.xxx.xxx", 465)           # 465 ：SSL 連結埠號
msg = mySMTP.helo()

mySMTP.quit()

print(type(mySMTP))
print(msg)

