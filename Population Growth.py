def nb_year(p0, percent, aug, p):
    percent = percent/100
    t = 0
    if (p0 >= p):
        return t
    while(p0<p):
        p0 = p0+ p0*percent +aug
        t += 1
    return t
