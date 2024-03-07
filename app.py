# from dbhelper import DBhelper
from flask import Flask, render_template, request,redirect, url_for,jsonify
import pandas as pd
import random
data=[]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def handle_registration():
    name = request.json['name']
    age=request.json['age']
    gender = request.json['gender']
    style = request.json['style']
    hairColor=request.json['hairColor']
    skinColor = request.json['skinColor']
    size = request.json['size']
    print(name, age, gender, style, hairColor, skinColor, size)
    df = pd.read_excel('coloranalysis.xlsx')
    filtered_df = df[(df['Gender'] == gender) &
                     (df['Age'] == age) &
                     (df['Skin color'] == skinColor) &
                     (df['Size'] == size) &
                     (df['Style'] == style) &
                     (df['Haircolor'] == hairColor)]

    filtered_data = filtered_df[['reference', 'links', 'price', 'image']].values.tolist()
    global data
    for item in filtered_data:
        item[3]=str(item[3])
        data.append([item[0],item[1],item[2],item[3]])
    data = random.sample(filtered_data, 3)
    print(data)

    return jsonify({'success': True})
@app.route('/men')
def men():
    gender="Male"
    df = pd.read_excel('coloranalysis.xlsx')
    filtered_df = df[(df['Gender'] == gender)]
    print(filtered_df)
    filtered_data = filtered_df[['reference', 'links', 'price', 'image']].values.tolist()
    data1=[]
    for item in filtered_data:
        item[3] = str(item[3])
        data1.append([item[0], item[1], item[2], item[3]])
    print(data1)
    return render_template('men.html',data=data1)
@app.route('/kids')
def kids():
    age="14 - 9"
    print(age)
    df = pd.read_excel('coloranalysis.xlsx')
    print(df)
    filtered_df = df[(df['Age'] == age)]
    print(filtered_df)
    filtered_data = filtered_df[['reference', 'links', 'price', 'image']].values.tolist()
    data1=[]
    for item in filtered_data:
        item[3] = str(item[3])
        data1.append([item[0], item[1], item[2], item[3]])
    print(data1)
    return render_template('men.html',data=data1)
@app.route('/women')
def women():
    gender="Female"
    df = pd.read_excel('coloranalysis.xlsx')
    filtered_df = df[(df['Gender'] == gender)]
    print(filtered_df)
    filtered_data = filtered_df[['reference', 'links', 'price', 'image']].values.tolist()
    data1=[]
    for item in filtered_data:
        item[3] = str(item[3])
        data1.append([item[0], item[1], item[2], item[3]])
    print(data1)
    return render_template('men.html',data=data1)
@app.route('/recommendation')
def recommendation():
    print(data)
    return render_template('card.html',data=data)

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
