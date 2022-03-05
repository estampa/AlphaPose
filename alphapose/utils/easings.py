def linear_ease(p):
    return p


def cubic_ease_in(p):
    return p * p * p


def cubic_ease_out(p):
    f = p - 1
    return f * f * f + 1


def cubic_ease_in_out(p):
    if p < 0.5:
        return 4 * p * p * p
    else:
        f = ((2 * p) - 2)
        return 0.5 * f * f * f + 1
