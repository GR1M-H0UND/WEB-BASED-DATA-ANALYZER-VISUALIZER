from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg'
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get uploaded file
    file = request.files['file']
    
    # Load data from the uploaded file
    data = pd.read_csv(file)
    
    # Analyze the data
    basic_statistics = data.describe()

    # Generate scatter plot
    column_x = request.form['column_x']
    column_y = request.form['column_y']
    plt.scatter(data[column_x], data[column_y])
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(f"{column_x} vs {column_y}")
    
    # Save plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # Render the result page with analysis results
    return render_template('result.html', basic_statistics=basic_statistics.to_html(), plot_url=plot_url)

@app.route('/about')
def about():
    developers = [
        {'name': 'Soumyajit Sardar', 'email': 'mailto:soumyajitsardar.2000@gmail.com'},
        {'name': 'Niladri Sekhar Naskar', 'email': 'mailto:niladrisekhar09@gmail.com'}
    ]
    return render_template('about.html', developers=developers)

if __name__ == '__main__':
    app.run(debug=True)
