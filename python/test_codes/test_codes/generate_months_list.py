# from datetime import datetime

# today = datetime.now()

# number_of_installments = 7

# months_to_search_example = {"2022": 10, "2022": 11, "2022": 12, "2023": 1,"2023": 2}

# year = today.year
# print(year, today.month)


# for i in range(1, number_of_installments):
#     if today.month + i > 12:
#         print(year + 1)
#     else:
#         print(year ,today.month + i)


# Python3 code to demonstrate working of
# Get Construct Next K dates List
# Using timedelta() + list comphehension
from datetime import datetime, timedelta
  
# initializing date
test_date = datetime.now()
               
  
# initializing K 
K = 12
  
# timedelta() gets successive dates with 
# appropriate difference
date = datetime.now()
res = [date = date + timedelta(days=30) for idx in range(K)]
  
# printing result
for i in res:
    print(i)

print("--------------------------------")
date = datetime.now()
for i in range(K):
    date = date + timedelta(days=30)
    print(date.strftime("%Y-%m"))