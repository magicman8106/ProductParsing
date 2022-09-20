import os
import csv
BASE_DIR=os.path.dirname(os.path.realpath(__file__))
def parse_out_num(list):
    ret_list=[]
    for i in list:
        for j, c in enumerate(i):
            if c.isdigit():
                ret_list.append((i[0:j+1]+'.html',i[0:j-1]+'.html'))
                break
    return ret_list
def main():
    try:
        FILE_PATH=os.path.join(BASE_DIR,'input.csv')
        output_dict={}
        urlList=[]
        input=[]
        with open(FILE_PATH) as csv_file:
            csv_reader =csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                urlList.append(row[0])
                input.append(row[0][row[0].rindex('/')+1:])
            csv_file.close()
        input=parse_out_num(input)
        for i in range(0,len(urlList)):
            output_dict.update({urlList[i]:input[i]})

    except Exception as e:
        print(e)
    try:
        OUTPUT_PATH=os.path.join(BASE_DIR,'output\single_output.csv')
        with open(OUTPUT_PATH,'w') as out:
            writer=csv.writer(out)
            for k in output_dict.keys():
                writer.writerow([k,output_dict[k][0],output_dict[k][1]])
        out.close()

    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()