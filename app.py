from flask import Flask, request, render_template
from model import classifier
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def classifierA():
    if request.method == "POST":
        Clump = int(request.form.get("Clump"))
        UnifSize = int(request.form.get("UnifSize"))
        UnifShape = int(request.form.get("UnifShape"))
        MargAdh = int(request.form.get("MargAdh"))
        SingEpiSize = int(request.form.get("SingEpiSize"))
        BareNuc = int(request.form.get("BareNuc"))
        BlandChrom = int(request.form.get("BlandChrom"))
        NormNucl = int(request.form.get("NormNucl"))
        Mit = int(request.form.get("Mit"))
        out = classifier(Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit)
        return render_template("login.html", out="The Class Of the Tumor Is:"+ out)

    return render_template("login.html",out="")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port = 8080)

if __name__ == "__main__":
    app.run(debug=True)