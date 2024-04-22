import mysql.connector as sqltor
import csv
import sqlparse
from sql_metadata import Parser

mycon = sqltor.connect(
  host="localhost",
  user="root",
  password="2003",
  database='mysql'
)
if(mycon.is_connected()):
    print(mycon)

cursor=mycon.cursor()
cursor.execute("Select * from general_log ")

log_data=cursor.fetchall()




# # print(len(log_data))
# for row in log_data:
#     row[-1].decode('utf-8')
#     print(row)

with open(r'logfile.csv', 'w', newline='') as outfile :
    writer = csv.writer(outfile,delimiter='#')
    writer.writerows(log_data)

with open(r'C:\Users\LENOVO\Desktop\sql_1\sql_1\logfile.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='#', quotechar='|')

    statements=[]


    for row in reader:
        # print(row)
        # print(len(row))
        if('Query'in row[4]):
            statements.append(row[-1][2:-1])
            # # row1=(', '.join(row))
            # print(row[-1])
            # statements = sqlparse.split(row[-1])
            # # print(statements)
            # statements.append(sqlparse.format(row[-1] , reindent=True, keyword_case='upper'))

# print(len(statements))

for i in range(len(statements)):
    if statements[i][0:2]=="\"\"":
        statements[i]=statements[i][2:-2]    
   
    print(statements[i])



##for the queries --

# print("parsing on sample queries  : \n\n")


with open(r'parsed_data_new.csv', 'w', newline='') as outfile : 
    parsed_data=[['values inserted', 'Columns Used ', 'Tables Used ', ' Subqueries Used ',' Column aliases Used ']]
   
    
    for i in range(4, len(statements)):
        # print(statements[i])
        try:
            
                # print (statements[i],'\n')
                p=Parser(statements[i])
                data=[]
                if ('INSERT' in statements[i]):
                    # print('Values Inserted :- \n',p.values, '\n\n')
                    data.append(p.values)
                else:
                    data.append(' ')
                data.append(p.columns)
                data.append(p.tables)
                data.append(p.subqueries)
                data.append(p.columns_aliases)
                parsed_data.append(data)
        except ValueError:
            continue

    writer = csv.writer(outfile)
    writer.writerows(parsed_data)