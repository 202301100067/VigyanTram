from flask import Flask, render_template, Response, url_for, redirect
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

# -----------------------------
# Home / Dashboard
# -----------------------------
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# -----------------------------
# Reports Page
# -----------------------------
@app.route("/report")
def report():
    reports = [
        {"Name": "AquaFresh", "Brand": "AquaPure Pvt Ltd", "Expiry": "12/2026"},
        {"Name": "MB Whey", "Brand": "MuscleBoost Pvt Ltd", "Expiry": "12/2026"}
    ]
    return render_template("report.html", reports=reports)

# -----------------------------
# Export Report PDF
# -----------------------------
@app.route("/download_report")
def download_report():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Product Report")

    product = {
        "Name": "MB Whey",
        "Brand": "MuscleBoost",
        "Expiry": "12/12/2026",
        "MRP": "₹1,499",
        "Manufacturer": "MuscleBoost Pvt. Ltd.",
        "Customer Care": "1800-765-432",
        "Compliance": "92%"
    }

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Product Report")
    pdf.setFont("Helvetica", 12)
    y = 750
    for key, value in product.items():
        pdf.drawString(50, y, f"{key}: {value}")
        y -= 20

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return Response(
        buffer,
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename=Product_Report.pdf"}
    )

# -----------------------------
# Guidelines Page
# -----------------------------
@app.route("/guidelines")
def guidelines_page():
    extracted = {
        "Name": "AquaFresh",
        "Brand": "AquaPure Pvt Ltd",
        "Expiry Date": "12/2026",
        "Batch No": "B12345"
    }
    gov_guidelines = ["Name", "Brand", "Expiry Date", "Batch No", "FSSAI No"]

    status_list = []
    for field in gov_guidelines:
        status = "Present ✅" if field in extracted else "Missing ⚠️"
        status_list.append({"field": field, "status": status})

    return render_template("guidelines.html", status_list=status_list)

# -----------------------------
# Download Guidelines PDF
# -----------------------------
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

# -----------------------------
# Optional: Logout Route
# -----------------------------
@app.route("/logout")
def logout():
    # If using login sessions, implement session clearing here
    return redirect(url_for('dashboard'))

# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
