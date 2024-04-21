ata.csv', 'w', newline='') as outfile : 
    parsed_data=[['values inserted', 'Columns Used ', 'Tables Used ', ' Tables Used ',' Column aliases Used ']]
   
    
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
    writer.write