import random
import pandas as pd
from datetime import datetime, timedelta

# Constants for input/output paths and thresholds
INPUT_FILES = {
    "daily_transactions": "Daily Household Transactions.csv",
    "credit_card": "credit_card_transaction_flow.csv",
    "digital_wallet": "digital_wallet_transactions.csv",
}
OUTPUT_FILES = {
    "daily_transactions": "output1.csv",
    "credit_card": "output2.csv",
    "digital_wallet": "output3.csv",
}
USD_THRESHOLD = 5
RANDOM_DATE_RANGE = (datetime(2024, 9, 1), datetime(2025, 1, 12))

# Function to generate a random date
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)





def modify_customer_ids(df, column_name='Customer ID', prefix='USER__', limit=200):
    """
    Modifies the Customer IDs in a DataFrame column to ensure all transactions are associated
    with customer IDs between USER__001 and USER__200.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the customer ID column.
        column_name (str): The name of the column with customer IDs.
        prefix (str): The prefix to use for new customer IDs (default is 'USER__').
        limit (int): The maximum number of unique IDs to allow (default is 200).

    Returns:
        pd.DataFrame: DataFrame with modified Customer IDs.
    """
    # Ensure the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    # Generate new IDs up to the limit
    new_ids = [f"{prefix}{str(i).zfill(3)}" for i in range(1, limit + 1)]

    # Limit the number of unique IDs from the original data
    unique_original_ids = df[column_name].drop_duplicates().iloc[:limit]

    # Create a mapping from original IDs to new IDs
    id_mapping = dict(zip(unique_original_ids, new_ids))

    # Assign random valid IDs for any transactions outside the defined range
    def assign_valid_id(current_id):
        if current_id not in id_mapping:
            # Assign a random valid ID if the current ID is not mapped
            return new_ids[random.randint(0, limit - 1)]
        return id_mapping[current_id]

    # Apply the mapping or assign new IDs
    df[column_name] = df[column_name].apply(assign_valid_id)

    return df


def merge_columns_with_space(df, col1, col2, new_col_name):
    """
    Merges the content of two columns in a DataFrame row-wise, separating with a space.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the columns to merge.
        col1 (str): The name of the first column to merge.
        col2 (str): The name of the second column to merge.
        new_col_name (str): The name of the new column to hold the merged content.

    Returns:
        pd.DataFrame: DataFrame with a new column containing the merged content.
    """
    # Ensure the columns exist
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"One or both columns '{col1}' and '{col2}' not found in the DataFrame.")

    # Merge the columns with a space separator
    df[new_col_name] = df[col1].astype(str) + ' ' + df[col2].astype(str)

    return df


# Process Daily Household Transactions
df1 = pd.read_csv(INPUT_FILES["daily_transactions"])
df1 = df1[df1['Subcategory'].notna() & df1['Subcategory'].str.strip().astype(bool)]
df1['Date'] = pd.to_datetime(df1['Date'], errors='coerce')
df1 = df1.dropna(subset=['Date'])
df1['USD'] = pd.to_numeric(df1['USD'], errors='coerce')
df1 = df1[df1['USD'] >= USD_THRESHOLD]
start_date, end_date = (datetime(2024, 12, 12), datetime(2025, 1, 12))
df1['Date'] = [random_date(start_date,end_date).strftime('%Y-%m-%d') for _ in range(len(df1))]
num_users = 20
user_ids = [f"USER__{str(i).zfill(3)}" for i in range(1, num_users + 1)]
df1['User ID'] = (user_ids * (len(df1) // num_users + 1))[:len(df1)]
df1.to_csv(OUTPUT_FILES["daily_transactions"], index=False)
print(f"Filtered data saved to {OUTPUT_FILES['daily_transactions']}")





#########################
#########################
#########################


#2ND DATASET - CREDIT CARD TRANSACTIONS FLOW CSV
# Process Credit Card Transactions
df2 = pd.read_csv(INPUT_FILES["credit_card"])
df2 = merge_columns_with_space(df2,"Name","Surname","FullName")
print(f"Number of unique Customer IDs: {df2['Customer ID'].nunique()}")
print(f"Number of unique Customer IDs: {df2['FullName'].nunique()}")

# Get first 200 unique FullNames and repeat them throughout the dataset
unique_fullnames = df2['FullName'].drop_duplicates().iloc[:200]
df2['FullName'] = pd.Series(unique_fullnames.tolist() * (len(df2) // 200 + 1))[:len(df2)]

num_users = 200
user_ids = [f"USER__{str(i).zfill(3)}" for i in range(1, num_users + 1)]
df2['User ID'] = (user_ids * (len(df2) // num_users + 1))[:len(df2)]

df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')
df2 = df2.dropna(subset=['Date'])
print(f"Date range: {df2['Date'].min().date()} to {df2['Date'].max().date()}")
df2 = modify_customer_ids(df2,column_name='User ID')
start_date, end_date = RANDOM_DATE_RANGE
df2['Date'] = [random_date(start_date,end_date).strftime('%Y-%m-%d') for _ in range(len(df2))]
df2.to_csv(OUTPUT_FILES["credit_card"], index=False)
print(f"Updated data with random dates saved to {OUTPUT_FILES['credit_card']}")



#########################
#########################
#########################


#3RD DATASET - DIGITAL WALLET TRANSACTIONS CSV

# Process Digital Wallet Transactions
df3 = pd.read_csv(INPUT_FILES["digital_wallet"])
print(f"Number of unique User IDs: {df3['user_id'].nunique()}")
df3['transaction_date'] = pd.to_datetime(df3['transaction_date'], errors='coerce')
df3 = df3.dropna(subset=['transaction_date'])
print(f"Date range: {df3['transaction_date'].min().date()} to {df3['transaction_date'].max().date()}")
start_date, end_date = RANDOM_DATE_RANGE
df3['transaction_date'] = [random_date(start_date, end_date).strftime('%Y-%m-%d') for _ in range(len(df3))]
df3 = modify_customer_ids(df3,column_name='user_id')
df3['USD'] = (df3['product_amount'] + df3['transaction_fee']) * 0.012
df3 = df3[df3['transaction_status'] == 'Successful']
df3.to_csv(OUTPUT_FILES["digital_wallet"], index=False)
print(f"Updated data with random dates saved to {OUTPUT_FILES['digital_wallet']}")


# Standardize columns for merging
# For df1: Select and rename required columns
df1 = df1.rename(columns={'Date': 'Transaction Date', 'USD': 'Transaction Amount', 'merchant': 'Merchant', 'User ID': 'User ID'})
df1 = df1[['Transaction Date', 'Transaction Amount', 'Merchant', 'User ID']]

# For df2: Select and rename required columns
df2 = df2.rename(columns={'Date': 'Transaction Date', 'FullName': 'Full Name', 'Merchant Name': 'Merchant', 'User ID': 'User ID'})
df2 = df2[['Transaction Date', 'Full Name', 'User ID', 'Transaction Amount', 'Merchant']]

# For df3: Select and rename required columns
df3 = df3.rename(columns={'transaction_date': 'Transaction Date', 'user_id': 'User ID', 'USD': 'Transaction Amount', 'merchant_name': 'Merchant', 'product_category': 'Product Category'})
df3 = df3[['Transaction Date', 'User ID', 'Transaction Amount', 'Merchant', 'Product Category']]

# Merge all datasets
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# Save the merged dataset
merged_output_path = "merged_transactions.csv"
merged_df.to_csv(merged_output_path, index=False)
print(f"Merged dataset saved to {merged_output_path}")

# Create a mapping of User ID to Full Name from rows where Full Name is available
id_to_fullname = df2[['User ID', 'Full Name']].dropna().drop_duplicates().set_index('User ID')['Full Name'].to_dict()

# Populate Full Name for missing values in the merged dataset
if 'Full Name' not in merged_df.columns:
    merged_df['Full Name'] = None  # Ensure the column exists if not present

merged_df['Full Name'] = merged_df.apply(
    lambda row: id_to_fullname.get(row['User ID'], row['Full Name']),
    axis=1
)

# Save the updated merged dataset
updated_output_path = "merged_transactions_with_fullnames.csv"
merged_df.to_csv(updated_output_path, index=False)
print(f"Updated merged dataset with full names saved to {updated_output_path}")
