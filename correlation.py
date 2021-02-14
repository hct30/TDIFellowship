# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:25:29 2021
@author: hct30
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#! Data
df = pd.read_csv('ngl_cpt.csv')
print(df.describe())

#! Depenedence of sleeve resistance fs and tip resistance qc with depth of penetration
test_id=869
depth = df['SCPT_DPTH'].loc[df['TEST_ID']==test_id]
qc =  df['SCPT_RES'].loc[df['TEST_ID']==test_id]
fs = df['SCPT_FRES'].loc[df['TEST_ID']==test_id]

fig = plt.figure(figsize=(5,6))
gs = gridspec.GridSpec(1, 2,figure=fig,width_ratios=[1,1])
ax1 = plt.subplot(gs[0:,0])
ax2 = plt.subplot(gs[0:,1])
gs.update(wspace=1,hspace=0.5)
ax1.plot(qc, depth, label='Measured')
ax2.plot(fs, depth, label='Measured')
ax1.set_xlabel('tip resistance (MPa)')
ax2.set_xlabel('sleeve resistance (MPa)')
ax1.set_xlim(0,20), ax2.set_xlim(0,0.3)


for ax in [ax1, ax2]:
    ax.set_ylim(0,14)    
    ax.set_ylabel('depth (m)')
    ax.invert_yaxis()
    ax.legend(bbox_to_anchor=(0.1,1.05),loc='center left')

plt.show()

#! save figure as pdf
figname="Figure3"
fig.savefig(figname+".pdf", bbox_inches='tight')


