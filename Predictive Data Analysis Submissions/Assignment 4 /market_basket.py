import pandas as pd

##################################### Basic       #######################################
def set_internal_multiplier(df, load_set):
    
    ## Intialize series
    df0=df[load_set[0]]
    
    ## Multiply series
    for col in load_set: 
        df0=df0*df[col]

    ## Return Series
    return df0

def support_calculator(df, setA,setB):
    
    setA_series=set_internal_multiplier(df, setA)
    setB_series=set_internal_multiplier(df, setB)
    
    support= (sum(setA_series*setB_series)) /len(setA_series) 
    return support

def identity_creater(df):
    df["I"]=1
    return df

def confidence_calculator(df, setA, setB):
    
    #### Numerator
    support_AB=support_calculator(df, setA, setB)
    
    
    #### Denominator
    df=identity_creater(df)
    support_B=support_calculator(df,setB,"I")
    
    #### Ratio
    confidence=support_AB/support_B
    
    return confidence

def lift_calculator(df, setA, setB):
    
    #### Numerator
    confidence=confidence_calculator(df,setA, setB)
    
    #### Denominator
    df=identity_creater(df)
    support_A=support_calculator(df,setA,"I")
    
    #### Ratio
    lift = confidence/support_A
    return lift
    

################################################# Advance ##################################


def set_acceptor(A, B, min_diff, unique):
    flag=True
    
        
    if len(A) >= len (B):
        diff=abs(len(set(A)-set(B)))
        commonalities = set(A) - (set(A) - set(B))

    else:
        diff=abs(len(set(B)-set(A)))
        commonalities = set(B) - (set(B) - set(A))

    
    
    if unique:
        if len(commonalities)>0:
            flag=False
            
    elif (len(A)>1) or (len(B)>1):
        if not diff>min_diff:
            flag= False
            
    else:
        if not diff>=2:
            flag= False
        
    return flag



def basket_combination_finder(X, setA_N, setB_N, min_diff, unique):
    from itertools import combinations
    setA_basket=list(combinations(X, setA_N))
    setB_basket=list(combinations(X, setB_N))

    comb_list=[]
    
    for A in setA_basket:
        for B in setB_basket:
            row=[A, B]
            if set_acceptor(A, B, min_diff, unique):
                comb_list.append(row)
    df_comb=pd.DataFrame(comb_list, columns=["A","B"])
    return df_comb




def master_basket_combination_finder(X, min_diff, unique):
    from itertools import permutations
    
    
    X_num_list=list(range(1, (len(X)+1) ))
    
    perm_list=list(permutations(X_num_list, 2))
    
    df_comb=pd.DataFrame(columns=["A","B"])
    
    for p in perm_list:
        dfc=basket_combination_finder(X, p[0], p[1], min_diff, unique)
        df_comb=df_comb.append(dfc)
    
    df_comb=df_comb.reset_index()
    return df_comb
############################################### Final Output #####################################


def basket_calculator(df,X,confidence_level=.6,  min_diff=1, unique=True):
    
        
    dfc=master_basket_combination_finder(X, min_diff, unique)
    dfc["support"]=0.0
    dfc["confidence"]=0.0
    dfc["lift"]=0.0
    
    
    for i in range(len(dfc)):
        
        setA=dfc.iloc[i]["A"]
        setB=dfc.iloc[i]["B"]
        
        support=support_calculator(df, setA, setB)
        confidence=confidence_calculator(df, setA, setB)
        lift=lift_calculator(df, setA, setB)
        
        
        
        dfc.at[i, "support"]=float(support)
        dfc.at[i, "confidence"]=float(confidence)
        dfc.at[i, "lift"]=float(lift)
    
    dfc= dfc[ dfc["confidence"]>=confidence_level]
    dfc=dfc.sort_values(by="lift", ascending=False)
    return dfc
