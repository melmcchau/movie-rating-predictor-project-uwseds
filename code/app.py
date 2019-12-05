from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def do_something(start_date,end_date):
   start_date = start_date.upper()
   end_date = end_date.upper()
   combine = start_date + end_date
   return combine

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    start_date = request.form['start_date']
    word = request.args.get('start_date')
    end_date = request.form['end_date']
    combine = do_something(start_date,end_date)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == "__main__":
    app.run()
