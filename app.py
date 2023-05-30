from flask import Flask, render_template, redirect, url_for, request, session
import uuid, os, schedule


app = Flask(__name__)

app.secret_key = "SecretKey"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/design")
def design():
    return render_template('design.html')

@app.route("/form/<string:design>", methods=["GET", "POST"])
def form(design):
    session["design_sess"] = design
    return render_template('form.html')

@app.route("/upload", methods = ["GET", "POST"])
def upload():
    design_upload = session.get("design_sess")
    if design_upload == "design1":
        design_name = "Design1.html"
    if design_upload == "design2":
        design_name = "Design2.html"
    if design_upload == "design3":
        design_name = "Design3.html"
    if design_upload == "design4":
        design_name = "Design4.html"
    
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        schoolname = request.form.get("schoolname")
        collegename = request.form.get("collegename")
        phone = request.form.get("phone")
        email = request.form.get("email")
        about = request.form.get("about")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        skill5 = request.form.get("skill5")
        instagram = request.form.get("instagram")
        linkedin = request.form.get("linkedin")
        github = request.form.get("github")

        key = uuid.uuid1()
        # Image Uploading Method
        img  = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}", f"static/images/{img_new_name}")
        

        
    return render_template(design_name, dname = firstname, dlname = lastname, dsch = schoolname, linkedin = linkedin, instagram = instagram, github = github, dcol = collegename, dph = phone, demail = email, ds1 = skill1, ds2 = skill2, ds3 = skill3, ds4 = skill4, ds5 = skill5, dabout = about, img = img_new_name)
    
def delete():
    files = os.listdir("static/images")
    for f in files:
        os.remove(f"static/images/{f}")
if __name__ == "__main__":   
    schedule.every().day.at("23:59").do(delete)
    app.run(debug=True)