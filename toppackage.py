
import base64
import os

from PyInstaller.__main__ import run

def package():
    basePath = os.path.abspath(__file__)
    print(basePath)
    basePath = basePath[:basePath.rfind("\\")]
    print(basePath)
    
    opts = [
        # 字符串前加“r”，防止字符转义
        '--clean',
        # -F, –onefile 打包一个单个文件
        '-F',
        # 要打包的Python文件
        r'{}\\main.py'.format(basePath),
        # # -w 不使用窗口
        # '-w',
        # --icon 指定exe文件的图标
        r'--icon',r'{}\\web_dist\\favicon.ico'.format(basePath),
        
        # --upx-dir 使用upx压缩
        # r'--upx-dir', 'upx393w',
        # --add-data 指定要包含的资源文件。
        # “C:\Windows\System32\sciter.dll”为资源文件原本所在路径（source）。
        # “.”为相对于exe文件的路径（destination），在这里“.”为同一目录的意思。
        # source路径与destination路径以英文状态下分号“;”隔开。
        # r'--add-data', 'C:\Windows\System32\sciter.dll;.', 
        
        # r'--add-binary', r'{}\templates;templates'.format(base),
        r'--add-binary', r'{}\\web_dist;web_dist'.format(basePath),
        # r'--add-binary', r'{}\autoit;autoit'.format(base),
        # r'--add-data', r'{}\templates;templates'.format(base),
        
        r'--add-data', r'{}\\web_dist;web_dist'.format(basePath),
        # r'--add-data', r'{}\autoit;autoit'.format(base)
        # 
        #        # 指定exe名称
        r'--name', "myapp"
    ]
    run(opts)
    
if __name__ == '__main__':
    package()
