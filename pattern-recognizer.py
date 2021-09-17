from person_recognizer import PersonRecognizer
from email_recognizer import EmailRecognizer
from aadhaar_recognizer import AadhaarRecognizer

sensitivityScore = {
    ""
}

sample = "NASA awarded Elon Musk SpaceX a $2.9 billion contract to build the lunar lander. Warren Edward Buffett is an American investor, business tycoon, philanthropist, and the chairman and CEO of Berkshire Hathaway. Input: str = 367598346012 Output: true Explanation:  The given string satisfies all the above mentioned conditions. Therefore, it is a valid Aadhar number. Input: str = 3675983460128  Output: false  Explanation:  The given string contains 13 digits. Therefore, it is not a valid Aadhar number. This is my email address person_name@email.com and this is my friend's email: friend_of_person@friend.com"

recognizedEntities = []

recognizedEntities.append(PersonRecognizer(sample).getEntity())
recognizedEntities.append(EmailRecognizer(sample).getEntity())
recognizedEntities.append(AadhaarRecognizer(sample).getEntity())

# print(myList)

for ents in recognizedEntities:
    for ent in ents:
        # print(ent.returnDict())
        var = ent.returnDict()
        # print(var["text"], var["span"])
        sample = sample.replace(var["text"], "{" + var["label"] + " [" + str(var["sensitivityScore"]) + "]}")
        

print(sample)