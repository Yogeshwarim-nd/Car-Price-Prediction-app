from flask import Flask

app=Flask(__name__)

@app.route("/yogo",methods=["GET"])
def yogo():
    return "welcome"

if __name__=="__main__":
    app.run(debug=True)