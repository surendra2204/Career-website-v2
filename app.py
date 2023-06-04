from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': '1',
  'title': 'Data Analyst',
  'location': 'Benguluru, India',
  'salary': '12LPA'
}, {
  'id': '2',
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': '15LPA'
}, {
  'id': '3',
  'title': 'Front end Engineer',
  'location': 'Remote',
  'salary': '9LPA'
}, {
  'id': '4',
  'title': 'Back end Engineer',
  'location': 'San Franciso, USA',
  'salary': '$12000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Surendra')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
