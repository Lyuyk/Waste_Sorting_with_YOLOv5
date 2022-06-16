"""
@author：吕英勤
@license: (C) Copyright 2021-2022, LuiYK.
@software：pycharm
@fileName：show.py
@time:2022/6/5上午 11:51

"""

import matplotlib.pyplot as plt
import numpy as np

list=['AluCan700.jpg','Glass370.jpg','HDPEM959.jpg','PET1715.jpg']
N=2
M=2
#形成NxM大小的画布
for i in range(4):#有27张图片
    path=list[i]
    img = plt.imread(path)
    plt.subplot(N,M,i+1)#表示第i张图片，下标只能从1开始，不能从0，
    plt.title(list[i])

    plt.imshow(img)
    #下面两行是消除每张图片自己单独的横纵坐标，不然每张图片会有单独的横纵坐标，影响美观
    #plt.xticks([])
    #plt.yticks([])
plt.show()
