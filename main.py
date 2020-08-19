from flask import Flask, jsonify, request
from faceR import faceRecog


app = Flask(__name__) #define app using flask
app.config['DEBUG'] = False


@app.route('/auth',methods=['POST'])
def auth_Conn():
    user =request.form['user'] 

    imagefile = request.files.get('imagefile', '')
    imagefile.save('C:/Users/ALEJANDROROMEROALDRE/Documents/maestria3ro/PROYECTOFINAL/software/python/imgs/temp_'+user+'.jpg')

    faceR = faceRecog()
    result = faceR.auth(user)
    if result==False:
        return jsonify({'status':'ERROR','data':{},'msg':result})
    else:
       return jsonify({'status':'OK','data':result,'msg':'OK'})

if __name__=='__main__':
    #app.run(debug=False, port=8080)
    app.run(host = "0.0.0.0",port=8080)