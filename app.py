#required imports
from flask import Flask, render_template, request, send_file
from json_excel_converter import Converter 
from json_excel_converter.xlsx import Writer
import json



app = Flask(__name__)

#homeage of localhost:5000
@app.route('/')
def upload_file():
   return render_template('upload.html')

#method to upload and conver a json file to excel file
@app.route('/download', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)
        json_data = open(f.filename)
        data = json.load(json_data)
        conv = Converter()
        out=f.filename[0:f.filename.index('.')]
        out=out+'.xlsx'
        conv.convert(data, Writer(file=out))
        #call download page
        return  render_template("download.html", value = out)  

#code to download the file
@app.route('/return-files/<filename>')
def return_files(filename):
    file_path = filename
    return send_file(file_path, as_attachment=True, attachment_filename=filename)

if __name__ == '__main__':
    app.run()
