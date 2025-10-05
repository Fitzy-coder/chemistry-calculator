from flask import Flask, render_template

app = Flask(__name__)

# ホームページ (計算ツール)
@app.route('/')
def index():
    return render_template('index.html')

# 各情報ページ
@app.route('/<page_name>')
def show_page(page_name):
    safe_pages = ['usage', 'developer', 'privacy', 'other_sites']
    if page_name in safe_pages:
        return render_template(f'{page_name}.html')
    else:
        return "Page not found", 404

# if __name__ == '__main__':
#     app.run(debug=True)

