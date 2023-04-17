import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import pyllusion
from tqdm import tqdm

# Muller-Lyerillusion
def dataset02(path, size, positive_ratio):
    label_df = pd.DataFrame(columns=['name', 'label', 'value', 'rotation', 'Top_x1', 'Top_y1', 'Top_x2', 'Top_y2', 'Bottom_x1', 'Bottom_y1', 'Bottom_x2', 'Bottom_y2'])
    for i in tqdm(range(size)):
        label = int(np.random.rand() < positive_ratio) #whether two line equal
        value = 0
        if label != 1:
            while value == 0:
                value = np.random.randint(-500, +500)/1000 # maximum +-1.5 longer
        mullerlyer = pyllusion.MullerLyer(illusion_strength=30, difference=value, distance=np.random.randint(80, 120)/100)
        rotation = np.random.randint(0, 180)
        img = mullerlyer.to_image(width=128, height=128, outline=4).rotate(angle=rotation, fillcolor = (255, 255, 255, 255))
        fn = lambda x : 255 if x > 210 else 0
        img = img.convert("L").point(fn, mode='1')
        dict = mullerlyer.get_parameters()
        name = f"mullerlyer{i}.png"
        img.save(os.path.join(path, name))
        # print(len(label_df) )
        label_df.loc[len(label_df)] = [name, label, value, rotation, dict['Top_x1'],dict['Top_y1'], dict['Top_x2'], dict['Top_y2'], dict['Bottom_x1'], dict['Bottom_y1'], dict['Bottom_x2'], dict['Bottom_y2']]
        
    label_df.to_csv(os.path.join(path, "label.csv"))
    
# Vertical–horizontal illusion
def dataset04(path, size, positive_ratio):
    minL = 1
    scale = 0.5
    
    label_df = pd.DataFrame(columns = ["name", "label", "x_length", "y_length"])
    for i in tqdm(range(size)):
        if np.random.rand() > positive_ratio:
            xl = minL + np.random.rand() * scale
            yl = minL + np.random.rand() * scale
        else:
            xl = minL + np.random.rand() * scale
            yl = xl
        
        if (xl == yl):
            label = 1
        else:
            label = 0

        fig = plt.figure(figsize=(4,4), facecolor='white', dpi = 32)
        ax1 = fig.add_subplot(111, aspect = 'equal')
        ax1.set_axis_off()
        ax1.plot([0, 0], [0, yl], linewidth = 1.3, c = 'black')
        ax1.plot([-xl/2, xl/2], [0, 0], linewidth = 1.3, c = 'black')
        
        name = f'vertical{i}.png'
    
        fig.savefig(os.path.join(path, name))
        
        label_df.loc[len(label_df)] = [name, label, xl, yl]
    label_df.to_csv(os.path.join(path, "label.csv"))
    

# RED YELLOW BOUNDARY
def dataset06(path, size, positive_ratio):
    label_df = pd.DataFrame(columns = ["name", "label", "width", "x", "y", "r", "g", "b"])
    for i in tqdm(range(size)):
        x = np.random.rand() * 43 - 21
        y = np.random.rand() * 43 - 21
        w = np.min([np.abs(x + 32), np.abs(32 - x), np.abs(y + 32), np.abs(32 - y), np.max([np.random.rand() * 64, 11]), 42])

        if np.random.rand() > positive_ratio:
            c = (1, np.random.rand(), 0)
            label = 0
        else:
            c = (1, 0.5, 0)
            label = 1

        fig = plt.figure(figsize=(4,4), facecolor='white', dpi = 16)
        ax1 = fig.add_subplot(111, aspect = 'equal')
        ax1.add_patch(
            patches.Rectangle(
                (x, y),
                width=w,
                height=w,
                color = c
            )
        )
        ax1.set_xlim([-32,32])
        ax1.set_ylim([-32,32])
        ax1.set_axis_off()
        
        name = f'rect{i}.png'
        
        #display figure 
        fig.savefig(os.path.join(path, name))
        
        label_df.loc[len(label_df)] = [name, label, w, x, y, *c]
    label_df.to_csv(os.path.join(path, "label.csv"))


# CLOCK ANGLE
def dataset07(path, size, positive_ratio):
    def limit(x, min, max):
        x = np.max((x, min))
        x = np.min((x, max))
        return x
    def get_angle(v1, v2):
        return v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    
    tolerance = 0 #tolerance 
    angleLimit = 0.1 #maximum angle between two segment
    
    label_df = pd.DataFrame(columns = ["name", "label", "angle", "x1", "y1", "x2", "y2", "x3", "y3"])
    for i in tqdm(range(size)):
        p1 = np.random.rand(2) * 64 - 32
        p2 = np.random.rand(2) * 64 - 32
        if (np.random.rand() > positive_ratio):
            p3 = np.random.rand(2) * 64 - 32
            theta = np.random.rand() * 2 * angleLimit - angleLimit
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))
            p3 = R @ (p2 - p1) * np.random.rand() + p2 
            xl = limit(p3[0], -32, 32) / p3[0]
            yl = limit(p3[1], -32, 32) / p3[1]
            p3 = R @ (p2 - p1) * np.min((xl, yl)) + p2
            label = 0 # FIXME NOT SAFE, TRY DOUBLE CHECK LATER
        else:
            p3 = (p2 - p1) * np.random.rand() + p2 
            xl = limit(p3[0], -32, 32) / p3[0]
            yl = limit(p3[1], -32, 32) / p3[1]
            p3 = (p2 - p1) * np.min((xl, yl)) + p2
            label = 1
        P = np.concatenate([p1[None,:],p2[None,:],p3[None,:]], axis = 0)
        fig = plt.figure(figsize=(4,4), facecolor='white', dpi = 128)
        ax1 = fig.add_subplot(111, aspect = 'equal')
        ax1.set_xlim([-32,32])
        ax1.set_ylim([-32,32])
        ax1.set_axis_off()
        ax1.plot(P[:, 0], P[:, 1], linewidth = 1, c = 'black')
        
        name = f'line{i}.png'
        
        fig.savefig(os.path.join(path, name))
        
        angle = get_angle(p2-p1, p3-p2)
        
        label_df.loc[len(label_df)] = [name, label, angle, *p1, *p2, *p3]
    label_df.to_csv(os.path.join(path, "label.csv"))