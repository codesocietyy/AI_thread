from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('monitor.html', PAR1=0, PAR2=0, PAR3=0,PAR4=0)

@app.route("/run")
def runnable():
    #call the function
    return render_template('monitor.html', PAR1=1, PAR2=1, PAR3=1, PAR4=1)

if __name__ == "__main__":
    app.run()
