import csv
import sqlparse
from sql_metadata import Parser

statements=[]

with open(r'C:\Users\LENOVO\Desktop\sql_1\sql_1\output2.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    
    for row in reader:
        # # print (row) 
        # # row1=(', '.join(row))
        # print(row[-1])
        # statements = sqlparse.split(row[-1])
        # print(statements)
        statements.append(sqlparse.format(row[-1], reindent=True, keyword_case='upper'))



##for the queries --

print("parsing on sample queries  : \n\n")

for i in range(-1,-20,-1):
    print (statements[i],'\n')
    p=Parser(statements[i])
    if ('INSERT' in statements[i]):
        print('Values Inserted :- \n',p.values, '\n\n')

    print('Columns Used :- \n',p.columns, '\n\n')
    print('Tables Used :- \n',p.tables, '\n\n')
    print('Subqueries Used :- \n',p.subqueries, '\n\n')
    print('Column aliases Used :- \n',p.columns_aliases, '\n\n')


# raw = 'select * from foo; select * from bar;'
# statements = sqlparse.split(raw)
# print(statements)

# first = statements[0]
# print(sqlparse.format(first, reindent=True, keyword_case='upper'))
# print(sqlparse.parse('select * from foo'))
