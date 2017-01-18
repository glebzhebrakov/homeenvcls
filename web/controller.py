from flask import request
from flask import abort

from web.service import classify_image


def configure(app):
    @app.route('/classify', methods=['POST'])
    def get_classify():
        if not request.data:
            abort(400, 'Post should contains path to image for classification in the body')
        return classify_image(request.data)

    return app
