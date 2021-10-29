import gspread
from oauth2client.service_account import ServiceAccountCredentials

# credential GCP spred drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credential = ServiceAccountCredentials.from_json_keyfile_name(
    'auth/active-chimera-330406-5d2c982b26f0.json', scope)
# googleSpredShhet
gspreadInstance = gspread.authorize(credential)
SPREADSHEET_KEY = '1ort9NT8SHo44Sfd7cFYCRIcQCehAH99cCDXab32sr4Q'
worksheet = gspreadInstance.open_by_key(SPREADSHEET_KEY).worksheet(
    'シート2')
print(worksheet.acell('A1').value)
