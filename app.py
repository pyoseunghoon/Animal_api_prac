from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

# @app.route('/')
# def home():
#     return render_template('index.html')
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/save')
def save():
    return render_template('save.html')

@app.route('/count')
def count():
    return render_template('count.html')

## API 역할을 하는 부분
@app.route('/animal', methods=['POST'])
def animal_save():
    animal = request.form['animal']
    count = request.form['count']
    print(animal, count)
    doc = {
        'animal': animal,
        'count': count
    }
    db.animals.insert_one(doc)
    return jsonify({'result':'success', 'msg':'저장되었습니다.'})

@app.route('/animal_count', methods=['GET'])
def animal_count_get():
    animal = request.args.get('animal')
    print(animal)
    doc = db.animals.find_one({'animal':animal},{'_id':0})
    print(doc)
    return jsonify({'result':'success', 'count': doc['count']})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)