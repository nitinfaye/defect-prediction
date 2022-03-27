from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv('clean_jm1.csv')
model = pickle.load(open('AdaBoostModel.pkl','rb'))

@app.route('/')
def index():
    uniq_Ops = df['uniq_Op'].unique()
    uniq_Opnds = df['uniq_Opnd'].unique()
    total_Ops = df['total_Op'].unique()
    total_Opnds =df['total_Opnd'].unique()
    branchCounts = df['branchCount'].unique()
    return render_template("index.html", uniq_Ops=uniq_Ops, uniq_Opnds=uniq_Opnds, total_Ops=total_Ops, total_Opnds= total_Opnds)

@app.route('/predict', methods=['POST'])
def predict():

    uniq_Op = request.form.get('uniq_Op')
    uniq_Opnd = request.form.get('uniq_Opnd')
    total_Op = request.form.get('total_Op')
    total_Opnd = request.form.get('total_Opnd')
    branchCount = request.form.get('branchCount')

    prediction = model.predict(pd.DataFrame(columns=['uniq_Op','uniq_Opnd','total_Op','total_Opnd','branchCount'], data=np.array([uniq_Op,uniq_Opnd,total_Op,total_Opnd,branchCount]).reshape(1,5)))

    return str(np.round(prediction[0],3))

if __name__ == '__main__':
    app.run(debug=True)
