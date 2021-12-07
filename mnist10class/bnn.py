import random

def load_data(f):
    with open(f) as fin:
        x = []; y = []
        for line in fin:
            xy = [int(_) for _ in line.split()]
            x.append(xy[:-1])
            y.append(xy[-1])
    return x, y

def save_weights(f, w):
    with open(f, 'w') as fout:
        for i in range(len(w)):
            fout.write(' '.join(str(_) for _ in w[i]) + '\n')

def read_weights(f):
    with open(f) as fin:
        return [[float(_) for _ in line.split()] for line in fin]

def fprop(x, w):
    yhat = [None] * len(x)
    for k in range(len(x)):
        a = [0] * 150
        for i in range(51):
            for j in range(150):
                a[j] += x[k][i] * (1 if w[i][j] > 0 else -1)
        a = [1 if _ > 0 else -1 for _ in a]
        b = [sum(a[i*15:(i+1)*15]) for i in range(10)]
        yhat[k] = b.index(max(b))
    return yhat

def bprop(x, y, yhat, w):
    dz = [[0]*10 for _ in range(len(y))]
    for k in range(len(y)):
        dz[k][yhat[k]] += 1
        dz[k][y[k]] -= 1
    dw = [[None]*150 for _ in range(51)]
    for i in range(51):
        for j in range(10):
            for p in range(15):
                dw[i][j*15+p] = (sum(x[k][i]*dz[k][j] for k in range(len(y)))
                                 / len(y))
    return dw

def acc(y, yhat):
    return 100*sum([int(y[i] == yhat[i]) for i in range(len(y))]) / len(y)

x, y = load_data('train.txt')
# w = [[random.choice([-1, 1]) for j in range(150)] for i in range(51)]
w = read_weights('weights3.txt')
# 4 epochs with alpha = 10, 8 epochs with alpha = 2, 8 epochs with alpha = 1
alpha = 1
for e in range(4):
    yhat = fprop(x, w)
    a = acc(y, yhat)
    print('Epoch %d: %f%% accuracy.' % (e+1, a))
    dw = bprop(x, y, yhat, w)
    for i in range(51):
        for j in range(150):
            w[i][j] -= alpha * dw[i][j]
save_weights('weights4.txt', w)
