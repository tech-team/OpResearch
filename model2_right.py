from pprint import pprint
from model2_common import nu_i, mu_i


def _compute_coefs(mu, nu, N_avg, Nk, Np):
    coefs = []
    addings = [1]

    for i in xrange(N_avg, 0, -1):
        nu__i = nu_i(nu, Np, i)
        mu__i = mu_i(mu, Nk, N_avg, i-1)

        coefs.append(nu__i / mu__i)
        addings.append(coefs[-1] * addings[-1])

    return coefs, addings


def solve(mu, nu, N_avg, Nk, Np):
    """

    :param mu: mu
    :type mu: float

    :param nu: nu
    :type nu: float

    :param N_avg: N
    :type N_avg int
    """

    p = []
    coefs, addings = _compute_coefs(mu, nu, N_avg, Nk, Np)

    p.append(1.0 / sum(addings))

    for i in xrange(0, N_avg):
        p_i = p[-1] * coefs[i]
        p.append(p_i)

    p = list(reversed(p))

    return p


if __name__ == "__main__":
    mu = 0.1
    nu = 1
    N_avg = 10
    Nk = 3
    Np = 4

    p = solve(mu, nu, N_avg, Nk, Np)
    pprint(p)
    print "Sum(p) = %f" % sum(p)
