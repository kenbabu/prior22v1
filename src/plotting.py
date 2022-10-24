def plot_ontology_ranks(dataset, **kwargs):
    f, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(15,14), sharex=True, sharey=True)
    plt.suptitle(kwargs['title'], size=16)
    
    x = list(DictUniprotGene.get(p) for p in kwargs['go'].keys())
#     print(x)
    y1 = [int(kwargs['go'][key]) for key in list(kwargs['go'].keys())]
#     print(y1)
    bar1=sns.barplot(x=x, y=y1, palette="deep", ax=ax1)
    ax1.axhline(0,color="k", clip_on=False)
    for b in bar1.patches:
        bar1.annotate(format(b.get_height(), '.0f'), 
                     (b.get_x() + b.get_width() /2., b.get_height()),
                     ha='center', va='center', size=8,
                     xytext =(0, 5), 
                     textcoords = 'offset points')
    
#     ax1.set_yscale('log')
    ax1.set_ylabel("GO Ranks")
   
    
    y2 = [int(kwargs['hpo'][key]) for key in list(kwargs['hpo'].keys())]
#     print(y2)
    bar2=sns.barplot(x=x, y=y2, palette="deep", ax=ax2)
    ax2.axhline(0,color="k", clip_on=False)
    for b in bar2.patches:
        bar2.annotate(format(b.get_height(), '.0f'), 
                     (b.get_x() + b.get_width() /2., b.get_height()),
                     ha='center', va='center', size=8,
                     xytext =(0, 5), 
                     textcoords = 'offset points')
    
#     ax2.set_ylim([0,5000])
#     ax2.set_yscale('log')
    ax2.set_ylabel("HPO Ranks")
    
    y3 = [int(kwargs['gohpo'][key]) for key in list(kwargs['gohpo'].keys())]
    bar3=sns.barplot(x=x, y=y3, palette="deep", ax=ax3)
    ax3.axhline(0,color="k", clip_on=False)
    ax3.set_xlabel('Genes')
    for b in bar3.patches:
        bar3.annotate(format(b.get_height(), '.0f'), 
                     (b.get_x() + b.get_width() /2., b.get_height()),
                     ha='center', va='center', size=8,
                     xytext =(0, 5), 
                     textcoords = 'offset points')
    
#     ax3.set_yscale('log')
    ax3.set_ylabel("GO & HPO Ranks")
    ax3.set_xticklabels(x, rotation = 45, ha='right')
    plt.savefig(f"{dataset}.png")
    