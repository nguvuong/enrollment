from application import app
from flask import render_template, request, json, Response

# pass data to view 
courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, 
                {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, 
                {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
                {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
                {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

# print the data to the console 
# print(courseData[0]["title"])

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # try the if login function in index file
    return render_template("index.html", index=True)

@app.route("/login")
def login():
    # try the if login function in index file
    return render_template("login.html", login=True)

@app.route("/courses/")
# use URL variable
@app.route("/courses/<term>")
def courses(term="Spring 2019"):

    # try the if login function in index file
    return render_template("courses.html", courseData = courseData, courses = True, term = term)

@app.route("/register")
def register():
    # try the if login function in index file
    return render_template("register.html", register=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    # using get so that it will not crash your site 
    #  import the request function as well 
    # using post # get 
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data= {"id": id, 
                                                                      "title": title,
                                                                      "term": term})

# set default idx = None
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData 
    else: 
        jdata = courseData[int(idx)]
        
    # dump it as json data 
    return Response(json.dumps(jdata), mimetype="application/json")