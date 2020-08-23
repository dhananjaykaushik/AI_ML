points = [(2, 4), (4, 2)]


def F(w):
    return sum((w * x - y) ** 2 for x, y in points)


def dF(w):
    # Calculating derivative
    return sum(2 * (w * x - y) * x for x, y in points)


# Gradient Descent
w = 0
eta = 0.01      # Step size
for t in range(100):
    value = F(w)
    gradient = dF(w)
    w = w - (eta * gradient)

    print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))
