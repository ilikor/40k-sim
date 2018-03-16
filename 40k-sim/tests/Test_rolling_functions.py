import pytest
import numpy
from DiceSim2 import RollingFunctions as rf


def test_rollingd6_interface(number):
    values = rf.rollingd6s(number)
    assert len(values) == 6


def test_rollingd6_no_lost_dices(number):
    values = rf.rollingd6s(number)
    assert numpy.sum(values) == number


def test_rollingd6_dist(number):
    values = rf.rollingd6s(number)
    assert numpy.sqrt(number) > numpy.max(values) - numpy.average(values)
    assert numpy.sqrt(number) > numpy.average(values) - numpy.min(values)


def test_rerolld6_interface(number, reroll_target):
    values = rf.rollingd6s(number)
    reroll = rf.reroll_d6s(values, reroll_target)
    assert len(reroll) == 6


def test_rerolld6_no_lost_dices(number, reroll_target):
    values = [number, 0, 0, 0, 0, 0]
    reroll = rf.reroll_d6s(values, reroll_target)
    assert numpy.sum(reroll) == number


def test_rerolld6_negative_reroll(value):
    false_reroll = -2
    with pytest.raises(ValueError):
        rf.reroll_d6s(value, false_reroll)


def test_rollingdx_time(number):
    assert len(rf.rollingdxs_time_dependant(number, 7)) == number

