This set of scripts produces and analyzes four input files using the snakemake pipeline: noSNP.var files for each, an Aged Mother
Yeast's last daughter, that daughter's daughter and a corresponding "forever young" lineage pair that have undergone the same number of divisions.
It then screens for places in the genome where heterozygous SNPs that resulted from the hybridized mating of two wildstrains are
converted to a homozygous variant, indicating a Loss of Heterozygosity event (LOH).
When such events are detected it outputs this location to two text files (One for Aged Pairs and one for Forever Young Pairs).
These locations can then be graphed on the graphical yeast genome using the script: LOHgraphing.py.

Order of Scripts:

Snakemake > Produces noSNP.var files
LOHsearch.py > Turns noSNP.var files into LOH calls in 2 text files
LOHcompiler.py > Produces a single text file for all generated LOH files, across all lines
LOHgraphing.py > uses the above input to produce a graphic image (.png) illustrated all detected LOH events for a single experiment type

ID note 11/1/2022: These scripts were last used in December of 2020, if needed again they could all easily be folded into the single existing Snakemake pipeline.
Originally kept separate for debugging purposes. Evaluate on future use.


Other Files:
312v314.txt
	Strain specific SNP information used during analysis. This collection is compiled from the specific SNPs of strains 312 and 314 (Sake and Malaysian origin wild yeast)

S288C-masked-genome.fasta
	The masked genome of the common laboratory strain S288C. This genome is used as a reference against the strain specific SNPs described in the previous text file.
	