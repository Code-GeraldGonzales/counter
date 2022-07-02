from flask import Flask, render_template, redirect, session

app = Flask(__name__)

app.secret_key = 'clyde'

@app.route('/clear')
def clear():
    return redirect('/counter')


@app.route('/counter')
def counts():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] +=1
    return render_template ("index.html")


@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/clear')


if __name__ == "__main__":
    app.run(debug=True)