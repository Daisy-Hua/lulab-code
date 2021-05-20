import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

gene_list=[
'ENSG00000214049.6',
'ENSG00000222041.10',
'ENSG00000251164.1',
'ENSG00000047597.5',
'ENSG00000265185.5',
'ENSG00000276168.1',
'ENSG00000260386.6',
'ENSG00000133316.15',
'ENSG00000212283.1',
'ENSG00000278048.1',
'ENSG00000127957.17',
'ENSG00000100949.14'
]
###########################
data=pd.read_csv('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/HCC_longRNA.csv',sep='\t')
data2=pd.read_csv('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/TCGA_HCC.txt',sep='\t')
data2.columns=['ID']+[i.split('-')[0]+'-'+i.split('-')[1]+'-'+i.split('-')[2]+'-'+i.split('-')[3] for i in data2.columns[1:]]
data2_=data2.loc[data2.ID.isin(gene_list),:]
data2_=data2_.set_index('ID')
data2_=data2_.T
data2_=data2_.reset_index().rename(columns={'index':'Sample_ID'})

sample_label=pd.read_csv('/Share2/home/lulab1/TCGA/Metadata/Gene_Expression_Quantification/RNA_Seq_metadata/LIHC/LIHC_sample_sheet.2019-06-08.tsv',sep='\t')
sample_label['File']=sample_label['File Name'].map(lambda x:x.split('.')[0])
label=sample_label[['File','Sample ID', 'Sample Type']]
label.columns=['File','Sample_ID', 'label']
label=label.drop_duplicates()
label.index=range(len(label))
label['label']=label['label'].replace('Recurrent Tumor','HCC').replace('Primary Tumor','HCC').replace('Solid Tissue Normal','NC')

data2_=pd.merge(data2_,label[['Sample_ID', 'label']],on='Sample_ID',how='left')

for i in gene_list:
    plt.figure(figsize=(4,5))
    sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
    ax = sns.boxplot(x="label", y=i, data=data2_,order=["NC", "HCC"],palette=["#808080", "#E74C3C"])
    plt.ylabel(i)
    # plt.ylim([0,15])
    plt.tight_layout()
    sns.despine(offset=5, trim=True)
    plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/longRNA/'+i+'.png')
    plt.close()

plt.figure(figsize=(4,5))
sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
ax = sns.boxplot(x="label", y='ENSG00000214049.6', data=data2_,order=["NC", "HCC"],palette=["#808080", "#E74C3C"])
plt.ylabel('ENSG00000214049.6')
plt.ylim([0,20000])
plt.tight_layout()
sns.despine(offset=5, trim=True)
plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/longRNA/ENSG00000214049.6.png')
plt.close()

plt.figure(figsize=(4,5))
sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
ax = sns.boxplot(x="label", y='ENSG00000260386.6', data=data2_,order=["NC", "HCC"],palette=["#808080", "#E74C3C"])
plt.ylabel('ENSG00000260386.6')
plt.ylim([0,150])
plt.tight_layout()
sns.despine(offset=5, trim=True)
plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/longRNA/ENSG00000260386.6.png')
plt.close()

plt.figure(figsize=(4,5))
sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
ax = sns.boxplot(x="label", y='ENSG00000265185.5', data=data2_,order=["NC", "HCC"],palette=["#808080", "#E74C3C"])
plt.ylabel('ENSG00000265185.5')
plt.ylim([0,5000])
plt.tight_layout()
sns.despine(offset=5, trim=True)
plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/longRNA/ENSG00000265185.5.png')
plt.close()

plt.figure(figsize=(4,5))
sns.set_context("talk", font_scale=1, rc={"lines.linewidth": 2.5})
ax = sns.boxplot(x="label", y='ENSG00000276168.1', data=data2_,order=["NC", "HCC"],palette=["#808080", "#E74C3C"])
plt.ylabel('ENSG00000276168.1')
plt.ylim([0,5])
plt.tight_layout()
sns.despine(offset=5, trim=True)
plt.savefig('/BioII/lulab_b/liuxiaofan/project/expanel/HCC_TCGA/longRNA/ENSG00000276168.1.png')
plt.close()
# data_=data.loc[data['gene']=='ENSG00000276168.1',:]

