from preswald import text, plotly, connect, get_df, table, query, slider, sidebar
import pandas as pd
import plotly.express as px

sidebar(defaultopen=True)

text("# Welcome to Liqin's Preswald!")
text("This is Liqin's first preswald app. 🎉")
text("## All data")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('wine_csv')
# Show the data
table(df)

text("## Filtered data - quality > 5")
sql = "SELECT density,pH,sulphates,alcohol,quality FROM wine_csv WHERE quality > 6"
filtered_df = query(sql, "wine_csv")
table(filtered_df, title="High Quality Wine")

text("## Filtered data with slider based on quality")
qualityView = slider("Quality", min_val=3, max_val=8, step=1, default=5)
table(df[df["quality"] > qualityView], title="Dynamic Data View - Quality")

# Create a scatter plot
text("## Scatter Plot - Quality vs alcohol")
fig1 = px.scatter(df, x='alcohol', y='quality', 
                 title='Alcohol vs. Quality',
                 labels={'alcohol': 'Alcohol', 'quality': 'Quality'})

# Add labels for each point
fig1.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
# Style the plot
fig1.update_layout(template='plotly_white')

plotly(fig1)

text("## Scatter Plot - Quality vs PH")
fig2 = px.scatter(df, x='pH', y='quality', 
                 title='PH vs. Quality',
                 labels={'pH': 'PH', 'quality': 'Quality'})
fig2.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig2.update_layout(template='plotly_white')
plotly(fig2)

text("## Scatter Plot - density vs PH")
fig3 = px.scatter(df, x='density', y='quality', 
                 title='Density vs. Quality',
                 labels={'density': 'Density', 'quality': 'Quality'})
fig3.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig3.update_layout(template='plotly_white')
plotly(fig3)
