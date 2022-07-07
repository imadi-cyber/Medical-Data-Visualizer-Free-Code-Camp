import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = 0
condition = (df["weight"]/(df["height"]*0.01)**2)>25
df.loc[condition, 'overweight'] = 1
df.loc[~condition, 'overweight'] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] > 1, "cholesterol"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 0


# Draw Categorical Plot
def draw_cat_plot():
  
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, id_vars = ["cardio"], value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='counts')

    # Draw the catplot with 'sns.catplot()'
  sns.catplot(x="variable", y = "total", hue = "cardio", col = "cardio", kind = "bar", data=df2)



    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  
    # Clean the data
  df1 = df[df['ap_lo'] <= df['ap_hi']]
  df2 = df1[df1['height'] >= df1['height'].quantile(0.025)]
  df3 = df2[df2["height"] <= df2["height"].quantile(0.975)]
  df4 = df3[df3["weight"] >= df3["weight"].quantile(0.025)]
  df_heat = df4[df4["weight"] <= df4["weight"].quantile(0.975)]

    # Calculate the correlation matrix
  corr = df_heat.corr()

    # Generate a mask for the upper triangle
  trimask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
  fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'

  sns.heatmap(corr, mask = trimask, annot=True)

    # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
