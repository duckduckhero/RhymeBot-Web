from flask import Flask, render_template, redirect, request, url_for
import RhymeBot as rb

app = Flask(__name__)

@app.route('/')
@app.route('/<int:val>')
def main(val=None):
    return render_template('main.html')

@app.route('/rhymecheck', methods=['POST'])
def rhymecheck(val=None):
    if request.method == 'POST':
        w1 = request.form['word1']
        w2 = request.form['word2']
        res = rb.rhymecheck(w1, w2)
    else :
        w1 = None
        w2 = None
    if res>=0.4 : return render_template('main.html', word1=w1+" , "+w2+" 을(를) 입력하셨습니다.", val="유사도는 "+str(res)+" 입니다", bool="두 단어는 Rhyme 이 맞습니다.")
    else : return render_template('main.html', word1=w1+" , "+w2+" 를 입력하셨습니다.", val="유사도는 "+str(res)+" 입니다", bool="두 단어는 Rhyme 이 맞지 않습니다.")
    #word1, word2 는 각각 사용자가 입력한 단어, val 은 알고리즘 거친 후의 결과값


if __name__ == '__main__':
    app.run()
