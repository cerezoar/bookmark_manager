from flask import Flask, render_template, request, redirect, url_for
import json
import os
import sys

app = Flask(__name__)
# Get the directory of the executable file
BASE_DIR = os.path.dirname(sys.executable)
BOOKMARKS_PATH = os.path.join(BASE_DIR, 'bookmarks.json')

# Load bookmarks from JSON file
def load_bookmarks():
    try:
        with open(BOOKMARKS_PATH, 'r', encoding='utf-8') as f:
            bookmarks = json.load(f)
    except FileNotFoundError:
        bookmarks = []
    return bookmarks

# Save bookmarks to JSON file
def save_bookmarks(bookmarks):
    with open(BOOKMARKS_PATH, 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f, indent=4, ensure_ascii=False)

bookmarks = load_bookmarks()

@app.route('/')
def index():
    return render_template('index.html', bookmarks=bookmarks, enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    url = request.form['url']
    description = request.form['description']
    doc_id = request.form['doc_id']
    bookmarks.append({'title': title, 'url': url, 'description': description, 'doc_id': doc_id})
    save_bookmarks(bookmarks)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        description = request.form['description']
        doc_id = request.form['doc_id']
        bookmarks[index] = {'title': title, 'url': url, 'description': description, 'doc_id': doc_id}
        save_bookmarks(bookmarks)
        return redirect(url_for('index'))
    else:
        bookmark = bookmarks[index]
        return render_template('edit.html', bookmark=bookmark, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    del bookmarks[index]
    save_bookmarks(bookmarks)
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('query')
    results = []
    for bookmark in bookmarks:
        if query.lower() in bookmark['title'].lower() or \
           query.lower() in bookmark['description'].lower() or \
           query.lower() == bookmark['doc_id'].lower():
            results.append(bookmark)
    return render_template('index.html', bookmarks=results, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
