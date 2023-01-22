import io
from flask import Flask, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

dpi = 96
step = 0.1

app = Flask(__name__)

@app.route("/plot", methods=['GET'])
def plot():
    args = request.args #slownik request.args
    a = args.get('a', default=0, type=float)
    b = args.get('b', default=0, type=float)
    c = args.get('c', default=0, type=float)
    xmin = args.get('xmin', default=-1, type=float)
    xmax = args.get('xmax', default=1, type=float)
    ymin = args.get('ymin', default=-1, type=float)
    ymax = args.get('ymax', default=1, type=float)

    x = np.arange(xmin, xmax + step, step)
    y = a * x ** 2 + b * x + c

    fig = Figure(figsize=(1920 / dpi, 1080 / dpi), dpi=dpi) #obrazek 1920x1080
    axis = fig.add_subplot(1, 1, 1)
    axis.grid() #siatka na wykresie
    axis.plot(x, y)
    axis.set_xlim([xmin, xmax])
    axis.set_ylim([ymin, ymax])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)