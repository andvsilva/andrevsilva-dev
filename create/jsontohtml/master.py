import os

# number article
papernumber = 14

message = f'''##############################
Creating the structure to publish the
article in my webpage.             
# paper number = {papernumber}
##############################
'''

print(message)

# run each step, please.
os.system('python3 genjsontopaper.py')
os.system(f'python3 headindex.py {papernumber}')
os.system(f'python3 papertohtml.py {papernumber}')