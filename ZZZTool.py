import os
import configparser
import webbrowser
import ctypes
import shutil
import subprocess
import msvcrt
import threading

# 将自动启动的选项存储在全局变量中
auto_start = '是'
os.system("title 绝区零官B互换")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def switch_server(server):
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        if server == 'BiliBili':
            dll_path = resource_path('PCGameSDK.dll')
            shutil.copy(dll_path, 'ZenlessZoneZero_Data/Plugins')
            config['general'] = {'channel': '14', 'sub_channel': '0', 'cps': 'zzz_bilibili_pc', 'uapc': '{"hyp":{"uapc":""},"nap_cn":{"uapc":""}}', 'game_version': '1.0.0'}
        elif server == 'Official':
            os.remove('ZenlessZoneZero_Data/Plugins/PCGameSDK.dll')
            config['general'] = {'channel': '1', 'sub_channel': '1', 'cps': 'mihoyo1_PC', 'uapc': '{"hyp":{"uapc":""},"nap_cn":{"uapc":""}}', 'game_version': '1.0.0'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print(f"执行服务器切换操作成功！")
        if auto_start == '是':
            threading.Thread(target=lambda:subprocess.Popen('ZenlessZoneZero.exe')).start()
    except Exception as e:
        print(f"执行服务器切换操作失败：{str(e)}")
        input("按任意键返回主菜单...")
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global auto_start
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("绝区零官B互换")
        print("作者:荷花-MOPELotus")
        print("Github:https://github.com/SummerLotus520/ZZZTool/")
        config = configparser.ConfigParser()
        config.read('config.ini')
        current_server = '官方服务器' if config['general']['cps'] == 'mihoyo1_PC' else 'Bilibili服务器'
        change_server = 'Bilibili服务器' if current_server == '官方服务器' else '官方服务器'
        print(f"[1]服务器切换： {current_server} 转 {change_server}")
        print("[2]重置为官方服务器")
        print("[3]重置为BiliBili服务器")
        print(f"[4]设置是否自动启动游戏：当前设置 {auto_start}")
        print("[5]打开Github页面检查更新")
        print("[6]加入QQ群交流反馈")
        print("[7]退出程序")
        choice = msvcrt.getch().decode('utf-8')
        if choice == '1':
            switch_server('BiliBili' if current_server == '官方服务器' else 'Official')
        elif choice == '2':
            switch_server('Official')
        elif choice == '3':
            switch_server('BiliBili')
        elif choice == '4':
            auto_start = '否' if auto_start == '是' else '是'
            print(f"执行设置自动启动游戏操作成功！")
        elif choice == '5':
            webbrowser.open('https://github.com/SummerLotus520/ZZZTool/')
            print(f"执行打开Github页面操作成功！")
        elif choice == '6':
            webbrowser.open('https://qm.qq.com/cgi-bin/qm/qr?k=LBH0KSX2iQQIkgq-RZjHxLUMGEUJrIdE&jump_from=webapi&authKey=JfdyuvI9z+HkhvKcDVckiB/YuXofzsZx+nRNSzHBrOLacc3dHFg23KyLAyfpy6NQ')
            print(f"执行加入QQ群交流反馈操作成功！")
        elif choice == '7':
            print("退出程序")
            break

if __name__ == "__main__":
    main()
