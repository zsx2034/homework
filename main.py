import matplotlib.pyplot as plt

# 定义x和y轴的数据
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 9]
z = [1, 2, 3, 4, 5]

# 使用scatter函数绘制散点图
# c参数用于设置点的颜色，edgecolors设置边缘颜色，s设置点的大小
plt.scatter(x, y, c=z, edgecolors='black', s=50)

# 添加标题和坐标轴标签
plt.title('散点图示例')
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 显示图形
plt.show()
