from pprint import pprint

def solve(la, nu_avg, N):
    """

    :param la: lambda
    :type la: float

    :param nu_avg: nu vector
    :type nu_avg: tuple

    :param N: N
    :type N int
    """
    
    # allocate array of N+1 probabilities
    p = [0] * (N+1)

    # calculate p[0]
    N_accumulated = 1.0
    la_accumulated = 1.0
    nu_avg_accumulated = 1.0

    sum = 1.0
    for i in range(1, N+1):
        N_accumulated *= N-i+1
        la_accumulated *= la
        nu_avg_accumulated *= nu_avg[i-1]

        p[i] = N_accumulated * la_accumulated / nu_avg_accumulated
        sum += p[i]

    p[0] = 1.0/sum
    
    # calculate p[1:N]
    for i in range(1, N+1):
        p[i] *= p[0]

    return p

if __name__ == "__main__":
    la = 0.1
    nu_avg = (1.0, 3.0, 1.0, 2.0)
    N = len(nu_avg)

    p = solve(la, nu_avg, N)
    pprint(p)
    print "Sum(p) = %f" % sum(p)
