from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def display_boxes():
    return render_template('index.html', num_boxes = 3, color = "blue")

@app.route('/play/<x>')
def display_x_boxes(x):
    return render_template('index.html', num_boxes = int(x), color = "blue")

@app.route('/play/<x>/<color>')
def display_x_boxes_color(x, color):
    return render_template('index.html', num_boxes = int(x), color = color)

if __name__ == "__main__":
    app.run(debug=True)