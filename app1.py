from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zy6s87z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/eh", methods=["POST"])
def eh_post():
    sport_receive = request.form['sport_give']
    comment_receive = request.form['comment_give']

    doc = {
        'sport': sport_receive,
        'comment': comment_receive
    }
    db.soprts.insert_one(doc)

    return jsonify({'msg': '운동 기록 완료!'})

@app.route("/eh", methods=["GET"])
def eh_get():
    comment_list = list(db.soprts.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/eh/comment", methods=["POST"])
def eh_comment():
    encourage_receive = request.form['encourage_give']

    doc = {
        'encourage': encourage_receive
    }
    db.comment.insert_one(doc)

    return jsonify({'msg': '댓글 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)