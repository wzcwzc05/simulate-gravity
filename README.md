# simulate-gravity
- 开发进度：核心计算部分已完成

这是一个基于Python的2D平面内的宇宙模拟工具

应用原理：

$$
{F} = \frac{{GMm}}{r^2}
$$
每一个循环内，假设其时间间隔无限短，那么可以对当前状态进行计算，计算每个星球对当前对象的引力，然后分别分解到X轴，Y轴方向从而计算出坐标轴方向的加速度与位移，从而做到近似模拟天体运动的效果。

### Features

- [ ] 可允许用户调整时间步长
- [ ] 可允许用户修改某个星球的数据
- [ ] 可允许用户添加星球
- [ ] 可允许用户修改星球的图片
- [ ] 可允许开启碰撞模式（可选择性开发）

