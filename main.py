import eel
import htmltopdf

# 定义html文件所在文件夹名称
eel.init('web')

@eel.expose # 使用装饰器,类似flask里面对路由的定义
def py_fun(url,pdfName,outPath):
    # content = '你好！' + a
    result = htmltopdf.buildpdf(url,pdfName,outPath)
    print(result)
    return("生成成功")

@eel.expose # 使用装饰器,类似flask里面对路由的定义
def batch(filePath,outPath):
    htmltopdf.impExcle(filePath,outPath)
    return ("生成成功")

# 测试调用js中的函数,同样需要使用回调函数
js_return = eel.js_fun('python传过去的参数')(lambda x: print(x))

# 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
eel.start('main.html', port=0, size=(1200,600))

# pyinstaller -D -p D:\workTools\python3.9\Lib -i web/favicon.ico mian.py
# python -m eel [your_main_script] web
# python -m eel main.py web --noconsole