::: {#notebook .border-box-sizing tabindex="-1"}
::: {#notebook-container .container}
::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[13\]:
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
In \[14\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    !ls Data
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

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### 1. Fizzy Drugs wants to optimize the yield from an important chemical process. The company thinks that the number of pounds produced each time the process runs depends on the size of the container used, the pressure, and the temperature. The scientists involved believe the effect to change one variable might depend on the values of other variables. The size of the process container must be between 1.3 and 1.5 cubic meters; pressure must be between 4 and 4.5 mm; and temperature must be between 22 and 30 degrees Celsius. The scientists patiently set up experiments at the lower and upper levels of the three control variables and obtain the data shown in the fi le Fizzy.xlsx.[¶](#1.---Fizzy-Drugs-wants-to-optimize-the-yield-from-an-important-chemical-process.-The-company-thinks-that-the-number-of-pounds-produced-each-time-the-process-runs-depends-on-the-size-of-the-container-used,-the-pressure,-and-the-temperature.-The-scientists-involved-believe-the-effect-to-change-one-variable-might-depend-on-the-values-of-other-variables.-The-size-of-the-process-container-must-be-between-1.3-and-1.5-cubic-meters;-pressure-must-be-between-4-and-4.5-mm;-and-temperature-must-be-between-22-and-30-degrees-Celsius.-The-scientists-patiently-set-up-experiments-at-the-lower-and-upper-levels-of-the-three-control-variables-and-obtain-the-data-shown-in-the-fi-le-Fizzy.xlsx.){.anchor-link} {#1.---Fizzy-Drugs-wants-to-optimize-the-yield-from-an-important-chemical-process.-The-company-thinks-that-the-number-of-pounds-produced-each-time-the-process-runs-depends-on-the-size-of-the-container-used,-the-pressure,-and-the-temperature.-The-scientists-involved-believe-the-effect-to-change-one-variable-might-depend-on-the-values-of-other-variables.-The-size-of-the-process-container-must-be-between-1.3-and-1.5-cubic-meters;-pressure-must-be-between-4-and-4.5-mm;-and-temperature-must-be-between-22-and-30-degrees-Celsius.-The-scientists-patiently-set-up-experiments-at-the-lower-and-upper-levels-of-the-three-control-variables-and-obtain-the-data-shown-in-the-fi-le-Fizzy.xlsx.}

a\. Determine the relationship between yield, size, temperature, and
pressure.

b\. Discuss the interactions between pressure, size, and temperature.

c\. What settings for temperature, size, and pressure would you
recommend?
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
    fi=pd.read_excel("Data/Fizzy.xlsx",header=0)
    fi.head() 
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[15\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Yield   Size   Pressure   Temperature   S\*P   S\*T   P\*T
  --- ------- ------ ---------- ------------- ------ ------ ------
  0   1550    1.3    4.0        22            5.20   28.6   88
  1   1925    1.5    4.0        22            6.00   33.0   88
  2   2150    1.3    4.5        22            5.85   28.6   99
  3   2350    1.5    4.5        22            6.75   33.0   99
  4   1525    1.3    4.0        30            5.20   39.0   120

</div>
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[16\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    print("columns",fi.columns)
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
    columns Index(['Yield', 'Size', 'Pressure', 'Temperature', 'S*P', 'S*T', 'P*T'], dtype='object')
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
#### a. Determine the relationship between yield, size, temperature, and pressure.[¶](#a.-Determine-the-relationship-between-yield,-size,-temperature,-and-pressure.){.anchor-link} {#a.-Determine-the-relationship-between-yield,-size,-temperature,-and-pressure.}
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
Ans a.

-   Spliting data set
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[17\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    y_1=fi[['Yield']]
    X_1=fi[['Size', 'Pressure', 'Temperature']]
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
-   Regression without interaction
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[18\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    X_1=sm.add_constant(X_1)
    model_1=sm.OLS(y_1,X_1).fit()
    model_1.summary()
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
    /home/boo/anaconda3/envs/tf_gpu/lib/python3.6/site-packages/scipy/stats/stats.py:1394: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=16
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
#### Conclusion a.[¶](#Conclusion-a.){.anchor-link} {#Conclusion-a.}

-   Yield is dependent on upon Pressure and Size and not related to
    Temprature if interaction are ignored.
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### b. Discuss the interactions between pressure, size, and temperature.[¶](#b.-Discuss-the-interactions-between-pressure,-size,-and-temperature.){.anchor-link} {#b.-Discuss-the-interactions-between-pressure,-size,-and-temperature.}
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[19\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    X_1b=fi[['Size', 'Pressure', 'Temperature', 'S*P', 'S*T', 'P*T']]
    X_1b=sm.add_constant(X_1b)
    model_1b=sm.OLS(y_1,X_1b).fit()
    model_1b.summary()
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
    /home/boo/anaconda3/envs/tf_gpu/lib/python3.6/site-packages/scipy/stats/stats.py:1394: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=16
      "anyway, n=%i" % int(n))
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[20\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    from ols_diag import ols_diag
    ols_diag(fi,X_1b,model_1b)
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
    Dataset:    16
    X:   16
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
    Rows to remove: [5, 9]
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
#### Conclusion b.[¶](#Conclusion-b.){.anchor-link} {#Conclusion-b.}

-   Pressure, Temprature, Size have positive association on Yield.
-   S*P and S*T have negative association on Yiled.
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### c. What settings for temperature, size, and pressure would you recommend?[¶](#c.-What-settings-for-temperature,-size,-and-pressure-would-you-recommend?){.anchor-link} {#c.-What-settings-for-temperature,-size,-and-pressure-would-you-recommend?}

-   From above summary we will recommend values in order of priority:
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
1.  P: Presure should be set to max value and thus P=4.5
2.  S\*P: Size should be set to least value (as P is already max) and
    thus S= 1.3
3.  S\*T: Since size is set to least hence T is also set to least, and
    thus T=22
4.  Putting above values is equation the Yield would be:
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[21\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    model_1b.params
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[21\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    const         -18883.43750
    Size           11973.43750
    Pressure        3825.62500
    Temperature      111.09375
    S*P            -2012.50000
    S*T              -89.84375
    P*T                1.56250
    dtype: float64
:::
:::
:::
:::
:::

::: {.cell .border-box-sizing .code_cell .rendered}
::: {.input}
::: {.prompt .input_prompt}
In \[22\]:
:::

::: {.inner_cell}
::: {.input_area}
::: {.highlight .hl-ipython3}
    P1=4.5
    S1=1.3
    T1=22
    X_1val=[1,S1, P1, T1, S1*P1, S1*T1, P1*T1]
    round(sum(model_1b.params*X_1val))
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[22\]:
:::

::: {.output_text .output_subarea .output_execute_result}
    2153
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
#### Conclusion c:[¶](#Conclusion-c:){.anchor-link} {#Conclusion-c:}

-   Max Yield = 2153 Units
:::
:::
:::
:::
:::
