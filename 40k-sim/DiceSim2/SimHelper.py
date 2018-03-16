import numpy
from DiceSim2.Attack import Attack
from DiceSim2.Defense import Defense
from DiceSim2.RollingFunctions import rollingdxs


def damage_string_reader(dmg):
    """

    Parameters
    ----------
    dmg : str

    Returns
    -------
    (int, int)

    """
    split = dmg.split("d")
    if len(split) > 1:
        return int(split[0]), int(split[1])

    else:
        return int(split[0]), 1


def determine_attack(attack):
    """

    Parameters
    ----------
    attack : Attack

    Returns
    -------
    int

    """

    nb, dx = damage_string_reader(attack.attack)
    results = rollingdxs(nb, dx)
    w = numpy.arange(1, len(results) + 1, 1)
    return int(numpy.inner(results, w))


def determine_wound_roll(attack, target):
    """

    Parameters
    ----------
    attack : Attack
    target : Defense

    Returns
    -------

    """

    stra = attack.str
    tt = target.t
    wound_roll = 4

    if stra >= 2 * tt:

        wound_roll = 2

    elif stra > tt:

        wound_roll = 3

    elif 2 * stra <= tt:

        wound_roll = 6

    elif stra < tt:

        wound_roll = 5

    return wound_roll


def determine_save(attack, target):
    """

    Parameters
    ----------
    attack : Attack
    target : Defense

    Returns
    -------

    """

    apa = attack.ap
    save = target.sv

    if apa == "MW":
        return 7

    mod_save = save - apa

    if target.isv is not None:

        if mod_save < target.isv:
            mod_save = target.isv

    return mod_save
