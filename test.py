import sys
import pygame
import pygame.freetype
pygame.init()
size=width,height=640,480  # 设置窗口的大小
# print(pygame.display.Info())
screen=pygame.display.set_mode(size)   # 将窗口显示到屏幕上
# print(pygame.display.Info())        # 在set_mode前后调用是有区别的
pygame.display.set_caption("Pygame文字绘制")
# color=(0,0,0)     # 设置刷新的颜色
black=0,0,0
GOLD=255,251,0
pos=[230,160]
# 引入字体类型
f1=pygame.freetype.Font(r"C:\Windows\Fonts\simsun.ttc",36)
f1rect=f1.render_to(screen,pos,"世界和平",fgcolor=GOLD,size=50)
"""
这里的ball可以理解为surface对象,对象.get_rect()可以形成一个和对象内切的一个对象
这样就可以方便的使用坐标了
"""
fps=300
fclock=pygame.time.Clock()
speed=[1,1]    # 设置移动的X轴，Y轴的矩形     左上角的坐标是(0,0)
bgcolor=pygame.Color("black")
# 定义一个参数返回0-255之间的一个整数
# a大于255返回255，小于255大于0返回a，小于0返回0
def RGBChannel(a):
    return 0 if a<0 else(255 if a>255 else(int(a)))
# clock=pygame.time.Clock()     # 设置时钟
"""
运行上述代码，会出现一个一闪而过的黑色窗口，这是因为程序执行完成后，会自动关闭，如果让窗口一直显示，需要
使用while True让程序一直执行，此外，还需要设置关闭按钮
"""
while True:
     # clock.tick(60)         # 每秒执行60次
    # 检查事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  # 如果单机关闭窗口，则退出
            sys.exit()
        elif event.type==pygame.VIDEORESIZE:
            size=width,height=event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)
    if pos[0]<0 or pos[0]+f1rect.width>width:
        speed[0]=-speed[0]
    if pos[1]<0 or pos[1]+f1rect.height>height:
        speed[1]=-speed[1]
    pos[0]=pos[0]+speed[0]
    pos[1]=pos[1]+speed[1]
    bgcolor.r=RGBChannel(f1rect.left*255/width)
    bgcolor.g=RGBChannel(f1rect.top*255/height)
    bgcolor.b=RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))    # 设置最大速度不能为0，最小为1
    screen.fill(bgcolor)        # 填充颜色
    f1rect=f1.render_to(screen,pos,"世界和平",fgcolor=GOLD,size=50)
    fclock.tick(fps)
    pygame.display.update()     # 更新全部显示