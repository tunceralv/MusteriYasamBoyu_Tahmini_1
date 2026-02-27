import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def create_cltv(profit):
    pd.set_option("display.max_columns",None)
    pd.set_option("display.max_rows",None)
    pd.set_option("display.expand_frame_repr", False)  # Alt satıra kaydırma yapma
    pd.set_option("display.float_format",lambda x:"%5f" %x)

    data=pd.read_excel("C:\\Users\\Tuncer\\Desktop\\Desktop\\Data_Science\\CLTV\\Datasets\\online_retail_II.xlsx",sheet_name="Year 2009-2010")
    df=pd.DataFrame(data)

    print(f"Boyut Bilgisi:\n*****\n{df.shape}\n")
    print(f"Eksik Veri Kontrolü:\n*****\n{df.isnull().sum()}\n")
    print(f"Ürün Özelinde Eşşiz Degerler:\n*****\n{df["Description"].nunique()}\n")
    print(f"En Çok Satan Ürünler:\n*****\n{df["Description"].value_counts().head()}\n")

    df.dropna(inplace=True)
    df=df[~df["Invoice"].str.contains("C",na=False)]
    df=df[df["Quantity"]>0]
    df["Toplam_Ucret"]=(df["Quantity"]*df["Price"])

    df_cltv=df.groupby(df["Customer ID"]).agg({"Invoice": lambda invoice:invoice.nunique(),
                                           "Quantity":lambda quantity:quantity.sum(),
                                           "Toplam_Ucret": lambda toplam_ucret: toplam_ucret.sum()})
    
    df_cltv.columns= ["Total_transaction","Total_unit","Total_price"]

    #Avarage order value=Total price/ Total Transacition
    df_cltv['avarage_order_value']=(df_cltv['Total_price']/df_cltv['Total_transaction'])
    df_cltv['purchase_frequency']=(df_cltv['Total_transaction']/df_cltv.shape[0])
    birden_fazla_alisveris_yapan_musteri_sayisi=df_cltv[df_cltv['Total_transaction']>1].shape[0]
    repeat_rate=(birden_fazla_alisveris_yapan_musteri_sayisi/df_cltv.shape[0])
    churn_rate=(1-repeat_rate)
    df_cltv['Profit_margin']=(df_cltv['Total_price']*profit)
    df_cltv['customer_value']=(df_cltv['avarage_order_value']*df_cltv['purchase_frequency'])
    df_cltv['customer_lifetime_value']=((df_cltv['customer_value']/churn_rate)*df_cltv['Profit_margin'])

    df_cltv['segment']=pd.qcut(df_cltv['customer_lifetime_value'],4,labels=['D','C','B','A'])

    print(df_cltv.sort_values(by='customer_lifetime_value',ascending=False).head())
    df_cltv.to_csv('cltv.csv')




create_cltv(profit=0.10)