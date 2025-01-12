from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meeting_the_brief')
def meeting_the_brief():
    return render_template('meeting_the_brief.html')

@app.route('/investigation')
def investigation():
    return render_template('investigation.html')

@app.route('/plan_and_design')
def plan_and_design():
    return render_template('plan_and_design.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/evaluation')
def evaluation():
    return render_template('evaluation.html')

@app.route('/references')
def references():
    return render_template('references.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)