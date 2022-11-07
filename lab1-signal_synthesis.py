import math
import matplotlib.pyplot as plt


def S(t_val, ak_list, bk_list, w_val):
    result = 2.2
    k_val = 1
    for i in range(20):
        result += ak_list[i] * math.cos(k_val * w_val * t_val) + bk_list[i] * math.sin(k_val * w_val * t_val)
        k_val += 1
    return result


if __name__ == '__main__':
    w = 188.6
    T = 0.0333

    ak = []
    bk = []
    for k in range(1, 21):
        ak.append(((367956302 * k * math.sin((104673 * k) / 25000)) - (8788233 * math.cos((104673 * k) / 25000))) /
                  ((364849349 * k ** 2) + 208124) + 9712500 / ((364849349 * k ** 2) + 208124))
        bk.append((406654605 * k - (8788233 * math.sin((104673 * k) / 25000)) -
                   (367956302 * k * math.cos((104673 * k) / 25000))) / ((364849349 * k ** 2) + 208124))

    print("Ak")
    for val in ak:
        print("%.4f" % val)
    print("----------------")

    print("Bk")
    for val in bk:
        print("%.4f" % val)
    print("----------------")

    print("sqrt(Ak^2 + Bk^2)")
    for i in range(len(ak)):
        print("%.4f" % math.sqrt(ak[i] ** 2 + bk[i] ** 2))
    print("----------------")

    print("arctg(Bk/Ak)")
    for i in range(len(ak)):
        print("%.4f" % math.atan(bk[i] / ak[i]))

    t = 0
    x_vals = []
    y_vals = []
    while t <= 2 * T:
        x_vals.append(t)
        y_vals.append(S(t, ak, bk, w))
        t += 0.00001
    plt.title("Graphic S(t)", fontdict={'family': 'serif', 'color': 'darkred', 'size': 18})
    plt.xlabel("t, c")
    plt.ylabel("S(t), B")
    plt.scatter(x_vals, y_vals, s=0.05)
    plt.show()
