from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # creates the landing page
def main():
    return render_template('main.html', static_url_path='/static')

@app.route("/decimal-binary", endpoint='decbi') # endpoint is necessary
def decimal_binary():
    return render_template('decimal-binary.html', static_url_path='/static')

@app.route("/IEEE", endpoint='IEEE')
def decimal_binary():
    return render_template('IEEE.html', static_url_path='/static')

@app.route("/GFC", endpoint='GFC')
def GFC():
    return render_template('GFC.html', static_url_path='/static')
    
if __name__ == '__main__':
    app.run()