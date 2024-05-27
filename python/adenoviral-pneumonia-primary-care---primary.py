# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"H20..","system":"ctv3"},{"code":"301814013","system":"ctv3"},{"code":"301364012","system":"ctv3"},{"code":"546491000006118","system":"ctv3"},{"code":"3163841000006112","system":"ctv3"},{"code":"301363018","system":"ctv3"},{"code":"301809014","system":"ctv3"},{"code":"125510013","system":"ctv3"},{"code":"H20y.00","system":"ctv3"},{"code":"H20z.00","system":"ctv3"},{"code":"Hyu0D00","system":"ctv3"},{"code":"H20..11","system":"ctv3"},{"code":"Hyu0800","system":"ctv3"},{"code":"H20..00","system":"ctv3"},{"code":"301809014","system":"ctv3"},{"code":"546491000006118","system":"ctv3"},{"code":"301364012","system":"ctv3"},{"code":"3163841000006112","system":"ctv3"},{"code":"301814013","system":"ctv3"},{"code":"301363018","system":"ctv3"},{"code":"125510013","system":"ctv3"},{"code":"H20y.00","system":"ctv3"},{"code":"H20..00","system":"ctv3"},{"code":"Hyu0D00","system":"ctv3"},{"code":"Hyu0800","system":"ctv3"},{"code":"H20z.00","system":"ctv3"},{"code":"H20..11","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["adenoviral-pneumonia-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["adenoviral-pneumonia-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["adenoviral-pneumonia-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
