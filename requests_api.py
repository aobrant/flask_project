from flask import Flask, request, jsonify
from flask.views import MethodView
from db import Element, Session
from errors import HttpError
from flask_bcrypt import Bcrypt

app = Flask('server')
bcrypt = Bcrypt(app)

@app.errorhandler(HttpError)
def error_handler(error: HttpError):

    http_response = jsonify({'status': 'error', 'description': error.message})
    http_response.status_code = error.status_code
    return http_response


def get_element(id: int, session: Session):

    element = session.query(Element).get(id)
    if element is None:
        raise HttpError(404, 'user not found')
    return element






class AdvertView(MethodView):

    def get(self, id: int):

        with Session() as session:
            element = get_element(id, session)
            return jsonify(
                {
                  'id': element.id,
                  'title': element.title,
                  'description': element.description,
                  'owner': element.owner,
                  'created_at': element.created_at.isoformat()
                }
            )




    def post(self):
        json_data = request.json
        json_data['password'] = bcrypt.generate_password_hash(json_data['password'].encode()).decode()

        with Session() as session:
            new_element = Element(**json_data)
            session.add(new_element)
            session.commit()
            return jsonify(
                {
                    'id':new_element.id,
                    'created_at':int(new_element.created_at.timestamp()),
                    'title':new_element.title,
                    'description':new_element.description
                }
            )


    def delete(self, id: int):
        with Session() as session:
            element = get_element(id, session)
            session.delete(element)
            session.commit()
            return jsonify({'status': 'success'})



app.add_url_rule('/advert/<int:id>', view_func=AdvertView.as_view('advert_with_id'), methods=['GET','DELETE'])
app.add_url_rule('/advert', view_func=AdvertView.as_view('advert_create'), methods=['POST'])


app.run(port=5001)

