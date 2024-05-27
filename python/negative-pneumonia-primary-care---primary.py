# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"7119721000006118","system":"ctv3"},{"code":"7119731000006115","system":"ctv3"},{"code":"7119741000006113","system":"ctv3"},{"code":"301810016","system":"ctv3"},{"code":"7119711000006114","system":"ctv3"},{"code":"219881000006111","system":"ctv3"},{"code":"Hyu0900","system":"ctv3"},{"code":"H22yX00","system":"ctv3"},{"code":"7119711000006114","system":"ctv3"},{"code":"7119731000006115","system":"ctv3"},{"code":"7119741000006113","system":"ctv3"},{"code":"301810016","system":"ctv3"},{"code":"219881000006111","system":"ctv3"},{"code":"7119721000006118","system":"ctv3"},{"code":"H22yX00","system":"ctv3"},{"code":"Hyu0900","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["negative-pneumonia-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["negative-pneumonia-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["negative-pneumonia-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
