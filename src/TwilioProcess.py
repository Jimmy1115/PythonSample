from twilio.rest import Client
import json


fn = "resource/file/twilioSid.json"
with open(fn) as fnObj:
    try:
        getDatas = json.load(fnObj)
        print(getDatas)
    except Exception as e:
        print("json格式錯誤:" + str(e))

accountSid = getDatas["accountSid"]
authToken = getDatas["authToken"]

client = Client(accountSid, authToken)
message = client.messages.create(
    from_="+16302803469",
    to="+886933077714",
    body="第二次測試"
)
