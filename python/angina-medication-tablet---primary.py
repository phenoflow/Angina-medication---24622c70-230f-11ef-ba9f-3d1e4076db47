# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0206010K0CNAAAE","system":"bnf"},{"code":"0206010K0CKAAAE","system":"bnf"},{"code":"0206010K0BDACAB","system":"bnf"},{"code":"0206010K0CTAAAE","system":"bnf"},{"code":"0206010K0BNACAE","system":"bnf"},{"code":"0206010K0BDADAD","system":"bnf"},{"code":"0206010K0BXACAE","system":"bnf"},{"code":"0206010K0CRAAAE","system":"bnf"},{"code":"0206010K0CJAAAE","system":"bnf"},{"code":"0206010K0CFAAAE","system":"bnf"},{"code":"0206010K0CDAAAE","system":"bnf"},{"code":"0206010K0CHAAAE","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('angina-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina-medication-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina-medication-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina-medication-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
