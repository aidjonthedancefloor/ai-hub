from rest.root import app

if __name__ == '__main__':
    # Run on 127.0.0.1:5000 by default
    app.run(host='127.0.0.1', port=5000, debug=True)
