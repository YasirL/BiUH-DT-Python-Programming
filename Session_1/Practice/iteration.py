import turtle
import time

# 全局变量设置 - 新增动画速度控制参数
NUM_DISKS = 5  # 盘子数量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PEG_WIDTH = 10
PEG_HEIGHT = 250
DISK_HEIGHT = 20
BASE_WIDTH = SCREEN_WIDTH * 0.8
BASE_HEIGHT = 20
ANIMATION_DELAY = 1.0  # 动画延迟时间（秒），数值越大速度越慢

# 颜色定义
PEG_COLOR = "#8B4513"
BASE_COLOR = "#A0522D"
DISK_COLORS = ["#FF6347", "#4682B4", "#3CB371", "#FFD700", "#9370DB", "#20B2AA", "#FF69B4"]

# 初始化屏幕
screen = turtle.Screen()
screen.title("汉诺塔动画演示")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("#F5F5F5")
screen.tracer(0)  # 关闭自动刷新

# 创建绘图turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# 存储每个柱子上的盘子
pegs = {
    'A': list(range(NUM_DISKS, 0, -1)),  # 初始状态：A柱有所有盘子，从大到小
    'B': [],
    'C': []
}

def draw_peg(pen, x, height):
    """绘制一个柱子"""
    pen.penup()
    pen.goto(x, 0)
    pen.pendown()
    pen.color(PEG_COLOR)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(PEG_WIDTH)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_base(pen):
    """绘制底座"""
    pen.penup()
    pen.goto(-BASE_WIDTH/2, 0)
    pen.pendown()
    pen.color(BASE_COLOR)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(BASE_WIDTH)
        pen.left(90)
        pen.forward(BASE_HEIGHT)
        pen.left(90)
    pen.end_fill()

def draw_disk(pen, x, y, width, disk_num):
    """绘制一个盘子"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    color_index = disk_num % len(DISK_COLORS)
    pen.color(DISK_COLORS[color_index])
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(DISK_HEIGHT)
        pen.left(90)
    pen.end_fill()

def draw_scene():
    """绘制整个场景"""
    pen.clear()
    # 绘制底座
    draw_base(pen)
    
    # 绘制三个柱子
    peg_positions = {
        'A': -SCREEN_WIDTH/4,
        'B': 0,
        'C': SCREEN_WIDTH/4
    }
    for peg in peg_positions:
        draw_peg(pen, peg_positions[peg], PEG_HEIGHT)
    
    # 绘制每个柱子上的盘子
    max_disk_width = BASE_WIDTH / 4
    min_disk_width = max_disk_width / NUM_DISKS
    
    for peg, position in peg_positions.items():
        disks = pegs[peg]
        for i, disk_num in enumerate(disks):
            # 盘子宽度随编号增大而增大
            disk_width = min_disk_width + (disk_num - 1) * (max_disk_width - min_disk_width) / (NUM_DISKS - 1)
            x = position - disk_width / 2 + PEG_WIDTH / 2
            y = BASE_HEIGHT + i * DISK_HEIGHT
            draw_disk(pen, x, y, disk_width, disk_num)
    
    screen.update()
    time.sleep(ANIMATION_DELAY)  # 使用全局变量控制延迟时间

def move_disk(from_peg, to_peg):
    """实际移动盘子的辅助函数（更新数据并刷新画面）"""
    if not pegs[from_peg]:
        return False
    
    # 检查是否可以移动（只有小盘子可以放在大盘子上）
    if pegs[to_peg] and pegs[from_peg][-1] > pegs[to_peg][-1]:
        return False
    
    # 移动盘子
    disk = pegs[from_peg].pop()
    pegs[to_peg].append(disk)
    
    # 刷新画面
    draw_scene()
    return True

# ----------------------
# 以下是需要学生实现的部分
# ----------------------
def move(n, a, b, c):
    """
    汉诺塔移动算法
    n: 盘子数量
    a: 源柱子
    b: 辅助柱子
    c: 目标柱子
    """
    if n == 1:
        # 移动一个盘子从a到c
        move_disk(a, c)
        print(f"{a} --> {c}")
    else:
        # 先把n-1个盘子从a移到b，用c作为辅助
        move(n-1, a, c, b)
        # 把第n个盘子从a移到c
        move(1, a, b, c)
        # 把n-1个盘子从b移到c，用a作为辅助
        move(n-1, b, a, c)
# ----------------------
# 以上是需要学生实现的部分
# ----------------------

def main():
    """主函数"""
    print(f"汉诺塔动画演示（{NUM_DISKS}个盘子）")
    print("移动步骤：")
    
    # 初始绘制
    draw_scene()
    time.sleep(2)  # 初始画面停留2秒（比之前更长）
    
    # 开始移动
    move(NUM_DISKS, 'A', 'B', 'C')
    
    print("移动完成！")
    screen.exitonclick()

if __name__ == "__main__":
    main()
    