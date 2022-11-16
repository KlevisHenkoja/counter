from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    return redirect('/counter/add')

@app.route('/counter/add')
def counter():
    if 'counter' not in session:
        session['counter']= 0
        return render_template('index.html', counter = session['counter'])
    session['counter'] += 1
    return render_template('index.html', counter = session['counter'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')




if __name__=="__main__":    
    app.run(debug=True)       