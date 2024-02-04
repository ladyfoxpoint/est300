
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os

from .logger import Logger

class Plot:
    def __init__(self, estat):
        self.logger = Logger('plot', '#FFB344')
        self.estat = estat
        pass


    def column(self, data, title, label, step, filename):
        sns.set_theme(style="ticks")
        fig, ax = plt.subplots(figsize=(9, 9))
        
        palette = sns.color_palette("blend:#99c4ff,#036bfc", n_colors=len(data))
        
        ax.bar(data.keys(), data.values(), color=palette)

        ax.set_title(title, y=-0.12)
        ax.set_ylabel(label)
        ax.tick_params(axis='y')

        plt.yticks(np.arange(0, max(data.values())+1, float(step)))
        sns.despine(fig)

        plt.savefig(f'{os.path.join(os.getcwd(), "output", filename)}.png')


    def pie(self, data, title, filename):

        # Fix data = 0
        data = {k: v for k, v in data.items() if v != 0}


        sns.set_theme(style="ticks")
        fig, ax = plt.subplots(figsize=(9, 9))
        
        palette = sns.color_palette("blend:#99c4ff,#036bfc", n_colors=len(data))

        ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140, colors=palette)
        ax.set_title(title, y=-0.12)
        
        sns.despine(fig)

        plt.savefig(f'{os.path.join(os.getcwd(), "output", filename)}.png')


    def bar(self, data, title, label, step, filename):
        sns.set_theme(style="ticks")
        fig, ax = plt.subplots(figsize=(9, 9))
        
        palette = sns.color_palette("blend:#99c4ff,#036bfc", n_colors=len(data))
        
        
        sns.barplot(x=data.values(), y=data.keys(), hue=data.keys(), palette=palette)
        
        ax.set_title(title, y=-0.12)
        ax.set_xlabel(label)
        ax.tick_params(axis='x')

        plt.xticks(np.arange(0, max(data.values())+1, float(step)))
        sns.despine(fig)

        plt.savefig(f'{os.path.join(os.getcwd(), "output", filename)}.png')


    def hist(self, data, title, label, step, filename):
        sns.set_theme(style="ticks")
        fig, ax = plt.subplots(figsize=(9, 9))

        palette = sns.color_palette("blend:#99c4ff,#036bfc", n_colors=len(data))

        sns.histplot(x=data.keys(), weights=data.values(), hue=data.values(), multiple="stack", palette=palette, legend=False)
        
        ax.set_title(title, y=-0.12)
        ax.set_ylabel(label)
        ax.tick_params(axis='y')

        plt.yticks(np.arange(0, max(data.values())+1, float(step)))

        sns.despine(fig)

        plt.savefig(f'{os.path.join(os.getcwd(), "output", filename)}.png')
