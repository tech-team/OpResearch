from pprint import pprint


def _compute_coefs(la, nu_avg, N):
    coefs = []
    addings = [1]

    for x in xrange(1, N+1):
        coefs.append(nu_avg[-x]/(x * la))
        addings.append(coefs[-1] * addings[-1])

    return coefs, addings


def solve(la, nu_avg, N):
    """

    :param la: lambda
    :type la: float

    :param nu_avg: nu vector
    :type nu_avg: tuple

    :param N: N
    :type N int
    """

    p = []
    coefs, addings = _compute_coefs(la, nu_avg, N)

    p.append(1.0 / sum(addings))

    for i in xrange(0, N):
        p_i = p[-1] * coefs[i]
        p.append(p_i)

    p = list(reversed(p))

    return p


if __name__ == "__main__":
    la = 0.1
    nu_avg = (1, 3, 1, 2)
    N = len(nu_avg)

    p = solve(la, nu_avg, N)
    pprint(p)
    print "Sum(p) = %f" % sum(p)