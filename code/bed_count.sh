#!/bin/sh
path="/BioII/lulab_b/liuxiaofan/project/expanel_domain/pico/bam/"
savepath="/BioII/lulab_b/huashuo/as/bam/"
for i in `ls ${path}`
do
echo ${i}
/BioII/lulab_b/liuxiaofan/software/bedtools/bedtools2/bin/bedtools  multicov -f 0.1 -S -bams ${path}/${i}/genome_rmdup.out.sorted.bam -bed /BioII/lulab_b/huashuo/as/data/as.bed > ${savepath}/${i}_featurecounts.bed
done

