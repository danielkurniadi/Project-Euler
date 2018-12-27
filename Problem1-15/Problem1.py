def solve(n):
    n_terms_3 = n//3
    n_terms_5 = n//5
    n_terms_15 = n//15
    
    s_3 = n_terms_3*(n_terms_3*3+3)//2
    s_5 = n_terms_5*(n_terms_5*5+5)//2
    s_15 = n_terms_15*(n_terms_15*15+15)//2
    print(s_3, s_5, s_15)

    return s_3 + s_5 - s_15

if __name__ == '__main__':
    solution = solve(1000)
    print(solution)
