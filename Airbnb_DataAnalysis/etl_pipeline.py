import sqlite3
import pandas as pd

# Extract data from the excel sheet using pandas for price/night analysis based on the neighbourhood.
# Only need host information, listing address and prices/night for that, so removing the remaining
# column.
airbnb_dict = pd.read_csv("datacamp_workspace_export_austin_2023-03-28 19_40_27.csv")

# Transform the data by dropping the unnecessary fields
airbnb_dict_price_analysis = airbnb_dict.drop(columns=['minimum_nights', 'number_of_reviews', 'last_review',
                                                       'reviews_per_month',  'calculated_host_listings_count',
                                                       'availability_365', 'number_of_reviews_ltm', 'license'])

# Load it in the database

# Created a database to store entries for Austin listing
db_obj = sqlite3.connect("airbnb_austin_listing.db")

db_obj.execute('''CREATE TABLE IF NOT EXISTS airbnb_austin_price_analysis (
                    'name',
                    'host_id',
                    'host_name',
                    'neighbourhood_group',
                    'neighbourhood',
                    'latitude',
                    'longitude',
                    'room_type',
                    'price');''')

airbnb_dict_price_analysis.to_sql(name='airbnb_austin_price_analysis', con=db_obj, if_exists='append', index=False)
db_obj.commit()

# Retrieve the database if needed
#r_df = pd.read_sql("select * from airbnb_austin_price_analysis", db_obj)

db_obj.close()
