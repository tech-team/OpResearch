from pprint import pprint
import model1_left
import model1_right
from model2_common import nu_i
import model2_left
import model2_right


def print_p(p):
    s = ''
    for i in xrange(0, len(p)):
        s += ('p[%d] = %.30f' % (i, p[i])) + ' <br> '
    return s


def _compute_nu_avg(nu, p, N_avg, Np):
    s = 0.0
    for i in xrange(1, N_avg + 1):
        s += nu_i(nu, Np, i) * p[i]
    return s


def _compute_N_avg(p):
    s = 0.0
    for i in xrange(0, len(p)):
        s += i * p[i]
    return s


def _compute_solve_time(N_avg, N, la):
    return N_avg / (la * (N - N_avg))


def _perform(la, mu, nu, N, Nk, Np, model1_solve_func, model2_solve_func):
    nu_avg = ()

    for N_avg_i in xrange(1, N+1):
        p2 = model2_solve_func(mu, nu, N_avg_i, Nk, Np)
        nu_avg_i = _compute_nu_avg(nu, p2, N_avg_i, Np)
        nu_avg += (nu_avg_i,)

    p1 = model1_solve_func(la, nu_avg, N)

    print 'p1: '
    print print_p(p1)

    print 'Sum(p1): %f' % sum(p1)

    N_avg = _compute_N_avg(p1)
    solve_time = _compute_solve_time(N_avg, N, la)
    print 'N_avg = %f' % N_avg
    print 'Solve time = %f' % solve_time

    print '------------------'

    N_avg_int = int(round(N_avg))
    p2_try2 = model2_solve_func(mu, nu, N_avg_int, Nk, Np)
    nu_avg_try2 = _compute_nu_avg(nu, p2_try2, N_avg_int, Np)

    print 'nu_avg (try1):'
    pprint(nu_avg)

    print 'nu_avg (try2):'
    pprint(nu_avg_try2)

    return p1, N_avg, solve_time


def perform(la, mu, nu, N, Nk, Np, model_type):
    model1_solve_func = None
    model2_solve_func = None

    if model_type == 'left':
        model1_solve_func = model1_left.solve
        model2_solve_func = model2_left.solve
    elif model_type == 'right':
        model1_solve_func = model1_right.solve
        model2_solve_func = model2_right.solve

    return _perform(la, mu, nu, N, Nk, Np, model1_solve_func, model2_solve_func)


if __name__ == "__main__":
    la = 2
    mu = 1
    nu = 0.2
    N = 4
    Nk = 1
    Np = 2
    model_type = 'left'
    # model_type = 'right'
