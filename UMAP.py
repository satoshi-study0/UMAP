import matplotlib as plt
import umap

model_umap = umap.UMAP(n_components=2,n_neighbors=8) #n_neighborsは2~100でデータに応じて変更
#vecs_list = model_umap.fit_transform(df_embedding)
vecs_list = model_umap.fit_transform(df)

#次元圧縮した結果をデータフレーム化
df_umap_result = pd.DataFrame(vecs_list)
df_umap_result['cluster'] = np.array(rank)[:,0]
df_umap_result


#ClusterName = ['Cluster0','Cluster1','Cluster2','Cluster3','Cluster4','Cluster5','Cluster6','Cluster7','Cluster8']
ClusterName = ['Cluster0','Cluster1','Cluster2','Cluster3','Cluster4','Cluster5','Cluster6','Cluster7','Cluster8','Cluster9','Cluster10','Cluster11','Cluster12','Cluster13']
ax = plt.subplot()
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.get_cmap("tab20").colors)
for id, d in df_umap_result.groupby('cluster'):
    ax.scatter(x=d[0], y=d[1], label=ClusterName[id])
#ax.legend()
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=8)
plt.show()