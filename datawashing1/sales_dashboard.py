import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 页面配置
st.set_page_config(page_title='销售看板', layout="wide")
st.title("销售自动化看板")

# 动态定位 CSV 文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "cleaned_sales.csv")

# 缓存数据加载
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Sales'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data(CSV_PATH)   # 所有数据都在这里

# --- 侧边栏日期选择 ---
st.sidebar.header("筛选条件")
min_date = df['InvoiceDate'].min().date()
max_date = df['InvoiceDate'].max().date()

start_date = st.sidebar.date_input("开始日期", value=min_date)
end_date = st.sidebar.date_input("结束日期", value=max_date)

if start_date > end_date:
    st.sidebar.error("开始日期不能晚于结束日期")
    st.stop()

# 日期过滤
df_filtered = df[(df['InvoiceDate'].dt.date >= start_date) &
                 (df['InvoiceDate'].dt.date <= end_date)]

# --- 每日销售额趋势 ---
st.subheader("每日销售额趋势")
daily_sales = df_filtered.resample('D', on='InvoiceDate')['Sales'].sum().reset_index()

fig_trend = px.line(
    daily_sales,
    x='InvoiceDate',
    y='Sales',
    title="每日总销售额",
    labels={'InvoiceDate': '日期', 'Sales': '销售额'}
)
fig_trend.update_layout(hovermode='x unified')
st.plotly_chart(fig_trend, use_container_width=True)

# --- TOP10 畅销商品 ---
st.subheader("TOP10")
top_products = (
    df_filtered.groupby('Description')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_top = px.bar(
    top_products,
    x='Sales',
    y='Description',
    orientation='h',
    title='销售额前10商品',
    labels={'Sales': '总销售额', 'Description': '商品描述'},
    text_auto='.2s'
)
fig_top.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_top, use_container_width=True)

# 指标卡片
col1, col2, col3 = st.columns(3)
col1.metric("总销售额", f"${df_filtered['Sales'].sum():,.0f}")
col2.metric("订单数", f"{len(df_filtered):,}")
col3.metric("活跃商品数", f"{df_filtered['Description'].nunique():,}")