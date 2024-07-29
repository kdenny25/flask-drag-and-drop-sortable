from flask import Flask, request, render_template, jsonify, url_for, redirect, flash, session
import json

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/receiveExpenses', methods=['POST'])
def receiveExpenses():
    expenses = request.form.getlist('expenses[]')

    print(expenses)
    #print(request.form.keys())
    #print(request)
    return json.dumps({'status': 'Success'})

if __name__ == '__main__':
    app.run()
