import re
import spacy
nlp = spacy.load("en_core_web_sm")

class CreditLicenseRecog:
    def isValidLicenseNo(self,str2):
        # Regex to check valid
        # Indian driving license number
        regex = ("(AN|AP|AR|AS|BR|CH|DN|DD|DL|GA|GJ|HR|HP|JK|KA|KL|LD|MP|MH|MN|ML|MZ|NL|OR|PY|PN|RJ|SK|TN|TR|UP|WB)[0-9]" +
                    "{2}((19|20)[0-9]" +
                    "[0-9])[0-9]{7}$")

        p = re.compile(regex)

        # If the string is empty
        # return false
        doc = nlp(str2)

        for token in doc:
            # print(token.text)
            res = re.match(p, token.text)
            if res:
                print("Match found!")
                return res
            else:
                print("Match not found!")

    def creditcrno(self,text):
        regex = r"(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)"
        pattern = re.compile(regex)
        doc = nlp(text)
        for token in doc:
            res = re.match(pattern, token.text)
            if res:
                print("Match found!")
                return res

ListLisc = []
lisc1 = CreditLicenseRecog()
ListLisc.append(lisc1.isValidLicenseNo(input("Enter Your License number : ")))
ListLisc.append(lisc1.isValidLicenseNo(input("Enter Your License number : ")))

print(ListLisc)

ListCrno = []
lisc2 = CreditLicenseRecog()
ListCrno.append(lisc2.creditcrno(input("Enter Your Credit Card number : ")))
ListCrno.append(lisc2.creditcrno(input("Enter Your Credit Card number : ")))

print(ListLisc)
Lis3  = ListCrno + ListLisc
print(Lis3)
# ListCrNo = []

# lisc2 = CreditLicenseRecog()
# mydict["LicenseNumber"] = ListCrNo.append(lisc2.isValidLicenseNo(input("Enter your License number : ")))
# mydict["CreditCard"] = ListCrNo.append(lisc2.creditcrno(input("Enter your credit card number : ")))
# print(mydict)

# ListLisc = []
# lisc1 = CreditLicenseRecog()
# ListLisc.append(lisc1.isValidLicenseNo(input("Enter Your License number : ")))
# ListLisc.append(lisc1.creditcrno(input("Enter Your Credit Card number : ")))
# lisc no = HR0619850034761 MH0619850034761
# text = "Mastercard 5408678185015492, VISA 4716388496693785, AMEX

# ListCrNo = []
# mydict = {}
# lisc2 = CreditLicenseRecog()
# d = str(ListCrNo.append(lisc2.isValidLicenseNo(input("Enter your License number : "))))
# c = str(ListCrNo.append(lisc2.creditcrno(input("Enter your credit card number : "))))
# mydict["LicenseNumber"] = [d]
# mydict["CreditCard"] = [c]
# print(mydict)
