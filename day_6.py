# import matplotlib.pyplot as plt
# weight=[90,100,110,120,130,140,150]
# height=[1.5,2.0,2.5,3,3.5,4.0,4.5]
# fig,ax=plt.subplots()
# ax.bar(weight,height)
# plt.show()
import matplotlib.pyplot as plt
# fig,ax=plt.subplots()
# months=["Jan","Feb","Mar","Apr","May","June"]
# temp_recorded=[36,42,40,48,49,36]
# bar_labels=['sunny','hot','hot','superhot','superhot','cool']
# bar_colors=['tab:blue','tab:red','tab:red','tab:orange','tab:orange','tab:green']
# ax.bar(months,temp_recorded,label=bar_labels,color=bar_colors)
# ax.set_ylabel("Temperature by month")
# ax.set_title("Months")
# ax.legend()
# plt.show()
import numpy as np
# species=("adelie\n $\\mu=$3700.66g","Chinstrap\n $\\mu=$3733.09g","Gentoo\n $\\mu=5076.02g$")
#
# weight_counts={
#     "Below":np.array([70,31,58]),
#     "above":np.array([70,31,58])
# }
# width=0.5
# bottom=np.zeros(3)
# for boolean,weight_count in weight_counts.items():
#     p=plt.bar(species,weight_count,width,label=boolean,bottom=bottom)
#     bottom+=weight_count
# plt.title("Number of penguins with average body mass")
# plt.legend(loc="upper right")
# plt.show()
import numpy as np
# species=["adelie","Chinstrap","Gento"]
# penguin_means={
#     "Billdepth":(18.5,18.43,14.98),
#     "Bill Length":(38.79,48.83,47.50),
#     "Flipper Length":(189.95,195.82,217.19)
# }
# x=np.arange(len(species))# label locationse\
# width=.25
# multiplier=0
#
# fig,ax=plt.subplots(layout="constrained")
# for attribute,measurement in penguin_means.items():
#     offset=width*multiplier
#     print(x+offset)
#     rects=ax.bar(x+offset,measurement,width,label=attribute)
#     ax.bar_label(rects,padding=3)
#     multiplier+=1
# ax.set_label("length(mm)")
# ax.set_title("penguine Attribute by species")
# ax.set_xticks(x+width,species)
# ax.legend(loc="upper left",ncols=3)
# ax.set_ylim(0,250)
# plt.show()
fig,ax=plt.subplots(figsize=(6,3),subplot_kw=dict(aspect="equal"))
recipe=[
    "375 g flour",
    "75 g sugar",
    "250 g butter",
    "300 g berries"
]
data=[float(x.split()[0]) for x in recipe]
incredients=[(x.split()[-1]) for x in recipe]
def fun(pct,alvals):
    absolute=int(np.round(pct/100.*np.sum(alvals)))
    return f'{pct:.1f}%\n({absolute:d}g)'

wedges,texts,autotexts=ax.pie(data,autopct=lambda pct : fun(pct,data),textprops=dict(color="w"))
ax.legend(wedges,incredients,title="Ingredients",loc="center left",bbox_to_anchor=(1,0,0.5,1))
plt.setp(autotexts,size=8,weight="bold")
ax.set_title("Bakery:A pie")
plt.show()