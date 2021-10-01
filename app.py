from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():


    # idx_receive = request.form['idx_give']
    title = request.form['title_give']
    content = request.form['content_give']

    today = datetime.now()
    time = today.strftime('%Y-%m-%d-%H-%M-%S')
    idx = +1

    print(title,content,time, idx)

    doc = {
       'idx':idx,
       'title':title,
       'content':content,
        'date': time
    }

    db.bookreview.insert_one(doc)
    #
    return jsonify({'msg': '저장 완료!'})




@app.route('/post', methods=['GET'])
def get_post():
    stock = list(db.dbStock.find({}, {'_id': False}))
    return jsonify({'all_stock': stock})



@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)