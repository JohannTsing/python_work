"""
文件名: snake_case 
类名: PascalCase
函数名: snake_case
"""
import subprocess
import os
from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
import win32gui
import win32process



def open_software_and_get_window(executable_path: str):
    """通过 subprocess 打开软件。通过 win32gui 查找窗口句柄"""

    """
    title: 打开软件客户端
    description: 根据 %executable_path% 指定的路径打开软件客户端。
    inputs:
        - executable_path (str): 软件路径，eg: "D:/Program Files/GJBrowser/SayHi.exe"
    outputs:
        None
    """

    # 1. 检查输入有效性。
    if not isinstance(executable_path, str) or not executable_path:
        print("错误：软件路径必须是非空字符串。")
        return

    if not os.path.exists(executable_path):
        print(f"错误：指定路径不存在 - {executable_path}")
        return

    if not os.path.isfile(executable_path):
        print(f"错误：指定路径不是一个文件 - {executable_path}")
        return

    # 2. 函数执行逻辑
    try:
        # 使用 subprocess.Popen 来非阻塞地启动应用程序
        process = subprocess.Popen([executable_path])
        print(f"已尝试打开软件：{executable_path}")
        
        # 等待窗口初始化（根据实际启动时间调整）
        time.sleep(3)  

        # 通过进程ID查找窗口句柄
        def callback(hwnd, pid):
            if win32gui.IsWindowVisible(hwnd) and win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
                window_titles.append(hwnd)
            return True
    
        window_titles = []
        win32gui.EnumWindows(callback, process.pid)

        if not window_titles:
            raise RuntimeError("未找到匹配的窗口")
    
        # 返回第一个匹配的窗口句柄
        return window_titles[0]

    except FileNotFoundError:
        print(f"错误：未能找到可执行文件或路径错误 - {executable_path}")
    except Exception as e:
        print(f"打开软件时发生错误：{e}")


def open_software_with_pywinauto(executable_path: str):
    """使用 pywinauto 模块实现打开指定软件并获取窗口对象"""
    # 软件路径（使用原始字符串避免转义问题）
    # exe_path = r"D:/Program Files/GJBrowser/SayHi.exe"
    
    try:
        # 启动应用程序
        app = Application(backend="win32").start(executable_path)
        
        # 等待应用程序初始化（根据实际启动时间调整）
        time.sleep(3)
        
        # 连接到已启动的进程
        # app = Application(backend="win32").connect(path=executable_path)
        # app.connect(process=app.process) 
        # 获取主窗口对象
        # main_window = app.top_window()
        
        # 获取主窗口对象
        #main_window = app.window(title_re=".*", found_index=0)  # 更通用的窗口匹配
        main_window = app.window(class_name="GJBrowser")
        main_window.wait("ready", timeout=5)  # 等待窗口就绪
        
        print(f"成功获取窗口对象: {main_window}")
        print(f"标题: {main_window.window_text()}")
        print(f"类名: {main_window.class_name()}")
        print(f"类型: {main_window.control_type()}")
        
        # 查找 员工编号 控件
        user_name = main_window.child_window(title='员工编号')
        print(f"员工编号: {user_name.window_text()}")
        print(f"类名: {user_name.class_name()}")
        print(f"类型: {user_name.control_type()}")

        # 验证窗口有效性
        if not main_window.exists():
            raise RuntimeError("无法获取有效窗口对象")

        window_handle = main_window.handle
        print(f"窗口句柄: {window_handle}")    
        return app, main_window
        
    except Exception as e:
        raise RuntimeError(f"软件启动失败: {str(e)}")

def print_window_controls(main_window):
    """打印窗口中的所有控件信息，用于调试"""
    try:
        print("\n=== 窗口控件信息 ===")
        main_window.print_control_identifiers(depth=None,filename='a.txt')
        
        print("\n=== 编辑框控件 ===")
        edit_controls = main_window.children(control_type="Edit")
        for i, control in enumerate(edit_controls):
            print(f"编辑框 {i}: {control}")
            
        print("\n=== 按钮控件 ===")
        button_controls = main_window.children(control_type="Button")
        for i, control in enumerate(button_controls):
            print(f"按钮 {i}: {control}")
            
    except Exception as e:
        print(f"获取控件信息失败: {str(e)}")

def safe_close_window(app, window):
    """安全关闭窗口，处理可能出现的确认弹窗"""
    try:
        print("准备关闭窗口...")
        
        # 方法1: 尝试直接关闭窗口（无等待）
        try:
            window.close()
            time.sleep(0.5)  # 给弹窗出现的时间
        except Exception as e:
            print(f"直接关闭失败: {e}")
        
        # 检查是否有弹窗出现
        try:
            confirm_dialog = app.window(class_name="#32770")
            if confirm_dialog:
                print("检测到确认弹窗")
                confirm_dialog.set_focus()
                print("尝试发送回车键确认")
                send_keys("{ENTER}")

            # 查找可能的确认弹窗
            # dialogs = app.windows(title_re=".*确认.*|.*提示.*|.*关闭.*")
            # if dialogs:
            #     print("检测到确认弹窗")
            #     # 确认弹窗通常只有一个，但为了保险起见，还是循环遍历
            #     for dialog in dialogs:
            #         print(f"检测到弹窗: {dialog.window_text()}")
            #         print(f"窗口类名: {dialog.class_name()}")
            #     dialog = dialogs[0]
            #     dialog.set_focus()
            #     # print("尝试发送回车键确认")
            #     # send_keys("{ENTER}")
            #     dialog['确定'].click()

                # 尝试点击确认/是/OK按钮
                # try:
                #     # 常见的确认按钮文本
                #     confirm_buttons = ["确认", "是", "OK", "确定", "Yes"]
                #     for btn_text in confirm_buttons:
                #         try:
                #             dialog.child_window(title=btn_text).click()
                #             print(f"成功点击{btn_text}按钮")
                #             break
                #         except:
                #             continue
                # except:
                #     # 如果找不到按钮，尝试发送回车键
                #     print("尝试发送回车键确认")
                #     send_keys("{ENTER}")
        except Exception as e:
            print(f"处理弹窗时出错: {e}")
        
        # 方法2: 如果还存在，尝试Alt+F4强制关闭
        # time.sleep(1)
        # if window.exists():
        #     print("尝试Alt+F4强制关闭")
        #     window.set_focus()
        #     send_keys("%{F4}")  # Alt+F4
        #     time.sleep(0.5)
            
        #     # 再次检查弹窗
        #     try:
        #         send_keys("{ENTER}")  # 如果有弹窗，发送回车确认
        #     except:
        #         pass
        
        # 方法3: 最后检查，如果窗口仍存在，强制终止进程
        time.sleep(1)
        if window.exists():
            print("窗口仍存在，强制终止进程")
            if app.is_process_running():
                app.kill()
        
        # 验证关闭结果
        time.sleep(1)
        if not window.exists():
            print("窗口已成功关闭")
            return True
        else:
            print("窗口关闭失败")
            return False
            
    except Exception as e:
        print(f"关闭窗口时发生错误: {e}")
        # 最后的保险措施：强制终止进程
        try:
            if app.is_process_running():
                app.kill()
                print("已强制终止进程")
        except:
            pass
        return False

def control_test():
    """测试控件操作"""
    # 启动应用程序
    app = Application(backend="uia").start(r"D:\Program Files\WeChat\[3.9.12.51]\WeChat.exe")
    print(f"app.process : {app.process}")
    # 拿到微信主窗口
    # win_main_Dialog = app.window(class_name='WeChatMainWndForPC')
    win_main_Dialog = app.connect(process=app.process).window()
    print(f"win_main_Dialog.control_type() : {win_main_Dialog.control_type()}")
    # 主窗口下的某个窗口，不管层级的找
    chat_list = win_main_Dialog.child_window(control_type='List', title='会话')
    first = chat_list.items()[0] # 第一个聊天项  列表支持items()，支持循环，支持索引
    print(f"first : {first}")

    # 详情页修改备注操作  parent()和children()都是只往上或往下查找一个层级，所有满足的放进列表
    details_page = win_main_Dialog.child_window(class_name='ContactProfileWnd') # 窗口下的某个窗口
    we_id = details_page.child_window(title="微信号：", control_type="Text").parent().children()[1].window_text() # 窗口的爸爸的第二个儿子的文字
    print(f"we_id : {we_id}")

    alia = details_page.child_window(title="微信号：", control_type="Text").parent().parent().children()[0].children()[0].window_text()
    print(f"alia : {alia}")

    edit_btn = details_page.child_window(title="备   注", control_type="Text").parent().children()[1]
    edit_btn.click_input()
    btn_modify_name_edit = edit_btn
    # 先ctrl+a选中所有然后再type_keys替换
    btn_modify_name_edit.type_keys('^a').type_keys('备注名字', with_spaces=True)

    # descendants查找所有后代中满足的，不管层级，所有满足的放进列表
    btns_list = win_main_Dialog.child_window(control_type='ToolBar').parent().descendants(control_type='Button')
    btns_list[0].click_input()

    # dialog.child_window(title="文件名(N):", auto_id="1148", control_type="Edit")



    
if __name__ == "__main__":

    #control_test()

    test_path = r"D:/Program Files/GJBrowser/SayHi.exe"
    try:
        # 启动软件
        app, window = open_software_with_pywinauto(test_path)
        
        # 操作窗口
        # window.maximize()  # 最大化窗口
        # print("窗口已最大化")
        
        # 等待一段时间
        time.sleep(3)

        # print_window_controls(window)
        
        # 安全关闭窗口
        # safe_close_window(app, window)
        
    except Exception as e:
        print(f"程序执行出错: {e}")
    
    print("程序执行完毕")



