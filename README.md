# simulate-gravity
- 开发进度：0.1.2

前言：

重构代码ing...

#### Releases：


说明:打包release版本因为打包python，文件量很大，运行程序是main.exe，推荐自主安装python和pygame easygui matplotlib第三方库，直接运行代码



这是一个基于Python的2D平面内的宇宙模拟工具

应用原理：

每一个循环内，假设其时间间隔无限短，那么可以对当前状态进行计算，计算每个星球对当前对象的引力，然后分别分解到X轴，Y轴方向从而计算出坐标轴方向的加速度与位移，从而做到近似模拟天体运动的效果。

### Features

- [x] 可允许用户调整时间步长
- [x] 可允许用户修改某个星球的数据
- [x] 可允许用户添加星球
- [x] 可允许用户修改星球的图片
- [x] 添加运动图像、速率图像
- [ ] 可允许开启碰撞模式（可选择性开发）

特别说明:为保证演示的效果，万有引力常数放大1e10倍
