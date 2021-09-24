from flask import Flask
from flask import request
import recognizers

app = Flask(__name__)

countEntities = {}

def pattern_recognizer(sample, country):
    recognizedEntities = recognizers.recognizers(sample, country)
    for ents in recognizedEntities:
        for ent in ents:
            var = ent.to_dict()
            if var["label"] in countEntities: # exists
                countEntities[var["label"]] += 1
            else:
                countEntities.add(var["label", 1])
            
            sample = sample.replace(var["text"], "<code><b>{" + var["label"] + " [" + str(var["sensitivityScore"]) + "]}</b></code>", 1)
    return sample +"\n" + f"{countEntities}"

@app.route("/")
def index():
    sample = request.args.get("sample", "")
    country = request.args.get("country", "")
    if sample:
        censoredText = pattern_recognizer(sample, country)
    else:
        censoredText = ""
    return (
        """
        <h1>Input</h1>
        <form action="" method="get">
            <label for="sample">Sample: </label> <br><br>
            <textarea id="sample" name="sample" rows="10" cols="50" placeholder="Enter sample text here"></textarea> <br><br><br>
            <label for="country">Country: </label>
            <input type="text" id="country" name="country" placeholder="Country Name"> <br><br><br><br>
            <input type="submit" value="Convert">
        </form>
        <br>
        <h1>Output</h1>
        Sample:
        <br>
        """
        + censoredText
    )

if __name__ == "__main__":
    app.run(debug=True)