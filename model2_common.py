def mu_i(mu, Nk, N_avg, i):
    return mu * min(Nk, N_avg - i)


def nu_i(nu, Np, i):
    return nu * min(Np, i)