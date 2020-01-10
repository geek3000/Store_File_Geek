from flask import Flask, render_template, request, current_app
from werkzeug.utils import secure_filename
import os, sqlite3
from models import db, Save_files

upload_dir=os.path.join(current_app.root_path, "uploads")
data_dir=os.path.join(current_app.root_path, "data")

app = Flask(__name__)
a
@app.route('/', methods=["GET","POST"])
@app.route('/index/')
def index():
    if request.method == "POST":
        if 'file_txt' not in request.files:
            return redirect('/')
        txt_file=request.files['file_txt']
        if txt_file.filename == '':
            return redirect('/')
        
        if txt_file.content_type:
            return redirect('/')
        filename = werkzeug.secure_filename(txt_file.filename)
        txt_file.save(upload_dir, filename)
        db.session.add(Save_files(file_name))
        db.session.commit()
        return redirect('/')

    saved_files=Save_files.query.all()
    return render_template('index.html', saved_files=saved_files)

@app.route('/<file_name>')
def display(file_name):
    saved_file=Save_files.query.filter_by(file_name=file_name)
    content=""
    if not saved_file:
        return render_template('display.html')
    
    with open(os.path.join(upload_dir, saved_file)) as f:
        content=f.read()
        
    return render_template('display.html', saved_file=saved_file,
                           content=content)
    
                
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port)
