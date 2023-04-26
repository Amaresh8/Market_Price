import pandas as pd
df=pd.read_csv("https://archives.nseindia.com/archives/sme/bhavcopy/sme250423.csv")
df1=pd.DataFrame(df)
df1.drop("CORP_IND",axis=1,inplace=True)
df1.to_csv("Market_report_2023-04-27.csv",index=False)
df1.to_json("Market_Price_2023-04-26.json")
df1.to_dict()