#4. Convert a date from yyyy-mm-dd format to dd-mm-yyyy format
def convert_date(date):
    return '-'.join(reversed(date.split('-')))

date = "2023-06-20"
print(convert_date(date))
