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
#### 2. For 12 straight weeks, you have observed the sales (in number of cases) of canned tomatoes at Mr. D's Supermarket. (See the fi le Grocery.xlsx.) Each week, you keep track of the following:[¶](#2.-------For-12-straight-weeks,-you-have-observed-the-sales-(in-number-of-cases)-of-canned-tomatoes-at-Mr.-D’s-Supermarket.-(See-the-fi-le-Grocery.xlsx.)-Each-week,-you-keep-track-of-the-following:){.anchor-link} {#2.-------For-12-straight-weeks,-you-have-observed-the-sales-(in-number-of-cases)-of-canned-tomatoes-at-Mr.-D’s-Supermarket.-(See-the-fi-le-Grocery.xlsx.)-Each-week,-you-keep-track-of-the-following:}

a\. Was a promotional notice for canned tomatoes placed in all shopping
carts?

b\. Was a coupon for canned tomatoes given to each customer?

c\. Was a price reduction (none, 1, or 2 cents off) given?

Use this data to determine how the preceding factors influence sales.
Predict sales of canned tomatoes during a week in which you use a
shopping cart notice, a coupon, and reduce price by 1 cent.
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
    gr=pd.read_excel("./Data/Grocery.xlsx",header=0)
    gr.head()
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

      Week   Cart Notice?   Coupon?   Price Reduction?   Sales
  --- ------ -------------- --------- ------------------ -------
  0   1      Yes            Yes       0                  36
  1   2      Yes            Yes       1                  38
  2   3      Yes            Yes       2                  40
  3   4      Yes            No        0                  40
  4   5      Yes            No        1                  42

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
    gr.columns
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
    Index(['Week', 'Cart Notice?', 'Coupon?', 'Price Reduction?', 'Sales'], dtype='object')
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
#### Converitng columns to dummy\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--[¶](#Converitng-columns-to-dummy-------------------){.anchor-link} {#Converitng-columns-to-dummy-------------------}
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
    gr_dum_col=['Cart Notice?', 'Coupon?', 'Price Reduction?']
    grr=pd.get_dummies(gr, prefix_sep='_', dummy_na=False, columns=gr_dum_col,  drop_first=True,)
    grr.head()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[5\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Week   Sales   Cart Notice?\_Yes   Coupon?\_Yes   Price Reduction?\_1   Price Reduction?\_2
  --- ------ ------- ------------------- -------------- --------------------- ---------------------
  0   1      36      1                   1              0                     0
  1   2      38      1                   1              1                     0
  2   3      40      1                   1              0                     1
  3   4      40      1                   0              0                     0
  4   5      42      1                   0              1                     0

</div>
:::
:::
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
    grr.columns
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

::: {.output_text .output_subarea .output_execute_result}
    Index(['Week', 'Sales', 'Cart Notice?_Yes', 'Coupon?_Yes',
           'Price Reduction?_1', 'Price Reduction?_2'],
          dtype='object')
:::
:::
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
    y_2=grr[["Sales"]]
    X_2=grr[['Cart Notice?_Yes', 'Coupon?_Yes',
           'Price Reduction?_1', 'Price Reduction?_2']]
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
-   Perfroming OLS now
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
    X_2=sm.add_constant(X_2)
    model_2=sm.OLS(y_2,X_2).fit()
    model_2.summary()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {.output_subarea .output_stream .output_stderr .output_text}
    /home/boo/anaconda3/envs/tf_gpu/lib/python3.6/site-packages/scipy/stats/stats.py:1394: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=12
      "anyway, n=%i" % int(n))
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
    ols_diag(grr,X_2, model_2)
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
    Dataset:    12
    X:   12
    1. Normality Test:  Jarque-Bera Test
    -----------------------------------------------
    Good
    Reason: Residual Normally distributed
    -----------------------------------------------


    2. Linearity Test:  Rainbow Test
    -----------------------------------------------
    Good
    Reason: Data have linear relationship
    -----------------------------------------------


    3. Heteroscedasticity Test:  Breusch-Pagan Test
    -----------------------------------------------
    Good
    Reason: Data have same variance accross
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
    Not Good: We have  2  Outliers
    Rows to remove: [9, 11]
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
    model_2.params
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[10\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    const                 14.500000
    Cart Notice?_Yes      20.166667
    Coupon?_Yes           -1.166667
    Price Reduction?_1     5.000000
    Price Reduction?_2    12.750000
    dtype: float64
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
    sales=model_2.params[0] \
    +model_2.params[1]*1 \
    +model_2.params[2]*1 \
    +model_2.params[3]*0 \
    +model_2.params[4]*2

    sales=sales.round(2)
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
#### And 2:[¶](#And-2:){.anchor-link} {#And-2:}

-   We predict that:
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
    print("Sales in which we use a shopping cart notice, a coupon, and reduce price by 1 cent is",sales,"$")
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
    Sales in which we use a shopping cart notice, a coupon, and reduce price by 1 cent is 59.0 $
:::
:::
:::
:::
:::
:::
:::
