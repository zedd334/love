from flask import Flask, render_template
import random
import time
import threading

app = Flask(__name__)

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
    '认真生活', '别忘了我', '爱你哟'
]

# 更多背景颜色选择
bg_colors = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
    'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
    'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon',
    'lightcyan', 'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen',
    'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow'
]

# 显示关心提示的 Web 页面
def show_warn_tip():
    tip = random.choice(tips)  # 随机选择一条关心提示
    bg = random.choice(bg_colors)  # 随机选择背景颜色
    return f'''
    <html>
        <head>
            <style>
                body {{
                    background-color: {bg};
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Helvetica, Arial, sans-serif;
                }}
                .popup {{
                    background-color: white;
                    border-radius: 15px;
                    padding: 20px;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                    color: #333;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }}
            </style>
        </head>
        <body>
            <div class="popup">{tip}</div>
        </body>
    </html>
    '''

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 创建并显示弹窗路由
@app.route('/show_tip')
def show_tip():
    return show_warn_tip()

# 启动 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
