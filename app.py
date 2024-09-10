from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def BMI():
    NAME = ''
    BMI = ''
    AGE = ''
    SUGGESTION = None
    if request.method == 'POST' and 'WEIGHT' in request.form: 
        NAME = request.form.get("NAME")
        WEIGHT = float(request.form.get('WEIGHT'))
        HEIGHT = float(request.form.get('HEIGHT'))
        AGE = int(request.form.get('AGE'))
        BMI = calc_bmi(WEIGHT, HEIGHT)
        SUGGESTION= suggest(BMI, AGE)
    return render_template("index.html", NAME=NAME, BMI=BMI, SUGGESTION=SUGGESTION)

def calc_bmi(WEIGHT, HEIGHT):
    return round((WEIGHT / ((HEIGHT / 100) ** 2)), 2)

def suggest(BMI, AGE):
    if (BMI<18 and AGE>18):
        return "Ummm...It's a bit low! Work on your body a bit!"
    elif (17 < BMI < 25 and AGE>18 ):
        return "Yayyy!!...Keep it up that's a good score."
    else:
        return "You need to improve, Keep working Hard!"

if __name__ == "__main__":
    app.run(debug=True, port=5500)
