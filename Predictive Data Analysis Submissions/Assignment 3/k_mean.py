import pandas as pd



def k_starter(df,N):
    k=df.sample(n=N)
    k.index=list(range(1,len(k)+1))
    k.index.name="cluster"
    return k

def cluster_finder(df,X,k, iteration):
    ecd_s=[]
    cluster_s=[]

    for i in range(len(df)):

        ### Matrix operations
        ecd=(k[X]-df[X].iloc[i])
        ecd_2=ecd**2

        ### Column operations 
        ecd_2["ecd"]=ecd_2.sum(axis=1)
        ecd_2["ecd2"]=ecd_2["ecd"]**0.5

        
        ### Minmum finder
        cluster_val=ecd_2[  ecd_2["ecd2"] == ecd_2["ecd2"].min()].index.item()
        
        ecd_val=ecd_2["ecd2"].min()
            
        ### Minimum Saver
        cluster_s.append(cluster_val)
        ecd_s.append(ecd_val)

    cluster_col_name="step_"+str(iteration)
    ecd_col_name="ecd_"+str(iteration)

    df[cluster_col_name]=pd.Series(cluster_s)
    df[ecd_col_name]=pd.Series(ecd_s)

    return df, iteration

def k_finder(df,X,iteration):
    cluster_col_name="step_"+str(iteration)
    ecd_col_name="ecd_"+str(iteration)
    k=df.groupby(cluster_col_name).mean()[X]
    k.index.name="cluster"
    return k

def convergence_breaker(df, iteration):
    to_break=False
    if iteration>1:
#     if iteration>20:
        previous_iteration=iteration-1
        cluster_col_name="step_"+str(iteration)
        previous_cluster_col_name="step_"+str(previous_iteration)
        diff=sum(list(df[previous_cluster_col_name]-df[cluster_col_name]))
        if not diff:
            to_break=True
            
    return to_break
        
def k_mean(df,X,N):
    
    ###############################Scaling datafroame
    from sklearn import preprocessing
    x = df[X].values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df[X] = pd.DataFrame(x_scaled)
    ####################################################################################3
    
    iteration =1
    k=k_starter(df,N)
    
    to_break=False
    while (to_break==False):
        df, iteration=cluster_finder(df,X,k,iteration)
        k=k_finder(df,X,iteration)
        to_break=convergence_breaker(df,iteration)
        iteration =iteration+1
        
    return df,iteration 


##########################################################################################################
########################################################PCA###############################################
##########################################################################################################
def pca_retirever(df, X):
    ############### PCA FITTING ###############################################
    from sklearn.decomposition import PCA
    df_scaled=(    df[X]  -  df[X].min() )/(   df[X].max() - df[X].min()         )
    pca=PCA(n_components=2)
    pca.fit(df_scaled)
    ###########################################################################

    pca1=[]
    pca2=[]
    for i in range(len(df_scaled)):
        pca1.append(sum(df_scaled[X].iloc[i]*pca.components_[0]))
        pca2.append(sum(df_scaled[X].iloc[i]*pca.components_[1]))
        
    pca1=pd.Series(pca1)
    pca2=pd.Series(pca2)
    
    df["pca1"]=pca1
    df["pca2"]=pca2
    
    return df





def plotter(df, iteration, output_dir):

    #################################### MATPLOTLIB IMPORTING#########################################
    import matplotlib.pyplot as plt
    
    from matplotlib.animation import FuncAnimation
    #%matplotlib nbagg
    
    ################################### Seaborn Import################################################3
    import seaborn as sns
    
    ### For Saving
    import os


    ### Blank Canvas
    fig,ax=plt.subplots(figsize=(6,6))
    marker_size=200

    
#     print("It works:", len(df))
#     sns.scatterplot(x="pca1", y="pca2", data=df, s=marker_size, palette="Paired")
#     plt.show()
    
    
    ### Data updation function
    def animate(i):
        ax.clear()
        if i==0:
            sns.scatterplot(x="pca1", y="pca2", data=df, s=marker_size, palette="Paired").set_title("Initial Data")
            step_name="./"+output_dir+"/Initial_Data.png"
        else:
            cluster_col_name="step_"+str(i)
            sns.scatterplot(x="pca1", 
                            y="pca2", 
                            data=df, 
                            hue=cluster_col_name, 
                            s=marker_size,
                            palette="Paired"
                            ).set_title("STEP: "+str(i))
            step_name="./"+output_dir+"/STEP_"+str(i)+".png"
        
        if not os.path.isfile(step_name):
            plt.savefig(step_name)

    ############# Animation tarts now
    anim=FuncAnimation(fig, animate,interval=1200, frames= iteration,repeat=True )
    anim.save("./"+output_dir+"/animation.gif", writer='imagemagick', fps=1)
    ##################### Displaying Animation
    
    
    return anim


def final_answer(df, iteration,y, file_name, output_dir):
    y_vals=pd.Series(df[y])
    previous_iteration=iteration-1
    last_step_col_name="step_"+str(previous_iteration)
    cluster_vals=pd.Series(df[last_step_col_name])
    
    df_out=pd.concat([cluster_vals,y_vals,], axis=1)    
    df_out=df_out.sort_values([last_step_col_name, y]).reset_index()

    file_name="./"+output_dir+"/"+file_name+str(".csv")
    df_out.to_csv(file_name)
    return df_out


def plot_printer(df, iteration, output_dir):
    
    import matplotlib.pyplot as plt
    
    import seaborn as sns
    
    marker_size=150
    
    plt.figure(0)
    sns.scatterplot(x="pca1", y="pca2", data=df, s=marker_size, palette="Paired").set_title("STEP 0")
    assignmanet_name="./"+output_dir+"/"
    step_name=assignmanet_name+"STEP_0"+".png"
    plt.savefig(step_name)
    
    for i  in range(1, iteration):
        plt.clf()
        plt.figure(i)
        cluster_col_name="step_"+str(i)
        sns.scatterplot(x="pca1", 
                        y="pca2", 
                        data=df, 
                        hue=cluster_col_name, 
                        s=marker_size,
                        palette="Paired"
                       ).set_title("STEP "+str(i))
        