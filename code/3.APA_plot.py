import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/BioII/lulab_b/huashuo/multiprimer/region/FPKM_CYP2E1_r.txt',sep="\t")

label_pico = pd.read_csv('/BioII/lulab_b/huashuo/label_data_stage_.txt',sep='\t')
label_pico=label_pico.rename(columns={'pipeline-ID':'sample_id','labels':'label','stage':'Stage'})
sample_id_pico = label_pico.loc[(label_pico['label']=='NC')|(label_pico['label']=='HCC'),'sample_id']
NC_pico = label_pico.loc[(label_pico['label']=='NC'),'sample_id']
HCC_pico_0 = label_pico.loc[(label_pico['label']=='HCC')&(label_pico['Stage']==0),'sample_id']
HCC_pico_1 = label_pico.loc[(label_pico['label']=='HCC')&(label_pico['Stage']==1),'sample_id']
fusion_2=list(pd.read_csv('/BioII/lulab_b/huashuo/genelist1.txt',header=None)[0])
data_pico=df.set_index('feature')
pico_data = data_pico.loc[fusion_2,list(NC_pico)+list(HCC_pico_0)+list(HCC_pico_1)].T
pico_data['label']=['NC' for i in range(len(NC_pico))]+['HCC_0' for i in range(len(HCC_pico_0))]+['HCC_1' for i in range(len(HCC_pico_1))]

pico_data.to_csv('/BioII/lulab_b/huashuo/multiprimer/region/plot_CYP2E1.csv',sep='\t')


# sns.set_theme(style="ticks", palette="pastel")
# ax = sns.boxplot(x="label", y="gene", data=data_,order=["NC", "HCC"])
# plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC/code/test.png')
# plt.close()
