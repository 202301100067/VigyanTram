from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Example extracted product details
    extracted = {
        "Name": "AquaFresh",
        "Brand": "AquaPure Pvt Ltd",
        "Expiry Date": "12/2026",
        "Batch No": "B12345"
    }

    # Example government mandatory guidelines
    gov_guidelines = ["Name", "Brand", "Expiry Date", "Batch No", "FSSAI No"]

    return render_template("dashboard.html", extracted=extracted, guidelines=gov_guidelines)

if __name__ == "__main__":
    app.run(debug=True)
