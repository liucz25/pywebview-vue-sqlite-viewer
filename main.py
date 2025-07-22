
import webview
from webview import screens
from api import API

if __name__ == '__main__':
    screen = screens[0]
    width = screen.width/2
    height = screen.height/2    
    database_filename="fsgl.db"


    api = API(database_filename)
 
    webview.settings = {
                'OPEN_DEVTOOLS_IN_DEBUG': True,
                # 一些其他配置，查文档
    }

# #//打包配置
    window = webview.create_window(
                '我的客户端', './web_dist/index.html', fullscreen=False, width=int(width), height=int(height),js_api=api)
    browser = webview.start(http_server=False, debug=False)
# # 开发配置
    # window = webview.create_window(
    #             '我的应用', './web_dist/index.html', width=int(width)/4, height=int(height)/4, js_api=api)
    # browser = webview.start(debug=True)
