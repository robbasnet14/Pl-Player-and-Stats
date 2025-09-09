## PL_Data_Scraping.py
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = []  # list to store all team data

# Use headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# Premier League main stats page
url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

# Find the main stats table
tables = soup.find_all('table', class_='stats_table')
if not tables:
    raise Exception("No tables found on the main page. The webpage structure may have changed!")

table = tables[0]

# Get all team squad links
links = table.find_all('a')
links = [l.get("href") for l in links if l.get("href") and '/squads/' in l.get("href")]
team_urls = [f"https://fbref.com{l}" for l in links]

# Loop through each team URL and scrape player stats
for team_url in team_urls:
    team_name = team_url.split("/")[-1].replace("-Stats", "")
    response = requests.get(team_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    stats_tables = soup.find_all('table', class_='stats_table')
    if not stats_tables:
        print(f"No table found for team {team_name}, skipping...")
        continue

    stats = stats_tables[0]

    # Convert to DataFrame
    team_data = pd.read_html(str(stats))[0]
    
    # Some tables have multi-level headers, drop the top level if it exists
    if isinstance(team_data.columns, pd.MultiIndex):
        team_data.columns = team_data.columns.droplevel()

    team_data["Team"] = team_name
    all_teams.append(team_data)

    print(f"Scraped {team_name}")
    time.sleep(5)  # delay to avoid getting blocked

# Combine all teams
stat_df = pd.concat(all_teams, ignore_index=True)

# Clean columns to match your DB
stat_df = stat_df.rename(columns={
    'Player': 'name',
    'Nation': 'nation',
    'Pos': 'pos',
    'Age': 'age',
    'MP': 'mp',
    'Starts': 'starts',
    'Min': 'min',
    'Gls': 'gls',
    'Ast': 'ast',
    'PK': 'pk',
    'CrdY': 'crdy',
    'CrdR': 'crdr',
    'xG': 'xg',
    'xAG': 'xag',
    'Team': 'team'
})

# Optional: keep only the columns used in your database
columns_order = ['name', 'nation', 'pos', 'age', 'mp', 'starts', 'min', 'gls', 'ast', 'pk', 'crdy', 'crdr', 'xg', 'xag', 'team']
stat_df = stat_df[columns_order]

# Save CSV directly to project root so your backend can read it
stat_df.to_csv("../prem_stats_clean.csv", index=False)
print("Saved prem_stats_clean.csv successfully!")
