# script to copy large folders from one external hard drive to another
# when finished, delete origin directory

import shutil, time

origin = r"K:\_archive\Business Client Work\JCarter"
destination = r"J:\_mystuff\media\_thirteen85media\_former\JCarter"

print(f'Started copying from.............. {origin}')
shutil.copytree(origin, destination)
print('Copy Process Complete.')

i = input('Press enter to continue:')

# delete the origin files
print(f'Deleting.............. {origin}')
shutil.rmtree(origin)
print(f'{origin} has been deleted')
