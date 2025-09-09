import pandas as pd

# Load the CSV you scraped
df = pd.read_csv("prem_stats_clean_final.csv")

# Inspect column names
print("Original columns:", df.columns.tolist())

# Keep only the columns your table needs
df_clean = df[['name','nation','pos','age','mp','starts','min','gls','ast','pk','crdy','crdr','xg','xag','team']]

# Fix numeric columns
numeric_cols = ['age','mp','starts','min','gls','ast','pk','crdy','crdr','xg','xag']
for col in numeric_cols:
    # Keep only the first number in case of "32-340" or strings
    df_clean[col] = pd.to_numeric(df_clean[col].astype(str).str.extract(r'(\d+\.?\d*)')[0], errors='coerce')

# Drop rows where age or MP is missing (required columns)
df_clean = df_clean.dropna(subset=['age','mp'])

# Save cleaned CSV
df_clean.to_csv("prem_stats_clean_final.csv", index=False)
print("CSV cleaned successfully!")
