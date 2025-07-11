import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title(body = 'Analytical Dashboard')
st.subheader(body = "*Thorough Analysis of AI Job Trends (2024 - 2030)*")
col = st.columns((2 , 4 , 4) , gap = 'medium')
df = pd.read_csv("ai_job_trends_dataset.csv")
df2 = df.round(0)

st.set_page_config(layout="wide")

st.subheader("✍️Raw Data Preview")
st.dataframe(data = df2, hide_index= True , on_select='ignore'  )

color_set = ['#9E0142','#e44f4f','#ffa1a1','#ad7035','#ffc828','#98f5c4','#8ab784','#30980f','#7ebce2','#9388c3']
sns.set_palette(color_set)


with col[0]:
    #1.barplot
    st.markdown("📊 ***Average Median Salary (USD) by Industry***")
    avg_sal = round(df2.groupby('Industry')[['Median Salary (USD)']].mean()) 
    
    sns.set_style({'axes.facecolor' : (0,0,0,0) , 'figure.facecolor':(0.5,0.5,1,0.1),'text.color':'white'})
    fig , ax = plt.subplots(figsize=(18,15))
    sns.barplot(x='Industry' , y = 'Median Salary (USD)' , data = avg_sal , ax = ax , hue = 'Industry' , errorbar='ci'  )
    sns.despine()
    ax.set_title('Average Median Salary (USD) by Industry')
    ax.set_xlabel('Industry').set_color('white')
    ax.set_ylabel('Average Median Salary').set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for container in ax.containers:
        ax.bar_label(container)
    st.pyplot(fig)
    st.caption('Compare how different industries compensate on average.')

    #2.boxplot
    st.markdown("⬜ ***Salary Distribution by Education***")
    sal_dis = df2[['Required Education' , 'Median Salary (USD)']]

    sns.set_style({'axes.facecolor' : (0,0,0,0) , 'figure.facecolor':(0.5,0.5,1,0.1),'text.color':'white'})
    fig , ax = plt.subplots(figsize=(18,15))
    sns.boxplot(x='Required Education' , y = 'Median Salary (USD)' , data = sal_dis , ax = ax ,hue ='Required Education' ,saturation= 1  )
    sns.despine()
    ax.set_title('Salary Distribution by Education')
    ax.set_xlabel('Required Education').set_color('white')
    ax.set_ylabel('Median Salary').set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig)
    st.caption('Observe salary spread for each education level.')


    #3.histogram
    st.markdown('📶 ***Histogram of Gender Diversity in Jobs***')
    fig , ax = plt.subplots(figsize = (18,10))
    sns.histplot(data = df2 , x = 'Gender Diversity (%)', color="#ebff99")
    sns.despine()
    ax.set_title('Histogram of Gender Diversity in Jobs')
    ax.set_xlabel('Gender Diversity (%)').set_color('white')
    ax.set_ylabel('Count').set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig) 
    st.caption('Check representation of genders in jobs')

    #4.piechart
    st.markdown("⚪***Job Distribution by Location***")
    labels = 'Australia' , 'Brazil' , 'Canada' , 'China' , 'Germany','India','UK','USA'
    job_country = df2.groupby('Location')[['Job Openings (2024)']].mean()
    fig ,ax = plt.subplots(figsize=(15,15))
    plt.pie(job_country['Job Openings (2024)'], labels = labels , autopct='%1.1f%%' , startangle=140 )
    centre_circle = plt.Circle((0,0),0.70,fc="#272748")
    fig.gca().add_artist(centre_circle)
    plt.axis('equal')
    st.pyplot(fig)
    st.caption('Country-wise job availability.')

    

with col[1]:
    #1.pairplot
    st.markdown(' 📈 ***Pairwise Relationships Between Numeric Job Attributes***')
    pplot = df2[['Industry','Median Salary (USD)','Experience Required (Years)','Projected Openings (2030)','Remote Work Ratio (%)']]
    fig = sns.pairplot(data = pplot.sample(250, random_state=42) , hue = 'Industry' , markers=['o','s','D'] , diag_kws=dict(fill=False))
    for ax in fig.axes[-1, :]:  # Bottom row of axes (x-axis labels)
        ax.set_xlabel(ax.get_xlabel(), color='white')
    for ax in fig.axes[:, 0]:
        ax.set_ylabel(ax.get_ylabel(), color='white')
    fig.tick_params(axis='x', colors='white')
    fig.tick_params(axis='y', colors='white')
    st.pyplot(fig) 
    st.caption('Explore all pairwise relations in numerical data (e.g., salary vs automation risk)')

    #2.heatmap
    st.markdown('❇️***Correlation Matrix of Numerical Job Attributes***')
    set2 = ["#FA5454" , "#FE9749" , "#C5FF69" , "#76FACE"]
    heat = df2.drop(columns=['Industry','Job Title','Job Status','AI Impact Level','Required Education','Location'])
    corr = heat.corr()
    fig , ax = plt.subplots(figsize=(20,15))
    sns.heatmap(corr, annot = True  ,cmap = set2 , fmt=".2f" , vmin = 0 , vmax = 1 , linewidths=0.5)
    ax.set_title('Correlation Matrix of Numerical Job Attributes')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig)
    st.caption('Find which variables are strongly related (e.g. experience & salary).')

    #3.violinplot
    st.markdown("🔶***Median Salary Distribution across AI Impact Levels***")
    fig , ax = plt.subplots(figsize=(20,15))
    sns.violinplot( x='AI Impact Level' , y = 'Median Salary (USD)' , hue = 'Industry' , data = df2 )
    sns.despine()
    ax.set_title("Median Salary Distribution across AI Impact Levels")
    for ax in fig.axes[-3:]:  # Bottom row of axes (x-axis labels)
        ax.set_xlabel(ax.get_xlabel(), color='white')
    for ax in fig.axes[0:]:
        ax.set_ylabel(ax.get_ylabel(), color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    
    st.pyplot(fig) 
    st.caption(' How AI impact is associated with salaries.')

with col[2]:
    #1.facetgrid
    st.markdown("▶️***Remote Work Ratio by Education in Each Industry***")
   
    fig = sns.catplot(data = df2 ,kind = 'boxen', y = 'Required Education' , x = 'Remote Work Ratio (%)' ,col = 'Industry' ,col_wrap=4, height = 5 , aspect = 0.6 )
    plt.subplots_adjust(wspace = 0.2 , hspace=0.2)
    for ax in fig.axes[-4:]:  # Bottom row of axes (x-axis labels)
        ax.set_xlabel(ax.get_xlabel(), color='white')
    for ax in fig.axes[0:]:
        ax.set_ylabel(ax.get_ylabel(), color='white')
    fig.tick_params(axis='x', colors='white')
    fig.tick_params(axis='y', colors='white')
    st.pyplot(fig)
    st.caption('Education level’s effect on remote capability per industry.')


    #2.lineplot
    st.markdown('📈 ***2024 vs 2030 Job Openings by Industry***')
    fig , ax = plt.subplots(figsize=(20,15))
    sns.lineplot(x='Job Openings (2024)' , y = 'Projected Openings (2030)' , hue = 'Industry' , data = df2.sample(250 , random_state=42))
    sns.despine()
    ax.set_title("2024 vs 2030 Job Openings by Industry")
    ax.set_xlabel('Job Openings (2024)').set_color('white')
    ax.set_ylabel('Projected Openings (2030)').set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig)
    st.caption('See how job demand is expected to grow.')

    #3.scatterplot
    st.markdown('🟠 ***Remote Work vs Automation Risk Colored by AI Impact***')
    fig , ax = plt.subplots(figsize=(20,15))
    sns.scatterplot(x='Remote Work Ratio (%)' , y = 'Automation Risk (%)' , hue = 'AI Impact Level' , data = df2.sample(10000, random_state=42))
    sns.despine()
    ax.set_title("Remote Work vs Automation Risk Colored by AI Impact")
    ax.set_xlabel('Remote Work Ratio (%)').set_color('white')
    ax.set_ylabel('Automation Risk (%)').set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig)
    st.caption('Jobs with high automation risk may or may not be remote-friendly.')
    
