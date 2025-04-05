# from flask import Flask, request, jsonify, session
# from flask_session import Session  # Install using: pip install flask-session

# app = Flask(__name__)

# # Configure session storage
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"  # Stores session data on the server
# Session(app)

# @app.route('/wishlist/add', methods=['POST'])
# def add_to_wishlist():
#     if 'wishlist' not in session:
#         session['wishlist'] = []

#     data = request.get_json()
#     product = {
#         'title': data.get('title'),
#         'thumbnail': data.get('thumbnail'),
#         'source': data.get('source'),
#         'price': data.get('price'),
#         'currency': data.get('currency'),
#         'link': data.get('link')
#     }

#     if product not in session['wishlist']:
#         session['wishlist'].append(product)
#         session.modified = True
#         return jsonify({'message': f"{product['title']} added to wishlist", 'wishlist': session['wishlist']}), 200
#     else:
#         return jsonify({'message': f"{product['title']} is already in wishlist"}), 400

# @app.route('/wishlist/remove', methods=['POST'])
# def remove_from_wishlist():
#     if 'wishlist' in session:
#         data = request.get_json()
#         title = data.get('title')
#         session['wishlist'] = [p for p in session['wishlist'] if p['title'] != title]
#         session.modified = True
#         return jsonify({'message': f"{title} removed from wishlist", 'wishlist': session['wishlist']}), 200

#     return jsonify({'message': 'Wishlist is empty'}), 400

# @app.route('/wishlist', methods=['GET'])
# def get_wishlist():
#     return jsonify({'wishlist': session.get('wishlist', [])}), 200

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5500)





from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/wishlist')
def wishlist():
    if 'user_id' not in session:
        return redirect(url_for('admin_login'))

    user_id = session['user_id']
    conn = get_db_connection()
    wishlist_items = conn.execute('SELECT * FROM wishlist WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()

    return render_template('wishlist.html', wishlist_items=wishlist_items)
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5500)