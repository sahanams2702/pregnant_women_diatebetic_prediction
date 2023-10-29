from flask import Flask,render_template,request
import numpy as np
import joblib
app=Flask(__name__)


@app.route('/predict',methods=['GET','POST']) #type:ignore
def predict():
    
    if request.method=='POST':
        
        testdata=[ float(item) for item in request.form.values() ]
        
        print(f"Test data = {testdata}")
        
        
        
        model=joblib.load('./knndiabetic.pkl')
        
        pred=model.predict(np.array([testdata]))
        
        print(f"Result of prediction = {pred}")
        
        result=pred[0]
        
        print(f"result = {result} , its type = {type(result)}")
        if result==1:
            msg="Patient may get diabetic"
        else:
            msg="No worries not diabetic"
        
        return render_template('homepage.html',result=msg)



@app.route('/login',methods=['GET','POST']) #type:ignore
def login():
    
    if request.method=='POST':
        
        uname=request.form['uname']
        pwd=request.form['pwd']
        
        if uname=="admin" and pwd=="admin123":
            return render_template('homepage.html')
        else:
            return render_template('login.html',result="Login failed")

@app.route('/')
def index():
    return render_template('login.html')


if __name__=='__main__':
    
    app.run(debug=True)