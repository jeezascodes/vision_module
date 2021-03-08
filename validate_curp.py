import re


def validate_curp(curp):
    pattern = r'^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'
    validated = re.match(pattern, curp)
    if not validated:
        return False

    def digit_verificator(curp17):
        dictionary = '0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        lng_suma = 0
        lng_digit = 0
        for i in range(17):
            lng_suma += dictionary.index(curp17[i]) * (18 - i)
        lng_digit = 10 - (lng_suma % 10)
        if lng_suma == 10:
            return 0
        return lng_digit
    
    if int(validated[2]) != digit_verificator(validated[1]):
        return False
    return True