def shumaShifrave(n:int)->int:
    """
    Funksioni kthen shume e shifrave te nurmit n. Per numrat negativ ruhet dhe shenja
    shumaShifrave (-123) kthen -6
    :param n:
    :return:
    """
    return sum([int(ch) for ch in str(n)]) if n >= 0 \
        else -1 * sum([int(ch) for ch in str(abs(n))])