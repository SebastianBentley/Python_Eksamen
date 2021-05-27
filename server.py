from flask import Flask, request, Response, render_template, url_for
import subprocess
import laptops as lp
import close_five as c5

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

    

@app.route("/laptop", methods=['POST'])
def calc():
    #subprocess.call('calc.exe')
    #return index()
    
    laptop = request.form['laptop']
    result = lp.fetch_data(laptop)
    print(result)
    name = result[1][0]
    company = result[0]
    imgsource = lp.find_img(name)
    price = float(result[1][1])
    close5 = c5.get_close_five(name, price)
    msg = ""
    final_string = ""

    names = list(close5['name'])
    prices = list(close5['price'])
    if (price != 0.0):
        msg = "Nær denne prisklasse"
        for idx, val in enumerate(names):
            final_string += "<li>" + str(names[idx]) + ". Price: " + str(prices[idx]) + "dkk.</li>"

    return "<body style=\"text-align: center; background-color:cadetblue;\">" + "<h1>Found pc: {}<br> Price: {} dkk.<br> Company: {}</h1><br><img src={} style=\"height: 200px; width: 200px;\" /><br><h2><u>{}</u></h2><h2><ol>{}</ol></h2><button onClick=\"window.history.back();\">Gå hjem</button></body>".format(name, price, company, imgsource, msg, final_string)
    

if __name__ == "__main__":
    app.run(debug='True')