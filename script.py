from etl import extract, transform, avg_monthly_sales, load, validation
import pandas

df = extract('grocery_sales.csv', 'extra_data.parquet')

df = transform(df)

df_holiday = avg_monthly_sales(df)

df = load(df, df_holiday)

validation('./clean_data.csv')
validation('./agg_data.csv')