from flask import Flask, request, render_template
import recognizers

app = Flask(__name__)

# countEntities = {}

def pattern_recognizer(sample, country):
    # creating countEntities inside method so that for every new sample text
    # it creates a new dictionary and doesn't add on to some previous dictionary
    # countEntities = {}
    entitylist = []
    recognizedEntities = recognizers.recognizers(sample, country)
    for ents in recognizedEntities:
        for ent in ents:
            var = ent.to_dict()
            if var not in entitylist:
                entitylist.append(var)
            # if var["label"] in countEntities: # exists
            #     countEntities[var["label"]] += 1
            # else:
            #     countEntities[var["label"]] = 1
            sample = sample.replace(var["text"], "{" + var["label"] + " [" + str(var["sensitivityScore"]) + "]}", 1)
            
    return {"censoredText": sample, "entityList": entitylist}

@app.route("/", methods=["POST", "GET"])
def index(sample = None, country = None):
    if request.method == "POST":
        sample = request.form["input"]
        country = "GENERIC"
        if "country" in request.files:
            country = request.form["country"]
        if sample:
            data = pattern_recognizer(sample, country)
            censoredText = data["censoredText"]
            entityList = data["entityList"]
        else:
            censoredText = ""
            entityList = {}
        return render_template("index.html", output=censoredText, entities=entityList)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)