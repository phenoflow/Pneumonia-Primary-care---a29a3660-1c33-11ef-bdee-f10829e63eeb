# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"H270.","system":"ctv3"},{"code":"H2y..","system":"ctv3"},{"code":"H2z..","system":"ctv3"},{"code":"H270z","system":"ctv3"},{"code":"H202.","system":"ctv3"},{"code":"H2700","system":"ctv3"},{"code":"XE0ZF","system":"ctv3"},{"code":"H2...","system":"ctv3"},{"code":"546421000006115","system":"ctv3"},{"code":"885271000006116","system":"ctv3"},{"code":"12721231000006111","system":"ctv3"},{"code":"301430012","system":"ctv3"},{"code":"301414016","system":"ctv3"},{"code":"3555881000006117","system":"ctv3"},{"code":"778871000006116","system":"ctv3"},{"code":"3164871000006118","system":"ctv3"},{"code":"3555901000006115","system":"ctv3"},{"code":"301357010","system":"ctv3"},{"code":"1229740013","system":"ctv3"},{"code":"301431011","system":"ctv3"},{"code":"885251000006114","system":"ctv3"},{"code":"H270z00","system":"ctv3"},{"code":"H270.99","system":"ctv3"},{"code":"H270000","system":"ctv3"},{"code":"H2z..00","system":"ctv3"},{"code":"H270.11","system":"ctv3"},{"code":"H2z..99","system":"ctv3"},{"code":"H270.00","system":"ctv3"},{"code":"H2y..00","system":"ctv3"},{"code":"H2...00","system":"ctv3"},{"code":"H2y..","system":"ctv3"},{"code":"H202.","system":"ctv3"},{"code":"H2...","system":"ctv3"},{"code":"XE0ZF","system":"ctv3"},{"code":"H2700","system":"ctv3"},{"code":"H270.","system":"ctv3"},{"code":"H2z..","system":"ctv3"},{"code":"H270z","system":"ctv3"},{"code":"3164871000006118","system":"ctv3"},{"code":"1229740013","system":"ctv3"},{"code":"546421000006115","system":"ctv3"},{"code":"12721231000006111","system":"ctv3"},{"code":"885251000006114","system":"ctv3"},{"code":"301414016","system":"ctv3"},{"code":"3555881000006117","system":"ctv3"},{"code":"778871000006116","system":"ctv3"},{"code":"301357010","system":"ctv3"},{"code":"3555901000006115","system":"ctv3"},{"code":"885271000006116","system":"ctv3"},{"code":"301430012","system":"ctv3"},{"code":"301431011","system":"ctv3"},{"code":"H2...00","system":"ctv3"},{"code":"H270z00","system":"ctv3"},{"code":"H2z..99","system":"ctv3"},{"code":"H270.00","system":"ctv3"},{"code":"H2z..00","system":"ctv3"},{"code":"H270.99","system":"ctv3"},{"code":"H270000","system":"ctv3"},{"code":"H2y..00","system":"ctv3"},{"code":"H270.11","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-primary-care-parainfluenzal---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-primary-care-parainfluenzal---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-primary-care-parainfluenzal---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
