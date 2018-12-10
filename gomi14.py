#! /usr/bin/python
# -*- coding: utf-8 -*-
# To use japanese langeage.

import matplotlib.pyplot as plt

import matplotlib.font_manager
fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/fonts-japanese-gothic.ttf")

plt.plot([1, 2, 3])
plt.title(u"グラフタイトル", fontdict = {"fontproperties" : fontprop})

plt.show()
