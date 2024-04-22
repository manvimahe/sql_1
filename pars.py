import csv
import sqlparse
from sql_metadata import Parser

statements=[]

with open(r'C:\Users\LENOVO\Desktop\sql_1\sql_1\output2.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')

    
   
    for row in reader:
        if(len(row)>1 and 'Query'in row[-2]):
            # # row1=(', '.join(row))
            # print(row[-1])
            # statements = sqlparse.split(row[-1])
            # print(statements)
            statements.append(sqlparse.format(row[-1], reindent=True, keyword_case='upper'))

# print(len(statements))



##for the queries --

# print("parsing on sample queries  : \n\n")


with open(r'parsed_data.csv', 'w', newline='') as outfile : 
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

        # print('Columns Used :- \n',p.columns, '\n\n')
        # print('Tables Used :- \n',p.tables, '\n\n')
        # print('Tables Used :- \n',p.subqueries, '\n\n')
        # print('Column aliases Used :- \n',p.columns_aliases, '\n\n')


# raw = 'select * from foo; select * from bar;'
# statements = sqlparse.split(raw)
# print(statements)

# first = statements[0]
# print(sqlparse.format(first, reindent=True, keyword_case='upper'))
# print(sqlparse.parse('select * from foo'))
