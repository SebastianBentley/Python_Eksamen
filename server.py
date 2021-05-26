from flask import Flask, request, Response, render_template
import subprocess
import laptops as lp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

    

@app.route("/laptop", methods=['POST'])
def calc():
    #subprocess.call('calc.exe')
    #return index()
    
    laptop = request.form['laptop']
    result = lp.fetch_data(laptop)
    return "<h1>hejhej</h1>"+str(result)

@app.route("/laptoptest", methods=['POST'])
def test():
    while True:
        subprocess.call('calc.exelaptop')

if __name__ == "__main__":
    app.run(debug='True')