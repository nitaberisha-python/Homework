company = input("Enter company name: ")
files = int(input("Enter number of files per day: "))
file_size = float(input("Enter average file size in MB: "))
days = int(input("Enter number of days: "))
price = float(input("Enter price per GB: "))

daily_storage = files * file_size
total_storage_mb = daily_storage * days
total_storage_gb = total_storage_mb / 1024
storage_cost = total_storage_gb * price

print("DATA STORAGE REPORT")
print("Company:", company)
print("Files Per Day:", files)
print("Average File Size:", file_size, "MB")
print("Days:", days)
print("Daily Storage:", daily_storage, "MB")
print("Total Storage:", total_storage_mb, "MB")
print("Total Storage:", total_storage_gb, "GB")
print("Storage Cost:", storage_cost)