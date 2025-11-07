import tkinter as tk
import random
import threading
import time
import signal
import sys

# 用于存储所有创建的窗口
windows = []

def show_warn_tip():
    # 创建窗口
    window = tk.Tk()
    
    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 窗口尺寸扩大1.5倍
    window_width = 270  # 180 * 1.5 = 270
    window_height = 75  # 50 * 1.5 = 75
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    
    # 设置窗口标题和位置
    window.title('关心')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 关心生活健康的话语（30条）
    tips = [
        '好好吃饭', '好好休息', '早点休息', '天天开心',
        '记得喝水', '按时吃饭', '别熬夜了', '照顾好自己',
        '注意身体', '记得运动', '放松一下', '保持微笑',
        '劳逸结合', '别太劳累', '记得午休', '多吃水果',
        '出去走走', '呼吸新鲜空气', '保持好心情', '别久坐',
        '记得早餐', '雅榕记得保护眼睛哦', '注意保暖', '别着凉',
        '保持健康', '平安喜乐', '开心每一天', '一切顺利',
        '万事如意', '心想事成',"每一个微笑都绽放无限温暖！",
        '认真生活', '别忘了我','爱你哟'
    ]
    
    tip = random.choice(tips)
    
    # 更多背景颜色选择
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
        'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon',
        'lightcyan', 'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow'
    ]
    bg = random.choice(bg_colors)
    
    # 创建消息框架
    frame = tk.Frame(window, bg=bg, padx=20, pady=10, relief="solid", bd=2, highlightthickness=0, highlightbackground=bg)
    frame.pack(expand=True, fill=tk.BOTH)
    
    # 设置消息文本
    label = tk.Label(
        frame, 
        text=tip, 
        bg=bg, 
        font=('Helvetica', 16, 'bold'),  # 字体优化，使用更现代的Helvetica字体
        width=20,
        height=2,
        justify="center",
        anchor="center",
        wraplength=240,
        padx=5,
        pady=5
    )
    label.pack(expand=True, fill=tk.BOTH)
    
    # 立即更新窗口显示
    window.update()
    
    # 窗口置顶
    window.attributes('-topmost', True)
    
    # 3秒自动关闭（加快关闭速度，避免长期占用资源）
    window.after(3000, window.destroy)
    
    # 将窗口对象添加到全局列表
    windows.append(window)
    
    window.mainloop()

def exit_program(signal, frame):
    """捕获终止信号，关闭所有窗口并退出程序"""
    print("\n程序终止，正在关闭所有窗口...")
    for window in windows:
        window.destroy()
    sys.exit(0)

if __name__ == "__main__":
    # 捕获 Ctrl+C（KeyboardInterrupt）信号，调用exit_program函数退出
    signal.signal(signal.SIGINT, exit_program)
    
    # 根据屏幕大小计算所需窗口数量（确保铺满）
    window_count = 300  # 减少窗口数量，避免过于密集
    
    # 快速创建窗口（缩短间隔）
    for i in range(window_count):
        t = threading.Thread(target=show_warn_tip)
        t.daemon = True  # 守护线程，主程序退出时自动结束
        t.start()
        time.sleep(0.01)  # 极短间隔，快速创建

    # 保持主程序运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 按Ctrl+C退出
        pass
