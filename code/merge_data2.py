import pandas as pd
import os
path='/BioII/lulab_b/huashuo/as/bam/'

data_all=pd.DataFrame(columns={i.split('feature')[0]  for i in os.listdir(path)})
for i in os.listdir(path):
    data=pd.read_csv(path+i,sep='\t',header=None)
    data=data[data[3].str.contains('exon')]
    data_all[i.split('feature')[0]]=data[6]
data_all['ID']=data[0]+'|'+data[1].astype('str')+'|'+data[2].astype('str')
data_all=data_all[['ID']+[i.split('feature')[0]  for i in os.listdir(path)]]

data_all.to_csv('/BioII/lulab_b/huashuo/as/as_peak.txt',sep='\t',index=False)



