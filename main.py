import json

import config
from typing import Tuple, List

import requests
from sqlalchemy import select
from db.db import session, Quiz
from flask import request, Flask

app = Flask(__name__)
BASE_URL = 'https://jservice.io/api/random?count='


@app.route('/api/v1/question', methods=['POST'])
def write_questions_to_db() -> List | Tuple:
    question_num: int = json.loads(request.data)['questions_num']

    # Check input data
    if not isinstance(question_num, int) or question_num < 1:
        return {'error': '"questions_num" should be a positive integer'}, 400

    # Get questions from the previous query to return to
    query = select(Quiz.id, Quiz.question, Quiz.answer, Quiz.created_at).where(Quiz.prev_ids == 1)
    prev_questions = [
        {'id': id, 'question': question, 'answer': answer, 'created_at': created_at}
        for id, question, answer, created_at in session.execute(query)
    ]

    # Set prev_ids to default to write again later
    session.query(Quiz).filter_by(prev_ids=1).update({'prev_ids': None})

    while question_num:
        questions = requests.get(BASE_URL + str(question_num))

        if questions.status_code == 200:
            for row in questions.json():
                is_id_unique = session.query(Quiz).filter_by(id=row['id']).first()
                if is_id_unique is None:
                    session.add(Quiz(
                        id=row['id'],
                        prev_ids=1,
                        question=row['question'],
                        answer=row['answer'],
                        created_at=row['created_at']
                    ))
                    session.commit()
                    question_num -= 1

    return prev_questions, 201


if __name__ == '__main__':
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True)
