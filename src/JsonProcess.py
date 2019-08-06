import json
from pygal.maps.world import COUNTRIES
import pygal.maps.world


def get_country_code(country_name):
    """
    :param country_name: 國家名
    :return: 國家代碼 或 None
    """
    for dictCode, dictName in COUNTRIES.items():
        if dictName == country_name:
            return dictCode
    return None


fn = "resource/file/populations.json"
with open(fn) as fnObj:
    try:
        getDatas = json.load(fnObj)
        print(getDatas)
    except Exception as e:
        print("json格式錯誤:" + str(e))

dict_data1, dict_data2 = {}, {}
for getData in getDatas:
    if getData["Year"] == "2000":
        countryName = getData["Country Name"]
        countryCode = get_country_code(countryName)
        population = int(float(getData["Numbers"]))
        if countryCode is not None:
            print(countryCode, "：", population)
            if population > 100000000:
                dict_data1[countryCode] = population
            else:
                dict_data2[countryCode] = population
        else:
            print(countryName, "名稱不吻合")

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2000"
""" 不同筆 add 的顏色不一樣"""
# worldMap.add("ch", ["tw", "cn"])
# worldMap.add("ch", ["tw"])
# worldMap.add("ch", ["cn"])
# worldMap.add("tw", {"tw": 1234, "cn": 12, "jp": 999})
worldMap.add("Year 2000 大於 1億", dict_data1)
worldMap.add("Year 2000 小於", dict_data2)
worldMap.render_to_file("out.svg")


if False:
    listObj = [{'Name':'Peter', 'Age':25, 'Gender':'M'}]    # 串列資料元素是字典
    jsonData = json.dumps(listObj)                          # 將串列資料轉成json資料
    print("串列轉換成json的陣列", jsonData)
    print("json陣列在Python的資料類型 ", type(jsonData))
