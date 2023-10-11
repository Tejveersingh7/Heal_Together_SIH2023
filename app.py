from flask import Flask, render_template ,request,redirect,send_from_directory,url_for
from flask import Flask, render_template, request
import pickle
import numpy as np



app=Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict' ,methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    predictions = model.predict(final)[0]
    print(predictions)
    # return render_template('result.html')

    if(predictions==0):
       return render_template('result.html',result=0)
    
    elif(predictions==1):
        return render_template('result.html',result=1)
    
    elif(predictions==2):
        return render_template('result.html',result=2)

    elif(predictions==3):
        return render_template('result.html',result=3)
    
    elif(predictions==4):
        return render_template('result.html',result=4)
    
    elif(predictions==5):
       return render_template('result.html',result=5)
    
    elif(predictions==6):
        return render_template('result.html',result=6)
    
    elif(predictions==7):
        return render_template('result.html',result=7)

    elif(predictions==8):
        return render_template('result.html',result=8)

if __name__=="__main__":
    app.run(debug=True,port=8000)