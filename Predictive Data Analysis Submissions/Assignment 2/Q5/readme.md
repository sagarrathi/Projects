::: {#notebook .border-box-sizing tabindex="-1"}
::: {#notebook-container .container}
::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[1\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    # %load ./import.py
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import seaborn as sns
    %matplotlib inline
    from sklearn.linear_model import LinearRegression
    !ls ./Data
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {.output_subarea .output_stream .output_stdout .output_text}
    Baseball96.xlsx  Countryregion.xlsx  Grocery.xlsx  USmacrodata.xls
    Cardata.xlsx     Fizzy.xlsx      Oreos.xlsx
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[2\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    from ols_diag import ols_diag
    # ols_diag(df,X,model, nlag=1, remove_outliers=False):
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
### 5. The file Cardata.xlsx provides the following information for 392 different car models:[¶](#5.-------The-file-Cardata.xlsx-provides-the-following-information-for-392-different-car-models:){.anchor-link} {#5.-------The-file-Cardata.xlsx-provides-the-following-information-for-392-different-car-models:}

        ■ Cylinders

        ■ Displacement

        ■ Horsepower

        ■ Weight

        ■ Acceleration

        ■ Miles per gallon (MPG)

Determine an equation that can predict MPG. Why do you think all the
independent variables are not significant?
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[3\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    car=pd.read_excel("./Data/Cardata.xlsx")
    car.head()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[3\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      cyl   disp    HP    wt     accel   mpg
  --- ----- ------- ----- ------ ------- ------
  0   8     304.0   193   4732   18.5    9.0
  1   8     307.0   200   4376   15.0    10.0
  2   8     360.0   215   4615   14.0    10.0
  3   8     400.0   150   4997   14.0    11.0
  4   8     350.0   180   3664   11.0    11.0

</div>
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[4\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    car.columns
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[4\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    Index(['cyl', 'disp', 'HP', 'wt', 'accel', 'mpg'], dtype='object')
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[5\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    y_5=car[["mpg"]]
    X_5=car[['cyl', 'disp', 'HP', 'wt', 'accel']]
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 1: OLS Modeling[¶](#Iteration-1:-OLS-Modeling){.anchor-link} {#Iteration-1:-OLS-Modeling}
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[6\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    X_5=sm.add_constant(X_5)
    model_5=sm.OLS(y_5,X_5).fit()
    model_5.summary()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[6\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
  ------------------- ------------------ --------------------- -----------
  Dep. Variable:      mpg                R-squared:            0.708
  Model:              OLS                Adj. R-squared:       0.704
  Method:             Least Squares      F-statistic:          186.9
  Date:               Tue, 30 Apr 2019   Prob (F-statistic):   9.82e-101
  Time:               03:52:43           Log-Likelihood:       -1120.1
  No. Observations:   392                AIC:                  2252\.
  Df Residuals:       386                BIC:                  2276\.
  Df Model:           5                                        
  Covariance Type:    nonrobust                                
  ------------------- ------------------ --------------------- -----------

  : OLS Regression Results

  ------- ------------ --------- -------- ---------- --------- ---------
          coef         std err   t        P\>\|t\|   \[0.025   0.975\]
  const   46.2643      2.669     17.331   0.000      41.016    51.513
  cyl     -0.3979      0.411     -0.969   0.333      -1.205    0.409
  disp    -8.313e-05   0.009     -0.009   0.993      -0.018    0.018
  HP      -0.0453      0.017     -2.716   0.007      -0.078    -0.012
  wt      -0.0052      0.001     -6.351   0.000      -0.007    -0.004
  accel   -0.0291      0.126     -0.231   0.817      -0.276    0.218
  ------- ------------ --------- -------- ---------- --------- ---------

  ---------------- -------- ------------------- ----------
  Omnibus:         38.561   Durbin-Watson:      0.575
  Prob(Omnibus):   0.000    Jarque-Bera (JB):   52.737
  Skew:            0.706    Prob(JB):           3.53e-12
  Kurtosis:        4.111    Cond. No.           3.87e+04
  ---------------- -------- ------------------- ----------

\
\
Warnings:\
\[1\] Standard Errors assume that the covariance matrix of the errors is
correctly specified.\
\[2\] The condition number is large, 3.87e+04. This might indicate that
there are\
strong multicollinearity or other numerical problems.
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 1: OLS Diagnostic test:[¶](#Iteration-1:-OLS-Diagnostic-test:){.anchor-link} {#Iteration-1:-OLS-Diagnostic-test:}
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[7\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    ols_diag(car,X_5,model_5)
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {.output_subarea .output_stream .output_stdout .output_text}
    Dataset:    392
    X:   392
    1. Normality Test:  Jarque-Bera Test
    -----------------------------------------------
    Warning
    Reason: Residual Not Normally distributed
    -----------------------------------------------


    2. Linearity Test:  Rainbow Test
    -----------------------------------------------
    Warning
    Reason: Data do not have linear relationship
    -----------------------------------------------


    3. Heteroscedasticity Test:  Breusch-Pagan Test
    -----------------------------------------------
    Warning
    Reason: Data do not have have same variance accross
    -----------------------------------------------


    4. Autocorrelation Test:  Breusch Godfrey Test
    -----------------------------------------------
    Warning
    Reason: Data are related to themself by:1 lag
    -----------------------------------------------


    5. Sum of residuals == 0
    -----------------------------------------------
    Good
    Reason: Sum of residuals = 0
    -----------------------------------------------


    6. Checking outliers:
    -----------------------------------------------
    Mode selected to remove Outliers: False
    Not Good: We have  40  Outliers
    Rows to remove: [13, 53, 54, 55, 107, 108, 113, 117, 131, 132, 138, 151, 152, 153, 171, 172, 183, 196, 212, 242, 259, 311, 337, 358, 365, 369, 372, 374, 376, 379, 381, 383, 384, 385, 386, 387, 388, 389, 390, 391]
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 1: Problems conclusion and further actions[¶](#Iteration-1:-Problems-conclusion-and-further-actions){.anchor-link} {#Iteration-1:-Problems-conclusion-and-further-actions}

-   We have breaking each and evry OLS assumtion as can be seen from
    above results.
-   We are follwing problem with this dataset:

1.  Residuals are not normally distributed.
2.  Thier is no linear relationship in the data
3.  Data do not have have same variance accross
4.  Data are related to themself by:1 lag
5.  We have atleast 40 outliers
6.  HP, Cylinder, Displacement ans Weight are all highly correleated
    with each other.

### Method A[¶](#Method-A){.anchor-link} {#Method-A}

#### Even if we remove the outliers the correlation between the terms will remain so we propose follwing action:[¶](#Even-if-we-remove-the-outliers-the-correlation-between-the-terms-will-remain-so-we-propose-follwing-action:){.anchor-link} {#Even-if-we-remove-the-outliers-the-correlation-between-the-terms-will-remain-so-we-propose-follwing-action:}

1.  Remove all 40 outliers
2.  Take diffrence of all variables with lag of itslef using
    Cochrane-Orcutt rho value of 1 as we have the one obtained using
    Cochrane-Orcutt is of no help in reducing autocrenaltion procedure
    and rerun OLS (Warning we are transforming variabl).
3.  Rerun regression \$\$ y\_{t}-\\rho y\_{{t-1}}=\\alpha (1-\\rho
    )+\\beta (X\_{t}-\\rho X\_{{t-1}})+e\_{t}.\\, \$\$
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[8\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    rows_to_remove=[13, 53, 54, 55, 107, 108, 113, 117, 131, 132, 138, 151, 152, 153, 171, 172, 183, 196, 212, 242, 259, 311, 337, 358, 365, 369, 372, 374, 376, 379, 381, 383, 384, 385, 386, 387, 388, 389, 390, 391]
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[9\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    car=car.drop(car.index[rows_to_remove])
    X_5=car[['cyl', 'disp', 'HP', 'wt', 'accel']]
    y_5=car[['mpg']]
    X_5=sm.add_constant(X_5)
    model_5=sm.OLS(y_5, X_5).fit()
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[10\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    ch_y=model_5.resid
    ch_X=model_5.resid

    ## Shift X by 1
    ch_X=ch_X.shift(periods=1, freq=None, axis=0)

    ## Remoce top row of X and y
    ch_X=ch_X[1:]
    ch_y=ch_y[1:]

    ## Remove bottom row of X
    print(len(ch_X))
    print(len(ch_X))
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {.output_subarea .output_stream .output_stdout .output_text}
    351
    351
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[11\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    model_ch=sm.OLS(ch_y, ch_X).fit()
    model_ch.params
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[11\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    x1    0.602161
    dtype: float64
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[12\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    rho=model_ch.params["x1"]
    rho=1
    car_rho=car*rho
    car_rho=car_rho.shift(periods=1,axis=0).fillna(0)
    car_rho=car_rho[:-1]
    car_rho
    car_b=car.subtract(car_rho)
    car_b=car_b.fillna(0)
    car_b.head()
    car_b=car_b.round(decimals=2)
    car_b.head()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[12\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      cyl   disp    HP      wt        accel   mpg
  --- ----- ------- ------- --------- ------- -----
  0   8.0   304.0   193.0   4732.0    18.5    9.0
  1   0.0   3.0     7.0     -356.0    -3.5    1.0
  2   0.0   53.0    15.0    239.0     -1.0    0.0
  3   0.0   40.0    -65.0   382.0     0.0     1.0
  4   0.0   -50.0   30.0    -1333.0   -3.0    0.0

</div>
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[13\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    car_b.columns
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[13\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    Index(['cyl', 'disp', 'HP', 'wt', 'accel', 'mpg'], dtype='object')
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 2: OLS Modeling[¶](#Iteration-2:-OLS-Modeling){.anchor-link} {#Iteration-2:-OLS-Modeling}
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[14\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    X_5b=car_b[['cyl', 'disp', 'HP', 'wt', 'accel']]
    y_5b=car_b[['mpg']]
    X_5b=sm.add_constant(X_5b)
    model_5b=sm.OLS(y_5b, X_5b).fit()
    model_5b.summary()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[14\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
  ------------------- ------------------ --------------------- ----------
  Dep. Variable:      mpg                R-squared:            0.389
  Model:              OLS                Adj. R-squared:       0.380
  Method:             Least Squares      F-statistic:          44.11
  Date:               Tue, 30 Apr 2019   Prob (F-statistic):   3.77e-35
  Time:               03:52:43           Log-Likelihood:       -172.49
  No. Observations:   352                AIC:                  357.0
  Df Residuals:       346                BIC:                  380.2
  Df Model:           5                                        
  Covariance Type:    nonrobust                                
  ------------------- ------------------ --------------------- ----------

  : OLS Regression Results

  ------- --------- ---------- -------- ---------- ---------- ---------
          coef      std err    t        P\>\|t\|   \[0.025    0.975\]
  const   0.1009    0.021      4.752    0.000      0.059      0.143
  cyl     0.1899    0.033      5.768    0.000      0.125      0.255
  disp    -0.0038   0.001      -5.125   0.000      -0.005     -0.002
  HP      0.0068    0.001      5.328    0.000      0.004      0.009
  wt      0.0002    6.87e-05   3.297    0.001      9.14e-05   0.000
  accel   0.0691    0.009      7.685    0.000      0.051      0.087
  ------- --------- ---------- -------- ---------- ---------- ---------

  ---------------- --------- ------------------- -----------
  Omnibus:         445.867   Durbin-Watson:      1.649
  Prob(Omnibus):   0.000     Jarque-Bera (JB):   63458.061
  Skew:            5.673     Prob(JB):           0.00
  Kurtosis:        67.792    Cond. No.           780\.
  ---------------- --------- ------------------- -----------

\
\
Warnings:\
\[1\] Standard Errors assume that the covariance matrix of the errors is
correctly specified.
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 2: OLS Diagnostic[¶](#Iteration-2:-OLS-Diagnostic){.anchor-link} {#Iteration-2:-OLS-Diagnostic}
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[15\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    ols_diag(car_b,X_5b,model_5b)
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {.output_subarea .output_stream .output_stdout .output_text}
    Dataset:    352
    X:   352
    1. Normality Test:  Jarque-Bera Test
    -----------------------------------------------
    Warning
    Reason: Residual Not Normally distributed
    -----------------------------------------------


    2. Linearity Test:  Rainbow Test
    -----------------------------------------------
    Warning
    Reason: Data do not have linear relationship
    -----------------------------------------------


    3. Heteroscedasticity Test:  Breusch-Pagan Test
    -----------------------------------------------
    Warning
    Reason: Data do not have have same variance accross
    -----------------------------------------------


    4. Autocorrelation Test:  Breusch Godfrey Test
    -----------------------------------------------
    Good
    Reason: Data are not related to themself:1 lag
    -----------------------------------------------


    5. Sum of residuals == 0
    -----------------------------------------------
    Good
    Reason: Sum of residuals = 0
    -----------------------------------------------


    6. Checking outliers:
    -----------------------------------------------
    Mode selected to remove Outliers: False
    Not Good: We have  36  Outliers
    Rows to remove: [0, 1, 3, 6, 7, 14, 20, 33, 45, 60, 61, 74, 82, 90, 92, 93, 95, 99, 112, 122, 157, 181, 197, 200, 204, 205, 210, 211, 235, 236, 248, 257, 271, 287, 303, 360]
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 2: Conclusion[¶](#Iteration-2:-Conclusion){.anchor-link} {#Iteration-2:-Conclusion}

1.  Even after removing autliers and taking Cochrane and self
    diffrenceing we are still breaking most of OLS assumtion.

2.  So we are stopping at this time to conclude that our model does not
    have any linear relationship
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### Iteration 3: To-Do[¶](#Iteration-3:-To-Do){.anchor-link} {#Iteration-3:-To-Do}

### Method B[¶](#Method-B){.anchor-link} {#Method-B}

#### Even if we remove the outliers the correlation between the terms will remain so we propose follwing action:[¶](#Even-if-we-remove-the-outliers-the-correlation-between-the-terms-will-remain-so-we-propose-follwing-action:){.anchor-link} {#Even-if-we-remove-the-outliers-the-correlation-between-the-terms-will-remain-so-we-propose-follwing-action:}

1.  Remove all 40 outliers
2.  Take log of all varaibles
3.  Take diffence of all varibales with its past
4.  Average HP, cyl, disp, wt
5.  Rerun regression

#### Which basically means we have performed too many surgeriers in data just to make model compatible to OLS, and thus we do not wich to continue any further. and out itertaion 2 is our answer[¶](#Which-basically-means-we-have-performed-too-many-surgeriers-in-data-just-to-make-model-compatible-to-OLS,-and-thus-we-do-not-wich-to-continue-any-further.-and-out-itertaion-2--is-our-answer){.anchor-link} {#Which-basically-means-we-have-performed-too-many-surgeriers-in-data-just-to-make-model-compatible-to-OLS,-and-thus-we-do-not-wich-to-continue-any-further.-and-out-itertaion-2--is-our-answer}
:::
:::
:::
:::
:::
