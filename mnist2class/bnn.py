import math, random

def elog(x):
    return math.log(x) if x >= 1e-300 else -1000        

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

def fprop(x, w):
    yhat = [None] * len(x)
    for k in range(len(x)):
        a = [0] * 30
        for i in range(51):
            for j in range(30):
                a[j] += x[k][i] * (1 if w[i][j] > 0 else -1)
        a = [1 if _ > 0 else -1 for _ in a]
        yhat[k] = 0 if sum(a[:15]) >= sum(a[15:]) else 1
    return yhat

def bprop(x, y, yhat, w):
    dz = [yhat[i]-y[i] for i in range(len(y))]
    dw = [[None]*30 for _ in range(51)]
    for i in range(51):
        for j in range(15):
            dw[i][15+j] = sum([x[k][i]*dz[k] for k in range(len(y))]) / len(y)
            dw[i][j] = -dw[i][15+j]
    return dw
            

def cost(y, yhat):
    return -sum([y[i]*elog(yhat[i]) + (1-y[i])*elog(1-yhat[i])
                 for i in range(len(y))]) / len(y)

def acc(y, yhat):
    return 100*sum([int(y[i] == yhat[i]) for i in range(len(y))]) / len(y)

x, y = load_data('train.txt')
w = [[random.choice([-1, 1]) for j in range(30)] for i in range(51)]
alpha = 2
for e in range(10):
    yhat = fprop(x, w)
    j = cost(y, yhat); a = acc(y, yhat)
    print('Epoch %d: %f cost, %f%% accuracy.' % (e+1, j, a))
    dw = bprop(x, y, yhat, w)
    for i in range(51):
        for j in range(30):
            w[i][j] -= alpha * dw[i][j]
    if e == 5:
        alpha = 0.5
save_weights('weights.txt', w)
