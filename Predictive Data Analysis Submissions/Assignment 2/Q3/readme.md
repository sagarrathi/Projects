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
    # ols_diag(df,X,model, nlag=1, remove_outliers=False):
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
#### 3. The file Countryregion.xlsx contains the following data for several underdeveloped countries:[¶](#3.-------The-file-Countryregion.xlsx-contains-the-following-data-for-several-underdeveloped-countries:){.anchor-link} {#3.-------The-file-Countryregion.xlsx-contains-the-following-data-for-several-underdeveloped-countries:}

         ■ Infant mortality rate

         ■ Adult literacy rate

         ■ Percentage of students finishing primary school

         ■ Per capita GNP

Use this data to develop an equation that can be used to predict infant
mortality. Are there any outliers in this set of data? Interpret the
coefficients in your equation. Within what value should 95 percent of
your predictions for infant mortality be accurate?
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
    cn=pd.read_excel("./Data/Countryregion.xlsx", sheet_name="Sheet1")
    cn.head()
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

      Country      Infant Mortality(deaths per thousand births)   %age adult literacy   %age finishing primary school   GNP per capita
  --- ------------ ---------------------------------------------- --------------------- ------------------------------- ----------------
  0   Cuba         18                                             98                    98                              2000
  1   Sri Lanka    20                                             85                    92                              3300
  2   Costa Rica   19                                             94                    84                              5800
  3   Vietnam      44                                             85                    58                              600
  4   China        54                                             80                    86                              2400

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
    cn.columns
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
    Index(['Country', 'Infant Mortality(deaths per thousand births)',
           '%age adult literacy', '%age finishing primary school',
           'GNP per capita'],
          dtype='object')
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
    y_3=cn[['Infant Mortality(deaths per thousand births)']]
    X_3=cn[['%age adult literacy', '%age finishing primary school',
           'GNP per capita']]
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
    X_3=sm.add_constant(X_3)
    model_3=sm.OLS(y_3, X_3).fit()
    model_3.summary()
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
In \[7\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    ols_diag(cn,X_3,model_3)
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
    Rows to remove: [3, 8]
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
#### Ans 3 and Conclusion[¶](#Ans-3-and-Conclusion){.anchor-link} {#Ans-3-and-Conclusion}

-   From above data we see that we do not have any outliers in our data.
-   We also see that \"%age adult literacy\" is the only sigificant
    parameter affecting the infant Mortality with negative coefficient.
-   Every country must hence target to increase Adult Litracy Rate to
    decreases Infant Mortality rate.
-   We do not find any outliers in this data.
:::
:::
:::
:::
:::
