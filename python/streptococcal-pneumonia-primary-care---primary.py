# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"3047831000006110","system":"ctv3"},{"code":"56816017","system":"ctv3"},{"code":"4781141000006114","system":"ctv3"},{"code":"1760561000006116","system":"ctv3"},{"code":"219991000006118","system":"ctv3"},{"code":"3047811000006116","system":"ctv3"},{"code":"H223000","system":"ctv3"},{"code":"H223.00","system":"ctv3"},{"code":"219991000006118","system":"ctv3"},{"code":"3047811000006116","system":"ctv3"},{"code":"56816017","system":"ctv3"},{"code":"1760561000006116","system":"ctv3"},{"code":"3047831000006110","system":"ctv3"},{"code":"4781141000006114","system":"ctv3"},{"code":"H223000","system":"ctv3"},{"code":"H223.00","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["streptococcal-pneumonia-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["streptococcal-pneumonia-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["streptococcal-pneumonia-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
