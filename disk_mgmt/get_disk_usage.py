import shutil

# specify path
path = 'J:/'

def get_disk_usage(path):
     # get stats
     total, used, free = shutil.disk_usage(path)

     # print
     print(f"Total: {total/(10**9)} GB")
     print(f"Used: {used/(10**9)} GB")
     print(f"Free: {free/(10**9)} GB")

get_disk_usage(path)