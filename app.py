from flask import Flask, request, jsonify, redirect
from pathlib import Path
app=Flask(__name__)
DATA=Path(__file__).resolve().parent/'feedback.txt'
@app.get('/')
def index(): return 'StudentPortfolio: /profile?name=Student, POST /feedback, /feedback, /go?next=/profile'
@app.get('/profile')
def profile():
    name=request.args.get('name','Student')
    return '<h1>Portfolio of '+name+'</h1><p>Software security projects</p>'
@app.post('/feedback')
def add_feedback():
    text=request.form.get('message','')
    with DATA.open('a',encoding='utf-8') as f: f.write(text.replace('\n',' ')+'\n')
    return jsonify(saved=True)
@app.get('/feedback')
def feedback():
    return '<h2>Feedback</h2>'+('<hr>'.join(DATA.read_text().splitlines()) if DATA.exists() else 'No feedback')
@app.get('/go')
def go(): return redirect(request.args.get('next','/'))
if __name__=='__main__': app.run(host='127.0.0.1',port=5105,debug=False)
