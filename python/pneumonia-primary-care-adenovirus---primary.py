# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"H2701","system":"ctv3"},{"code":"219801000006119","system":"ctv3"},{"code":"2622081000006118","system":"ctv3"},{"code":"301413010","system":"ctv3"},{"code":"301362011","system":"ctv3"},{"code":"3555891000006119","system":"ctv3"},{"code":"3555871000006115","system":"ctv3"},{"code":"1232627018","system":"ctv3"},{"code":"4781131000006116","system":"ctv3"},{"code":"H202.00","system":"ctv3"},{"code":"H270100","system":"ctv3"},{"code":"H200.00","system":"ctv3"},{"code":"H201.00","system":"ctv3"},{"code":"H2701","system":"ctv3"},{"code":"1232627018","system":"ctv3"},{"code":"219801000006119","system":"ctv3"},{"code":"301362011","system":"ctv3"},{"code":"2622081000006118","system":"ctv3"},{"code":"301413010","system":"ctv3"},{"code":"3555871000006115","system":"ctv3"},{"code":"3555891000006119","system":"ctv3"},{"code":"4781131000006116","system":"ctv3"},{"code":"H201.00","system":"ctv3"},{"code":"H270100","system":"ctv3"},{"code":"H200.00","system":"ctv3"},{"code":"H202.00","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-primary-care-adenovirus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-primary-care-adenovirus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-primary-care-adenovirus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
