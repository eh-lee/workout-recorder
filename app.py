from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.s2vjf18.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():

    user_data = list(db.user.find({},{'_id':False}))

    return jsonify({'user_data' : user_data})


@app.route('/test', methods=['POST'])
def test_post():
    label_receive = request.form['label_give']
    box_receive = request.form['box_give']
    comment_receive = request.form['comment_give']


    doc = {
        'label' : label_receive,
        'box' : box_receive,
        'comment' : comment_receive,
    }

    db.user.insert_one(doc)

    return jsonify({'msg': '기록습니다.'})

@app.route('/boob', methods=['POST'])
def boob_post():

    db.user.delete_one({'label':'운동명'})
    return jsonify({'msg': '삭제했습니다..'})

@app.route('/add_comment', methods=['POST'])
def add_comment_post():
    comment_receive = request.form['comment_give']

    db.user.update_one({'comment':''},{'$set':{'comment':comment_receive}})
    return jsonify({'msg': '변경했습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

