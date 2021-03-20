
# import main Flask class and request object
from Model import Model
from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
import random

app = Flask(__name__, template_folder='Template')  # create the Flask app
Model = Model()


@app.route('/', methods=["GET", "POST"])
def index():
    get_subjects = Model.get_subjects()
    get_students = Model.get_students()
    get_votes = Model.get_votes()
    get_sum_votes = Model.get_sum_votes()
    if request.method == "POST":
        vote_value = request.form.get("vote-radio")
        get_vote = Model.get_vote(vote_value)
        if get_vote:
            Model.update_vote(vote_value)
        else:
            Model.add_new_vote(vote_value)
        return redirect('/')
    else:
        return render_template('index.html', subjects=get_subjects, students=get_students, votes=get_votes)


@app.route('/result')
def result():
    get_scores_with_join = Model.get_scores_with_join()
    return render_template('result.html', scores=get_scores_with_join)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=7000)
