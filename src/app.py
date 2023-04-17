from flask import Flask, request,make_response
from werkzeug.utils import secure_filename
from flask_cors import CORS
from helpers import *
from constants import *
import os,time




app=Flask(__name__,static_folder="../data")

# app.config.from_object(os.getenv('APP_SETTINGS'))

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/imageRestoration',methods = ['POST','GET'])
def restore():
    try:
        data=str(request.get_json()['images_path'])
        print(data)
        images_path= data
        print('images_path ',images_path)
        do_system(f'python3 ./inference_realesrgan.py \
              -i {images_path} \
              --output {images_path} \
              --face_enhance \
              -g 0 \
              -dn 1 \
              -s 1')
        return make_response("Done"),200
    except Exception as e:
        print(e)
        return make_response(e)


if __name__=="__main__":
    app.run(host='0.0.0.0',port=REAL_ESRGAN_PORT,debug=True)