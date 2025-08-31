from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your own MongoDB URI
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todo_items

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']

    collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
