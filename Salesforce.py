from simple_salesforce import Salesforce
import requests
import pandas as pd
from io import StringIO
# Sign into Salesforce

folderPath = r'C:'   # Default folder path for downloaded files
folderDownload = folderPath + '\\Downloads'
fileName = r'Report.csv'
filePath = folderDownload + '\\' + fileName


sf = Salesforce(username='yourusername@domain.com', # Input your SaleForce user here
password='yourpassword', # Input your SalesForce password here
security_token='JDAIVPv9oPCHQwugkk2ZOayw')

# Set report details
sf_org = 'https://domain.my.salesforce.com/' # Input your SalesForce domain here
report_id = '000000000000000000' # Input your SalesForce report ID here
export_params = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'

# Download report
sf_report_url = sf_org + report_id + export_params
response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
new_report = response.content.decode('utf-8')
report_df = pd.read_csv(StringIO(new_report))
report_df['Comentários'] = report_df['Comentários'].str.replace("\n"," . ")
print("Writing File: ")
print(report_df)
report_df.to_csv(filePath, encoding='utf-8')

print("Done.")