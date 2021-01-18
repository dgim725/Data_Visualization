import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

labels = ['한국디지털미디어고등학교','선린인터넷고등학교','한세사이버보안고등학교','세명컴퓨터고등학교']
ratio = [621,904,364,630]
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
explode = [0,0,0.20,0]
wedgeprops={'width':0.7, 'edgecolor':'w', 'linewidth' :5}

plt.pie(ratio,labels=labels, autopct='%d%%', shadow=True, startangle=90, colors=colors, explode=explode, wedgeprops=wedgeprops)
title = '4개의 고등학교 학생 비율 (100%)'
plt.title(title)
plt.show()