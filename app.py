import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Vehicles Exploratory Data Analysis')

df = pd.read_csv('vehicles_us.csv')

df['model_year'] = df['model_year'].fillna('Unknown')
df['cylinders'] = df['cylinders'].fillna('Unknown')
df['paint_color'] = df['paint_color'].fillna('Unknown')

df['odometer'] = df['odometer'].fillna('Unknown')

df['is_4wd']=df['is_4wd'].fillna(0)
df['is_4wd'] = df['is_4wd'].astype('int')
df['date_posted']=pd.to_datetime(df['date_posted'], format = '%Y-%m-%d')

turn_over=[]
def turnover(days):
   
    
    for item in days:
        if item <= 75:
            item = 'short'
            turn_over.append(item)
        elif item > 75 and item <= 150:
            item = 'medium'
            turn_over.append(item)
        elif item > 150:
            item = 'Long'
            turn_over.append(item)

turnover(df['days_listed'])
df['turnover_rate'] = turn_over
df.head()

group2 = df.groupby(['turnover_rate','days_listed'])['price'].mean().reset_index()

df_turnover = df.groupby('turnover_rate')['price']


checked  = st.checkbox("Color by Turnover Rate")

if checked:
    
    fig4 = px.scatter(group2, x='days_listed', y='price', color='turnover_rate', title = 'Price vs duration a vehicle is listed for')
    fig4.update_layout(xaxis_title = 'Days Listed', yaxis_title = 'Average Price')
    
    fig5 = px.scatter(df, x = 'days_listed', y='condition', color='turnover_rate', title = 'Condition vs duration a vehicle is listed for')
    fig5.update_layout(xaxis_title = 'Days Listed', yaxis_title = 'Condition of Vehicle')

else:

    fig4 = px.scatter(group2, x='days_listed', y='price', title = 'Price vs duration a vehicle is listed for')
    fig4.update_layout(xaxis_title = 'Days Listed', yaxis_title = 'Average Price')

    fig5 = px.scatter(df, x = 'days_listed', y='condition', title = 'Condition vs duration a vehicle is listed for')
    fig5.update_layout(xaxis_title = 'Days Listed', yaxis_title = 'Condition of Vehicle')


st.write('Relation of Price to how long a vehicle is listed for.')
st.plotly_chart(fig4)

st.write('How condition effects a vehicles turnover rate')
st.plotly_chart(fig5)




    
    





