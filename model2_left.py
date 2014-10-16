from pprint import pprint

def _mu_i(mu, Nk, N_avg, i):
    return mu * min(Nk, N_avg - i)


def _nu_i(nu, Np, i):
    return nu * min(Np, i)


def solve(mu, nu, N_avg, Nk, Np):
    """
    :param mu: mu
    :type mu: float

    :param nu: nu
    :type nu: float

    :param N_avg: N
    :type N_avg int
    """
    
    # allocate array of N_avg+1 probabilities
    p = [0] * (N_avg+1)

    # calculate p[0]
    mu_accumulated = 1.0
    nu_accumulated = 1.0

    sum = 1.0
    for i in range(1, N_avg+1):
        mu_accumulated *= _mu_i(mu, Nk, N_avg, i-1)
        nu_accumulated *= _nu_i(nu, Np, i)

        p[i] = mu_accumulated / nu_accumulated
        sum += p[i]

    p[0] = 1.0/sum
    
    # calculate p[1:N_avg]
    for i in range(1, N_avg+1):
        p[i] *= p[0]

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
