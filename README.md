# MusteriYasamBoyu_Tahmini_1
This project calculates Customer Lifetime Value (CLTV) using the Online Retail II dataset (2009–2010).

📌 Project Purpose

The main objective is to estimate the long-term value of customers based on their historical transaction behavior and segment them accordingly.

⚙️ Methodology

The following steps were applied:

Data preprocessing (removing missing values, cancellations, negative quantities)

Feature engineering:

Total transaction

Total unit

Total revenue

Average order value

Purchase frequency

Repeat rate & churn rate

Profit margin

CLTV calculation using a simplified formula

Customer segmentation using quartiles (A, B, C, D)

📊 CLTV Formula
CLTV=(Customer ValueChurn Rate)×Profit Margin
CLTV=(
Churn Rate
Customer Value
	​

)×Profit Margin
🧩 Output

Customers ranked by CLTV

Segmentation into 4 groups:

A → Highest value customers

D → Lowest value customers

Exported result as cltv.csv

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn
