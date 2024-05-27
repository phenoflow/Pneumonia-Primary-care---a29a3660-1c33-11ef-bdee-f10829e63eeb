# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"1231963019","system":"ctv3"},{"code":"885221000006117","system":"ctv3"},{"code":"3465971000006110","system":"ctv3"},{"code":"H243.00","system":"ctv3"},{"code":"H243.99","system":"ctv3"},{"code":"1231963019","system":"ctv3"},{"code":"885221000006117","system":"ctv3"},{"code":"3465971000006110","system":"ctv3"},{"code":"H243.00","system":"ctv3"},{"code":"H243.99","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-primary-care-cough---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-primary-care-cough---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-primary-care-cough---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
