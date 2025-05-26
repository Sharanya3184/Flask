from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/name/<name>', methods=['GET'])
def render_name(name:str):

    if name :
        return render_template('name.html', value=name)
    return render_template('error.html', value=name)


@app.route('/name', methods=['GET'])
def get_user_details():
    return render_template('form.html')

@app.route('/name', methods=['POST'])
def post_user_details():
    username=request.values.get('name')
    if username:
        return render_template('name.html', value=username)


def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)