# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0206010I0AAAWAW","system":"bnf"},{"code":"0206010K0AABBBB","system":"bnf"},{"code":"0206030N0AAAFAF","system":"bnf"},{"code":"0206010K0AAANAN","system":"bnf"},{"code":"0206010K0AAASAS","system":"bnf"},{"code":"0206030Y0BBAAAA","system":"bnf"},{"code":"0206010K0AAAMAM","system":"bnf"},{"code":"0206010I0AAARAR","system":"bnf"},{"code":"0206010K0AAALAL","system":"bnf"},{"code":"0206030Y0BBABAB","system":"bnf"},{"code":"0206010I0AAASAS","system":"bnf"},{"code":"0206010K0AAAWAW","system":"bnf"},{"code":"0206030N0AAAEAE","system":"bnf"},{"code":"0206010I0AAATAT","system":"bnf"},{"code":"0206010K0AAARAR","system":"bnf"},{"code":"0206010I0AAAQAQ","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('angina-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina-medication-procoralan---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina-medication-procoralan---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina-medication-procoralan---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
