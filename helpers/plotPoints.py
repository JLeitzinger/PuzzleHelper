import matplotlib.pyplot as plt

def plotPoints(coords):
    xs = [x[0] for x in coords]
    ys = [x[1] for x in coords]
    plt.plot(xs, ys)
    plt.show()
