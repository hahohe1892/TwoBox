#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm

def TwoBox_Plot_TimeSeries(x,y, xaxes_limits, x_label, yaxes_limits, y_label, figure_text, legend_text):
    # colors
    line_colors=[[1, 0, 0],
                 [0, 0, 1],
                 [0, 1, 0],
                 [1, 0.5, 0],
                 [0.5, 0.5, 0], 
                 [0.5, 0, 1], 
                 [0.5, 0.5, 0.5], 
                 [0.5, 0, 0.5],
                 [0.7, 0.5, 0.2], 
                 [0.2, 0.7, 0.7],
                 [0.9, 0.1, 0.9]]

    Line_width=1.5
    
    #font and fontsize
    fntname='Times'
    fnt=12

    legend_labels=[]

    if y.ndim==1:
        p, =plt.plot(x,y, label=legend_text)
    if y.ndim==2:
        for i,data in enumerate(y):
            p=plt.plot(x,data, label=legend_text)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(figure_text)
    if xaxes_limits:
        plt.xlim(xaxes_limits)
    if yaxes_limits:
        plt.ylim(yaxes_limits)
    plt.plot(x,np.zeros(len(x)), '--', color='black')

    return p