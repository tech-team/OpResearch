from pprint import pprint
import model1_left
import model1_right
from model2_common import nu_i
import model2_left
import model2_right


def _print_p(p):
    for i in xrange(0, len(p)):
        print 'p[%d] = %f' % (i, p[i])


def _compute_nu_avg(nu, p, N_avg, Np):
    s = 0.0
    for i in xrange(1, N_avg):
        s += nu_i(nu, Np, i) * p[i]
    return s


def _compute_N_avg(p):
    s = 0.0
    for i in xrange(0, len(p)):
        s += i * p[i]
    return s


def _compute_solve_time(N_avg, N, la):
    return N_avg / (la * (N - N_avg))


def perform(la, mu, nu, N, Nk, Np, model1_solve_func, model2_solve_func):
    nu_avg = ()

    for N_avg_i in xrange(1, N+1):
        p2 = model2_solve_func(mu, nu, N_avg_i, Nk, Np)
        nu_avg_i = _compute_nu_avg(nu, p2, N_avg_i, Np)
        nu_avg += (nu_avg_i,)

    p1 = model1_solve_func(la, nu_avg, N)

    print 'p1: '
    _print_p(p1)

    print 'Sum(p1): %f' % sum(p1)

    N_avg = _compute_N_avg(p1)
    print 'N_avg = %f' % N_avg
    print 'Solve time = %f' % _compute_solve_time(N_avg, N, la)

    print '------------------'

    N_avg_int = int(round(N_avg))
    p2_try2 = model2_solve_func(mu, nu, N_avg_int, Nk, Np)
    nu_avg_try2 = _compute_nu_avg(nu, p2_try2, N_avg_int, Np)

    print 'nu_avg (try1):'
    pprint(nu_avg)

    print 'nu_avg (try2):'
    pprint(nu_avg_try2)


if __name__ == "__main__":
    la = 0.1
    mu = 0.1
    nu = 1
    N = 4
    Nk = 3
    Np = 4

    perform(la, mu, nu, N, Nk, Np, model1_right.solve, model2_right.solve)