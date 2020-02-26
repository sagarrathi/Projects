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
    ! tree
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
    .
    ├── animation.gif
    ├── Assignment 3.1.ipynb
    ├── Assignment 3.2.ipynb
    ├── Assignment 3-Copy1.2.ipynb
    ├── Cluster_lib.ipynb
    ├── Data
    │   ├── cereal.xls
    │   └── NewMBAdata.xlsx
    ├── import.py
    ├── k_mean.py
    ├── None0000000.png
    ├── output_1
    │   ├── animation.gif
    │   ├── Initial_Data.png
    │   ├── STEP_1.png
    │   ├── STEP_2.png
    │   ├── STEP_3.png
    │   ├── STEP_4.png
    │   └── University.csv
    ├── output_2
    └── __pycache__
        └── k_mean.cpython-36.pyc

    4 directories, 18 files
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
1.1 Importing common libraries[¶](#1.1-Importing-common-libraries){.anchor-link} {#1.1-Importing-common-libraries}
================================================================================
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
    # %load ../import.py
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
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
1.2 Imporitng custom library[¶](#1.2-Imporitng-custom-library){.anchor-link} {#1.2-Imporitng-custom-library}
============================================================================
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
    from k_mean import k_mean
    ###Syntax:
    # k_mean(df,X,N)
    ### INput
    # df
    # X
    # N
    ### Output
    # df : moddified with all steps 
    # iteration: number of iteration

    from k_mean import pca_retirever
    ### Syntax
    # pca_retirever(df, X)
    ### INput
    #df
    #X
    ### Output
    #df



    from k_mean import plotter
    ### Syntax
    # plotter(df, iteration)
    ### INput
    # df
    # iteration
    ### Output
    # anim : plt object


    from k_mean import final_answer
    ### Syntax
    # final_answer(df, iteration,y, file_name, output_dir):

    ### INput
    # df
    # iteration
    # y
    # file_name

    ### Output
    # df_out: 
    # file daved at location


    from k_mean import plot_printer
    # def plot_printer(df, iteration, output_dir):

    ### INput
    # df
    # iteration
    # output_dir
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
2. Question[¶](#2.-Question){.anchor-link} {#2.-Question}
==========================================
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
#### 1. \#\# 2. The file cereal.xls contains calories, protein, fat, sugar, sodium, fiber, carbs, sugar, and potassium content per ounce for 43 breakfast cereals. Use this data to perform a cluster analysis with five anchors.[¶](#1.-----##-2.------The-file-cereal.xls-contains-calories,-protein,-fat,-sugar,-sodium,-fiber,-carbs,-sugar,-and-potassium-content-per-ounce-for-43-breakfast-cereals.-Use-this-data-to-perform-a-cluster-analysis-with-five-anchors.){.anchor-link} {#1.-----##-2.------The-file-cereal.xls-contains-calories,-protein,-fat,-sugar,-sodium,-fiber,-carbs,-sugar,-and-potassium-content-per-ounce-for-43-breakfast-cereals.-Use-this-data-to-perform-a-cluster-analysis-with-five-anchors.}
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
3. Importing data[¶](#3.-Importing-data){.anchor-link} {#3.-Importing-data}
======================================================
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
    df=pd.read_excel("./Data/cereal.xls")
    df.head()
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

      Rank   Cereal          Cal   Protein   Fat   Sodium   Fiber   Carbs   Sugar   Potassium
  --- ------ --------------- ----- --------- ----- -------- ------- ------- ------- -----------
  0   1      ACCheerios      110   2         2     180      1.5     10.5    10      70
  1   2      Cheerios        110   6         2     290      2.0     17.0    1       105
  2   3      CocoaPuffs      110   1         1     180      0.0     12.0    13      55
  3   4      CountChocula    110   1         1     180      0.0     12.0    13      65
  4   5      GoldenGrahams   110   1         1     280      0.0     15.0    9       45

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
    df.columns
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
    Index(['Rank', 'Cereal', 'Cal', 'Protein', 'Fat', 'Sodium', 'Fiber', 'Carbs',
           'Sugar', 'Potassium'],
          dtype='object')
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
4. Setting Parameters[¶](#4.-Setting-Parameters){.anchor-link} {#4.-Setting-Parameters}
==============================================================
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
4.1 Renaming columns[¶](#4.1-Renaming-columns){.anchor-link} {#4.1-Renaming-columns}
------------------------------------------------------------
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
    df.columns=['Rank','Cereal', 'Cal', 'Protein', 'Fat', 'Sodium', 'Fiber', 'Carbs', 'Sugar',
           'Potassium']
    df.columns
    df.head()
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
<div>

      Rank   Cereal          Cal   Protein   Fat   Sodium   Fiber   Carbs   Sugar   Potassium
  --- ------ --------------- ----- --------- ----- -------- ------- ------- ------- -----------
  0   1      ACCheerios      110   2         2     180      1.5     10.5    10      70
  1   2      Cheerios        110   6         2     290      2.0     17.0    1       105
  2   3      CocoaPuffs      110   1         1     180      0.0     12.0    13      55
  3   4      CountChocula    110   1         1     180      0.0     12.0    13      65
  4   5      GoldenGrahams   110   1         1     280      0.0     15.0    9       45

</div>
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
4.2 Identyfying X[¶](#4.2-Identyfying-X){.anchor-link} {#4.2-Identyfying-X}
------------------------------------------------------
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
    X=['Cal', 'Protein', 'Fat', 'Sodium', 'Fiber', 'Carbs', 'Sugar',
           'Potassium']
    df[X].head()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[7\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Cal   Protein   Fat   Sodium   Fiber   Carbs   Sugar   Potassium
  --- ----- --------- ----- -------- ------- ------- ------- -----------
  0   110   2         2     180      1.5     10.5    10      70
  1   110   6         2     290      2.0     17.0    1       105
  2   110   1         1     180      0.0     12.0    13      55
  3   110   1         1     180      0.0     12.0    13      65
  4   110   1         1     280      0.0     15.0    9       45

</div>
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
4.3 Identyfying y[¶](#4.3-Identyfying-y){.anchor-link} {#4.3-Identyfying-y}
------------------------------------------------------
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
    y=["Cereal"]
    df[y].head()
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt .output_prompt}
Out\[8\]:
:::

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Cereal
  --- ---------------
  0   ACCheerios
  1   Cheerios
  2   CocoaPuffs
  3   CountChocula
  4   GoldenGrahams

</div>
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
4.4 Setup Numbe of cluster, here: 5[¶](#4.4-Setup-Numbe-of-cluster,-here:-5){.anchor-link} {#4.4-Setup-Numbe-of-cluster,-here:-5}
------------------------------------------------------------------------------------------
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
    N=5
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
5. Starting K-Mean Clustering algo[¶](#5.-Starting-K-Mean-Clustering-algo){.anchor-link} {#5.-Starting-K-Mean-Clustering-algo}
========================================================================================
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
    df, iteration=k_mean(df,X,N)
    df.head()
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

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Rank   Cereal          Cal        Protein   Fat        Sodium    Fiber      Carbs      Sugar      Potassium   step\_1   ecd\_1     step\_2   ecd\_2     step\_3   ecd\_3
  --- ------ --------------- ---------- --------- ---------- --------- ---------- ---------- ---------- ----------- --------- ---------- --------- ---------- --------- ----------
  0   1      ACCheerios      0.545455   0.2       0.666667   0.56250   0.166667   0.452381   0.666667   0.180328    1         0.357373   1         0.278403   1         0.278403
  1   2      Cheerios        0.545455   1.0       0.666667   0.90625   0.222222   0.761905   0.066667   0.295082    2         0.000000   2         0.000000   2         0.000000
  2   3      CocoaPuffs      0.545455   0.0       0.333333   0.56250   0.000000   0.523810   0.866667   0.131148    1         0.379137   1         0.252903   1         0.252903
  3   4      CountChocula    0.545455   0.0       0.333333   0.56250   0.000000   0.523810   0.866667   0.163934    1         0.386160   1         0.251353   1         0.251353
  4   5      GoldenGrahams   0.545455   0.0       0.333333   0.87500   0.000000   0.666667   0.600000   0.098361    5         0.441103   5         0.452937   5         0.454815

</div>
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
6. Using PCA to reduce dimension for 2D plotting:[¶](#6.-Using-PCA-to-reduce-dimension-for-2D-plotting:){.anchor-link} {#6.-Using-PCA-to-reduce-dimension-for-2D-plotting:}
======================================================================================================================

#### Top 2 Principal componenet will be used[¶](#Top-2-Principal-componenet-will-be-used){.anchor-link} {#Top-2-Principal-componenet-will-be-used}
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
    df=pca_retirever(df, X )
    df.head()
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

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

      Rank   Cereal          Cal        Protein   Fat        Sodium    Fiber      Carbs      Sugar      Potassium   step\_1   ecd\_1     step\_2   ecd\_2     step\_3   ecd\_3     pca1       pca2
  --- ------ --------------- ---------- --------- ---------- --------- ---------- ---------- ---------- ----------- --------- ---------- --------- ---------- --------- ---------- ---------- -----------
  0   1      ACCheerios      0.545455   0.2       0.666667   0.56250   0.166667   0.452381   0.666667   0.180328    1         0.357373   1         0.278403   1         0.278403   0.786626   -0.315910
  1   2      Cheerios        0.545455   1.0       0.666667   0.90625   0.222222   0.761905   0.066667   0.295082    2         0.000000   2         0.000000   2         0.000000   0.803633   0.661376
  2   3      CocoaPuffs      0.545455   0.0       0.333333   0.56250   0.000000   0.523810   0.866667   0.131148    1         0.379137   1         0.252903   1         0.252903   0.511342   -0.591776
  3   4      CountChocula    0.545455   0.0       0.333333   0.56250   0.000000   0.523810   0.866667   0.163934    1         0.386160   1         0.251353   1         0.251353   0.527113   -0.584231
  4   5      GoldenGrahams   0.545455   0.0       0.333333   0.87500   0.000000   0.666667   0.600000   0.098361    5         0.441103   5         0.452937   5         0.454815   0.359700   -0.345323

</div>
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
7. Plotting[¶](#7.-Plotting){.anchor-link} {#7.-Plotting}
==========================================
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
    %matplotlib notebook
    anim=plotter(df, iteration, "output_2")
:::
:::
:::
:::

::: {.output_wrapper}
::: {.output}
::: {.output_area}
::: {.prompt}
:::

::: {#053d8045-7c3e-4192-9190-c03cf8345cf0}
:::

::: {.output_subarea .output_javascript}
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
8. Final Results[¶](#8.-Final-Results){.anchor-link} {#8.-Final-Results}
====================================================
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
    df_out=final_answer(df, iteration, "Cereal", "Cereals", "output_2")
    col="step_"+str(iteration-1)
    df_out.groupby([col,"Cereal"]).count()
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

::: {.output_html .rendered_html .output_subarea .output_execute_result}
<div>

</div>
:::
:::
:::
:::
:::
:::
:::

index

step\_3

Cereal

1

ACCheerios

1

CapNCrunch

1

CocoaPuffs

1

CountChocula

1

FrootLoops

1

HoneyGrahamOhs

1

LuckyCharms

1

MueslixCrispyBlend

1

OatmealRaisinCrisp

1

Smacks

1

Trix

1

2

Cheerios

1

3

CornFlakes

1

Crispix

1

Kix

1

NutriGrainWheat

1

Product19

1

RiceKrispies

1

SpecialK

1

TotalCornFlakes

1

4

AllBran

1

Cheaties

1

CracklinOatBran

1

FrostedMiniWheats

1

Life

1

PuffedRice

1

PuffedWheat

1

QuakerOatmeal

1

RaisinNutBran

1

TotalWholeGrain

1

5

AppleJacks

1

CornPops

1

FrostedFlakes

1

FruitfulBran

1

GoldenGrahams

1

HoneyNutCheerios

1

JustRightCrunchyNuggets

1

MultiGrainCheerios

1

NutNHoneyCrunch

1

NutriGrainAlmondRaisin

1

RaisinBran

1

TotalRaisinBran

1

WheatiesHoneyGold

1

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
9. Conclusion[¶](#9.-Conclusion){.anchor-link} {#9.-Conclusion}
==============================================
:::
:::
:::

::: {.cell .border-box-sizing .text_cell .rendered}
::: {.prompt .input_prompt}
:::

::: {.inner_cell}
::: {.text_cell_render .border-box-sizing .rendered_html}
-   It seems that cluster 1 is composed of wheats and grains related
    product
-   CLuster 4 contains puffed items
-   Cluster 3 contains corns an rrice related product
-   Cluster 5 contains breakfast related brans and oatmenals
:::
:::
:::
