from flask import Flask, render_template, Response
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

# Home / Dashboard
@app.route("/")
def dashboard():
    extracted = {
        "Name": "AquaFresh",
        "Brand": "AquaPure Pvt Ltd",
        "Expiry Date": "12/2026",
        "Batch No": "B12345"
    }
    gov_guidelines = ["Name", "Brand", "Expiry Date", "Batch No", "FSSAI No"]

    return render_template("dashboard.html", extracted=extracted, guidelines=gov_guidelines)

# Guidelines page
@app.route("/guidelines")
def guidelines_page():
    extracted = {
        "Name": "AquaFresh",
        "Brand": "AquaPure Pvt Ltd",
        "Expiry Date": "12/2026",
        "Batch No": "B12345"
    }
    gov_guidelines = ["Name", "Brand", "Expiry Date", "Batch No", "FSSAI No"]

    # Prepare status for display
    status_list = []
    for field in gov_guidelines:
        status = "Present ✅" if field in extracted else "Missing ⚠️"
        status_list.append({"field": field, "status": status})

    # Use lowercase template name for consistency
    return render_template("guidelines.html", status_list=status_list)

# Download PDF
@app.route("/download_guidelines")
def download_guidelines():
    extracted = {
        "Name": "AquaFresh",
        "Brand": "AquaPure Pvt Ltd",
        "Expiry Date": "12/2026",
        "Batch No": "B12345"
    }
    gov_guidelines = ["Name", "Brand", "Expiry Date", "Batch No", "FSSAI No"]

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Guidelines Report")

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Guidelines Report")

    pdf.setFont("Helvetica", 12)
    y = 750
    pdf.drawString(50, y, "Field")
    pdf.drawString(300, y, "Status")
    y -= 20

    for field in gov_guidelines:
        status = "Present ✅" if field in extracted else "Missing ⚠️"
        pdf.drawString(50, y, field)
        pdf.drawString(300, y, status)
        y -= 20

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return Response(
        buffer,
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename=Guidelines_Report.pdf"}
    )

if __name__ == "__main__":
    app.run(debug=True)
