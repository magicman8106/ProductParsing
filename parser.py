import os
import csv

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
def printDict(d):
    assert isinstance(d,dict)
    for k in d.keys():
        print(k,' ',d[k][0],' ',d[k][1])
def writeDict(d):
    assert isinstance(d,dict)
    OUTPUT_PATH=os.path.join(BASE_DIR,'output\output.csv')
    with open(OUTPUT_PATH, 'w') as out:
        writer=csv.writer(out)
        for k in d.keys():
            writer.writerow([k,d[k][0],d[k][1]])
def main():
    FILE_PATH=os.path.join(BASE_DIR,"raw_data.csv")
    dict={}
    try:
        with open(FILE_PATH) as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                    
                tup=(row[0][row[0].rindex('/')+1:],row[1][row[1].rindex('/')+1:])
                k=row[0]
                dict.update({k:tup})
                csv_file.close()
        csv_file.close()
        writeDict(dict)
    except ValueError as e:
                pass
if __name__=="__main__":
    main()