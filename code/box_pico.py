import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/BioII/lulab_b/huashuo/multiprimer/region/plot_CYP2E1.csv',sep='\t')

for i in list(data.columns[1:-1]):
    plt.figure(figsize=(4,5))
    sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
    ax = sns.boxplot(x="label", y=i, data=data,order=["NC", "HCC_0","HCC_1"],palette=["#808080", "#239B56","#2980B9"])
    plt.ylabel(i.split('|')[0])
    # plt.ylim([0,400])
    plt.tight_layout()
    sns.despine(offset=5, trim=True)
    plt.savefig('/BioII/lulab_b/huashuo/multiprimer/box/'+i.split('|')[0]+'|'+i.split('|')[1]+'.png')
    plt.close()
