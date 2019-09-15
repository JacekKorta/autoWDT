import shelve

shelve_file = shelve.open('customer_db')
with open('eksportowi.txt','r') as file:
    for line in file:
        code, prefix, number = line.split(';')
        number = number.replace('\n','').replace(' ','')
        shelve_file[code] = (prefix, number)
shelve_file.close()
