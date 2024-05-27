# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"301818011","system":"ctv3"},{"code":"301408011","system":"ctv3"},{"code":"546481000006116","system":"ctv3"},{"code":"396105015","system":"ctv3"},{"code":"546441000006110","system":"ctv3"},{"code":"12728631000006117","system":"ctv3"},{"code":"12728461000006112","system":"ctv3"},{"code":"301377015","system":"ctv3"},{"code":"301382010","system":"ctv3"},{"code":"301409015","system":"ctv3"},{"code":"H26..00","system":"ctv3"},{"code":"H26..11","system":"ctv3"},{"code":"H260.00","system":"ctv3"},{"code":"Hyu0H00","system":"ctv3"},{"code":"H23..00","system":"ctv3"},{"code":"H23z.00","system":"ctv3"},{"code":"H25..11","system":"ctv3"},{"code":"H25..00","system":"ctv3"},{"code":"301382010","system":"ctv3"},{"code":"301408011","system":"ctv3"},{"code":"546441000006110","system":"ctv3"},{"code":"12728461000006112","system":"ctv3"},{"code":"301818011","system":"ctv3"},{"code":"12728631000006117","system":"ctv3"},{"code":"396105015","system":"ctv3"},{"code":"301409015","system":"ctv3"},{"code":"301377015","system":"ctv3"},{"code":"546481000006116","system":"ctv3"},{"code":"H23z.00","system":"ctv3"},{"code":"H260.00","system":"ctv3"},{"code":"H26..00","system":"ctv3"},{"code":"H25..00","system":"ctv3"},{"code":"H23..00","system":"ctv3"},{"code":"H26..11","system":"ctv3"},{"code":"Hyu0H00","system":"ctv3"},{"code":"H25..11","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-primary-care-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-primary-care-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-primary-care-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
