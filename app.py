from flask import Flask, render_template, request

app = Flask(__name__)

ASTRONAUT_DICT = {}
ASTRONAUT_DICT["Shirra"] = {"Missions":["Mercury 5", "Apollo 7"],"Moonwalker":"No"}
ASTRONAUT_DICT["Eisele"] = {"Missions":["Apollo 7"],"Moonwalker":"No"}
ASTRONAUT_DICT["Cunningham"] = {"Missions":["Apollo 7"],"Moonwalker":"No"}
ASTRONAUT_DICT["Borman"] = {"Missions":["Gemini 7","Apollo 8"],"Moonwalker":"No"}
ASTRONAUT_DICT["Lovell"] = {"Missions":["Gemini 7", "Gemini 12","Apollo 8","Apollo 13"],"Moonwalker":"No"}
ASTRONAUT_DICT["Anders"] = {"Missions":["Apollo 8"],"Moonwalker":"No"}
ASTRONAUT_DICT["McDivitt"] = {"Missions":["Gemini 4","Apollo 9"],"Moonwalker":"No"}
ASTRONAUT_DICT["Scott"] = {"Missions":["Gemini 8","Apollo 9","Apollo 15"],"Moonwalker":"Yes"}
ASTRONAUT_DICT["Schweickert"] = {"Missions":["Apollo 9"],"Moonwalker":"No"}
ASTRONAUT_DICT["Stafford"] = {"Missions":["Gemini 6","Gemini 9","Apollo 10","Apollo Soyuz"],"Moonwalker":"No"}
ASTRONAUT_DICT["Young"] = {"Missions":["Gemini 3","Gemini 8","Apollo 10","Apollo 16","STS-1","STS-9"],"Moonwalker":"Yes"}
ASTRONAUT_DICT["Cernan"] = {"Missions":["Gemini 8","Apollo 10","Apollo 17"],"Moonwalker":"Yes"}

SELECTION = {}

@app.route("/")
def index():
    return render_template("index.html",astronauts=ASTRONAUT_DICT.keys())

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html",  name=request.form.get("name", "world"))

@app.route("/register", methods=["POST"])
def register():

    astronaut = request.form.get("astronaut")
    astronaut_data_dict = ASTRONAUT_DICT.get( astronaut, "Unknown")
    if astronaut_data_dict == "Unknown":
        return render_template("failure.html", message="Invalid astronaut")

    return render_template("success.html", data=(astronaut, astronaut_data_dict))