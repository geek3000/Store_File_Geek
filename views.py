from flask import Flask, render_template, request, current_app, redirect
from werkzeug.utils import secure_filename
import os, sqlite3
from models import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config["UPLOAD_FOLDER"]="./static/uploads" 


db = SQLAlchemy(app)
db.init_app(app)

@app.route('/', methods=["GET","POST"])
def index():
    saved_files=Save_files.query.all()
    id1=len(saved_files)+1
    if request.method == "POST":
        print(request.files)
        if not 'file_txt' in request.files:
            return redirect('/')
        print('pppp')
        txt_file=request.files['file_txt']
        if txt_file.filename == '':
            return redirect('/')
        print(txt_file.content_type)
        if not txt_file.content_type == 'text/plain':
            return redirect('/')
        
        filename = secure_filename(txt_file.filename)
        txt_file.save(app.config["UPLOAD_FOLDER"]+'/paetii'+str(id1)+'.txt')
        db.session.add(Save_files(filename, id1))
        db.session.commit()
        return redirect('/')

    saved_files=Save_files.query.all()
    return render_template('index.html', saved_files=saved_files)

@app.route('/display/<id1>')
def display(id1):
    saved_file=Save_files.query.filter_by(id1=id1).first()
    content=""
    if not saved_file:
        return render_template('display.html')
    with open(app.config["UPLOAD_FOLDER"]+'/paetii'+saved_file.id1+'.txt') as f:
        content=f.read()
        
    return render_template('display.html', saved_file=saved_file, content=content)
    
                
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
