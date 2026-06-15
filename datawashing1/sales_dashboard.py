import streamlit as st
import pandas as pd
import plotly.express as px
import os

#page title
st.set_page_config(page_title='销售看板' , layout="wide")
st.title("销售自动化看板")

# 动态定位 CSV 文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "cleaned_sales.csv")

st.sidebar.header("筛选条件")
df_full = pd.read_csv("cleaned_sales.csv")
df_full['InvoiceDate'] = pd.to_datetime(df_full['InvoiceDate'])
min_date = df_full['InvoiceDate'].min().date()
max_date = df_full['InvoiceDate'].max().date()

# --- 侧边栏日期选择（稳定版）---
st.sidebar.header("筛选条件")
start_date = st.sidebar.date_input("开始日期", value=min_date)
end_date = st.sidebar.date_input("结束日期", value=max_date)

# 确保结束日期不小于开始日期
if start_date > end_date:
    st.sidebar.error("开始日期不能晚于结束日期")
    st.stop()

# 把数据加载与过滤分开
df_filtered = df_full[(df_full['InvoiceDate'].dt.date >= start_date) &
                 (df_full['InvoiceDate'].dt.date <= end_date)].copy()
@st.cache_data #缓存数据
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

df = load_data(CSV_PATH)

st.subheader("每日销售额趋势")
#按天聚合销售额
daily_sales = df.resample('D', on='InvoiceDate')['Sales'].sum().reset_index()

#画图
fig_trend = px.line(
    daily_sales,
    x='InvoiceDate',
    y='Sales',
    title= "每日总销售额",
    labels={'InvoiceDate': '日期', 'Sales': "销售额"}
)
fig_trend.update_layout(hovermode='x unified')
st.plotly_chart(fig_trend, use_container_width=True)

st.subheader("TOP 10")
#计算top10
top_products = (
    df.groupby('Description')["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

#横向条形图
fig_top = px.bar(
    top_products,
    x='Sales',
    y='Description',
    orientation='h',
    title='销售额前10商品',
    labels={'Sales': '总销售额' , 'Description':'商品描述'},
    text_auto='.2s'
)
fig_top.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_top, use_container_width=True)

