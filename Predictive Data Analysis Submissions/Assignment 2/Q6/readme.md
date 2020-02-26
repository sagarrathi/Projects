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
### 6. The file Oreos.xlsx gives daily sales of Oreos at a supermarket and whether Oreos were placed 7" from the floor, 6" from the floor, or 5" from the floor. How does shelf position influence Oreo sales?[¶](#6.-------The-file-Oreos.xlsx-gives-daily-sales-of-Oreos-at-a-supermarket-and-whether-Oreos-were-placed-7”-from-the-floor,-6”-from-the-floor,-or-5”-from-the-floor.-How-does-shelf-position-influence-Oreo-sales?){.anchor-link} {#6.-------The-file-Oreos.xlsx-gives-daily-sales-of-Oreos-at-a-supermarket-and-whether-Oreos-were-placed-7”-from-the-floor,-6”-from-the-floor,-or-5”-from-the-floor.-How-does-shelf-position-influence-Oreo-sales?}
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
    oo=pd.read_excel("./Data/Oreos.xlsx")
    oo.head()
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

      Observation   Height in feet   Sales
  --- ------------- ---------------- -------
  0   1             5                28
  1   2             6                61
  2   3             7                40
  3   4             5                29
  4   5             5                36

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
    oo_dum_col=['Height in feet']
    ood=pd.get_dummies(oo, prefix_sep='_', dummy_na=False, columns=oo_dum_col)
    ood.head()
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

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Observation   Sales   Height in feet\_5   Height in feet\_6   Height in feet\_7
  --- ------------- ------- ------------------- ------------------- -------------------
  0   1             28      1                   0                   0
  1   2             61      0                   1                   0
  2   3             40      0                   0                   1
  3   4             29      1                   0                   0
  4   5             36      1                   0                   0

</div>
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
    ood.columns
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

::: {.output_text .output_subarea .output_execute_result}
    Index(['Observation', 'Sales', 'Height in feet_5', 'Height in feet_6',
           'Height in feet_7'],
          dtype='object')
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
    y_6=ood["Sales"]
    X_6=ood[['Height in feet_5','Height in feet_6', 'Height in feet_7']]
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
#### OLS Modeling[¶](#OLS-Modeling){.anchor-link} {#OLS-Modeling}
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
    X_6=sm.add_constant(X_6)
    model_6=sm.OLS(y_6, X_6).fit()
    model_6.summary()
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

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### OLS Diagnostic test[¶](#OLS-Diagnostic-test){.anchor-link} {#OLS-Diagnostic-test}
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
    ols_diag(ood,X_6,model_6)
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
    Rows to remove: [1, 11]
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
#### Ans 6 and Conclusion[¶](#Ans-6-and-Conclusion){.anchor-link} {#Ans-6-and-Conclusion}

1.  All our diagonetic test are good.
2.  It is recommeded to keep product in 6\" or 7\" inch from floor.
3.  It seems that people do not like bending heads to find product and
    retailers must not have lower shelf or display purpose, as it is
    waste of money.
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[ \]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
     
:::
:::
:::
:::
:::
:::
:::
