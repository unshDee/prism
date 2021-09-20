from flask import Flask
from flask import request
from person_recognizer import PersonRecognizer
from email_recognizer import EmailRecognizer
from aadhaar_recognizer import AadhaarRecognizer

app = Flask(__name__)

def pattern_recognizer(sample):
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
    return sample

@app.route("/")
def index():
    sample = request.args.get("sample", "")
    if sample:
        sample1 = pattern_recognizer(sample)
    else:
        sample1 = ""
    return (
        """<form action="" method="get">
                Sample : <textarea name="sample" rows="10" cols="50"></textarea>
                <input type="submit" value="Convert">
            </form>"""
        + "Sample: "
        + sample1
    )


if __name__ == "__main__":
    app.run(debug=True)