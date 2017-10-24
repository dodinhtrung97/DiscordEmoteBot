def draw_type_of(random_rate):
    ssr_rate = 3
    sr_rate = 15
    r_rate = 82

    if random_rate < ssr_rate:
        return "SSR"
    elif random_rate > ssr_rate and random_rate < (sr_rate + ssr_rate):
        return "SR"
    elif random_rate > sr_rate and random_rate < (ssr_rate + sr_rate + r_rate):
        return "R"

def letter_type(draw_type):
    if draw_type == "R":
        return "*"
    elif draw_type == "SR":
        return "**"
    return "***"
