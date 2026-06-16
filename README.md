# 📊 电商销售自动化数据分析项目

> **从原始数据清洗，到自动分析报告，再到交互式Web看板——全流程 Python 自动化实战。**

本项目以某英国在线零售商的真实交易数据为基础，完整展示了一个数据分析师如何利用 Python 自动化地完成：
- 数据读取与清洗（处理缺失值、异常退货记录）
- 一键生成专业数据分析报告（基于 `ydata-profiling`）
- 构建可交互的 Streamlit 网页看板（展示每日销售趋势、畅销商品等）

---

## ✨ 项目亮点

- **全流程自动化**：只需提供原始 CSV，即可自动输出 HTML 报告和 Web 看板
- **真实业务场景**：数据包含客户、时间、商品、金额，完美模拟电商分析需求
- **专业级报告**：`ydata-profiling` 生成的报告涵盖统计分布、相关性、缺失值、时间序列等
- **可交付成果**：生成的报告和看板可直接发送给客户，无需对方安装任何软件
- **低代码复用**：替换数据文件后，稍作修改即可用于其他行业的分析

---

## 🛠️ 技术栈

- **Python 3.8+**
- **Pandas**：数据处理与清洗
- **NumPy**：数值计算
- **ydata-profiling**：自动生成数据报告
- **Streamlit**：构建交互式 Web 仪表板
- **Plotly**：交互式可视化图表
- **Jupyter Notebook**：分步记录清洗与分析过程

---

### 1. 环境准备
确保已安装 Python 3.8 以上版本。克隆本仓库后，在项目根目录执行：
bash
pip install -r requirements.txt
### 2. 获取数据
数据来源于 Kaggle 的 E-Commerce Data（英国某在线零售商的真实交易记录）。
你可以从以下地址下载原始 CSV 文件：

Kaggle - E-Commerce Data

下载后，将文件命名为 ecommerce.csv 放入项目根目录，然后运行 Jupyter Notebook 执行清洗并生成 cleaned_sales.csv。

或者，如果你已经有清洗好的数据，直接使用 cleaned_sales.csv 并跳过 Notebook 中的清洗步骤。

### 3. 运行数据清洗与自动报告
bash
jupyter notebook data_analysis.ipynb
按照 Notebook 中的步骤执行，将会：

读取原始数据

处理缺失值、去除退货记录（数量/单价为负）

创建销售额字段

生成 cleaned_sales.csv

自动输出 report.html 分析报告

### 4. 启动 Streamlit 看板
bash
streamlit run sales_dashboard.py
浏览器将自动打开本地看板页面，你可以：

通过侧边栏选择日期范围

查看每日总销售额趋势图

查看销售额 TOP10 畅销商品

查看关键 KPI 卡片（总销售额、订单数、商品数）

此为通过streamlit进行部署的网站：
## https://datawashing-for-11.streamlit.app/
