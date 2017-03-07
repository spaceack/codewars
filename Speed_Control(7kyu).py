def gps(s, x):
    sections = []
    if len(x)<=1:
        return 0
    for t in range(len(x) - 1):
        sections.append(abs(x[t] - x [t + 1]))
    return int(max([ 3600 * c // s for c in sections]))
