import statsmodels.stats.stattools as smt
import statsmodels.stats.diagnostic as smd
import matplotlib.pyplot as plt
#% matplotlib inline
import seaborn as sns



def heatmap(X):
    X=X.astype(float)
    X_corr=X.corr()
    X_corr_order=X_corr.sum().sort_values(ascending=True).index.values
    X_corr=X[X_corr_order].corr()
    print("-----------------------------------------------")
    plt.figure(figsize=(12, 8))
    hm=sns.heatmap(X_corr, annot=True, cmap="YlGnBu");
    plt.show(hm)
    plt.clf()
    
    print("-----------------------------------------------")
    
def outliers(df,model,lower_quartile=0.05,upper_quartile=0.95, remove_outliers=False):
    
    print("-----------------------------------------------")
    ax=sns.boxplot(y=model.resid)
    print("Mode selected to remove Outliers:", remove_outliers)
   
    resid=model.resid
    ql=resid.quantile(lower_quartile)
    qu=resid.quantile(upper_quartile)

    resid_filter = resid[(resid<ql)|(resid>qu) ]
    delta=len(resid_filter)
   
    rows_to_remove=[]
    if delta:
        rows_to_remove=list(resid_filter.index)
        print("Not Good:", "We have ",delta, " Outliers")        
        print("Rows to remove:", rows_to_remove)
    else:
        print("Good:", "No Outliers detected")
    plt.show(ax)
    plt.clf()
    
    
    print("-----------------------------------------------")
    print("\n\n")
    

def hypo_out(p_value, H0, H1):
    print("-----------------------------------------------")
    if p_value < 0.05:
        print("Warning")
        reason=H1
    else:
        print("Good")
        reason=H0
    print("Reason:", reason)
    print("-----------------------------------------------")
    print("\n")
    
    
def ols_diag(df,X,model, nlag=1, remove_outliers=False):
    
    ### Small Info
    print("Dataset:","\t",len(df))
    print("X:","\t",len(X))
    
    ## Residdual Normalaity Test
    print("1. Normality Test: ", "Jarque-Bera", "Test")
    jb_h0="Residual Normally distributed"
    jb_h1="Residual Not Normally distributed"
    jb_p=smt.jarque_bera(model.resid)[1]
    hypo_out(jb_p, jb_h0, jb_h1)

    ## Data Linearity Test
    print("2. Linearity Test: ","Rainbow", "Test")
    r_h0="Data have linear relationship"
    r_h1="Data do not have linear relationship"
    r_t,r_p=smd.linear_rainbow(model)
    hypo_out(r_p, r_h0, r_h1)
    
    
    ## Hetrosedacity Test: Scaling error
    print("3. Heteroscedasticity Test: ","Breusch-Pagan", "Test")
    bp_h0="Data have same variance accross"
    bp_h1="Data do not have have same variance accross"
    bp_p=smd.het_breuschpagan(model.resid, model.model.exog)[1]
    hypo_out(bp_p, bp_h0, bp_h1)
    
    ## Autocrrelation Test
    print("4. Autocorrelation Test: ","Breusch Godfrey", "Test")
    bg_h0="Data are not related to themself:"+str(nlag)+" lag"
    bg_h1="Data are related to themself by:"+str(nlag)+" lag"
    bg_p=smd.acorr_breusch_godfrey(model, nlag)[1]
    hypo_out(bg_p, bg_h0, bg_h1)
    
    ## Sum residulas =0 
    print("5. Sum of residuals == 0")
    sr_h0="Sum of residuals = 0"
    sr_h1="Sum of residual != 0"
    if round(sum(model.resid),1)==0:
        sr_p=1
    else:
        sr_p=0
    hypo_out(sr_p, sr_h0, sr_h1)
    
    
    ## List of outliers 
    print("6. Checking outliers:")
    outliers(df,model,remove_outliers=False)
  

    ## Endogenity Check: 
#     print("7. Checking Endogenity:"; )
#     heatmap(X)

    ## Multicolinearity test: 
    print("7. Checking multicolinearity")
    try: 
        heatmap(X)
    except:
        print("Cannot perrform this test")