import plotly.express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", y="tip", histfunc='avg')
fig.show()