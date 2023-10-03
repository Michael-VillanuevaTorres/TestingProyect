from app.user import bp as app

@app.route('/likes', methods=['GET'])
def get_likes_from_user():
    pass

@app.route('/reports', methods=['GET'])
def get_reports_from_user():
    pass  
