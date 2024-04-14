import csv
import sqlparse

with open(r'C:\Users\LENOVO\Desktop\sql_1\sql_1\output.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    
    for row in reader:
        # # print (row) 
        # # row1=(', '.join(row))
        # print(row[-1])
        # statements = sqlparse.split(row[-1])
        # print(statements)
        print(sqlparse.format(row[-1], reindent=True, keyword_case='upper'))
        print("\n\n")

# raw = 'select * from foo; select * from bar;'
# statements = sqlparse.split(raw)
# print(statements)

# first = statements[0]
# print(sqlparse.format(first, reindent=True, keyword_case='upper'))
# print(sqlparse.parse('select * from foo'))
