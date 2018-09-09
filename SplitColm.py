with open(r"C:\Users\arunt.LAPTOP-H8LKFSEI\Desktop\hive_assignment.csv",'r') as inputfile:
    file1=inputfile.readlines()
    with open(r'C:\Users\arunt.LAPTOP-H8LKFSEI\Desktop\output.csv','w') as outputfile:
        output=outputfile.write("Name,Country,Year,Season")
        print(output)
    for line in file1[1:]:
        col1=line.split(",")
        #print(col1)
        col2=col1[2]
        #print(col2)
        col3=col2.split(" ")
        print(col3)
        #col4=col3[0]
        #print(col4)
        col5=col3[1:]
        print(col5)
        str_output_row = col1[0]+ "," +col1[1] + "," + col1[3] + "," + col1[5]
        with open(r'C:\Users\arunt.LAPTOP-H8LKFSEI\Desktop\output.csv','a') as outputfile:
            output=outputfile.write(str_output_row)
            print(output)
    
