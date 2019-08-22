from PIL import ImageColor
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import qrcode

# color code
if False:
    print(ImageColor.getrgb("#0000ff"))
    print(ImageColor.getrgb("rgb(0, 0 ,255)"))
    print(ImageColor.getrgb("rgb(0%, 0% ,100%)"))
    print(ImageColor.getrgb("Blue"))
    print(ImageColor.getrgb("blue"))

    print()

    print(ImageColor.getcolor("#0000ff", "RGB"))
    print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
    print(ImageColor.getcolor("Blue", "RGB"))
    print(ImageColor.getcolor("#0000ff", "RGBA"))
    print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
    print(ImageColor.getcolor("Blue", "RGBA"))

file_name = "./resource/rushmore.jpg"
# 圖檔的明細資料
if False:
    rush_more = Image.open(file_name)
    print("列出物件型態:", type(rush_more))
    width, height = rush_more.size
    print("高度:%s,寬度:%s" % (width, height))
    print("檔案名稱:", rush_more.filename)
    print("列出物件副檔名:", rush_more.format)
    print("列出物件描述:", rush_more.format_description)
    # rush_more.save("123.png")

if False:
    pict_obj = Image.new("RGBA", (300, 300), "Yellow")
    draw_obj = ImageDraw.Draw(pict_obj)

    # 繪製點
    for x in range(100, 200, 3):
        for y in range(100, 200, 3):
            draw_obj.point([x, y], fill="Green")

    # 外框線
    draw_obj.line([(0, 0), (299, 0), (299, 299), (0, 299), (0, 0)], fill="Black")

    # 繪製右上角美工線
    for x in range(150, 300, 10):
        draw_obj.line([(x, 0), (300, x-150)], fill="Blue")
    # 繪製左下角美工線
    for y in range(150, 300, 10):
        draw_obj.line([(0, y), (y-150, 300)], fill="Blue")

    draw_obj.rectangle((0, 0, 299, 299), outline='Black')       # 影像外框線
    draw_obj.ellipse((30, 60, 130, 100), outline='Black')       # 左眼外框
    draw_obj.ellipse((65, 65, 95, 95), fill='Blue')             # 左眼
    draw_obj.ellipse((170, 60, 270, 100), outline='Black')      # 右眼外框
    draw_obj.ellipse((205, 65, 235, 95), fill='Blue')           # 右眼
    draw_obj.polygon([(150, 120), (180, 180), (120, 180), (150, 120)], fill='Aqua')     # 鼻子
    draw_obj.rectangle((100, 210, 200, 240), fill='Red')        # 嘴

    str_txt = "test"
    draw_obj.text((20, 20), str_txt, fill="Blue")

    str_txt = "測試"
    font_info = ImageFont.truetype("C:\Windows\Fonts\MSJHBD.TTC", 24)
    draw_obj.text((20, 30), str_txt, fill="Blue", font=font_info)
    pict_obj.save("123.png")

code_text = "http://www.deepstone.com.tw"
img = qrcode.make(code_text)
img.save("123.jpg")
