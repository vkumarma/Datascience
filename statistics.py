from linear_algebra import dot, sum_of_squares
from typing import List
from collections import Counter
import math

# want to get some notion of where our data is centered
# mean is very sensitive to the outliers

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """ if len(xs) is odd, the median is the middle element """
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """ if len(xs) is even, it's the average of the middle two elements """
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """ Finds the 'middle-most' value of v """
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float],
             p: float) -> float:  # refers to value under which a certain percentile of data lies (median represents value under which 50% of the data lies)
    """ Returns the pth-percentile value in x """
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mode(x: List[float]) -> List[float]:  # most common values
    """ Returns a list, since there might be more than one mode"""
    counts = Counter(x)  # key, freq or num , freq
    max_count = max(counts.values())  # highest frequency
    return [x_i for x_i, count in counts.items() if count == max_count]


print("mode: ", mode(friends), "\n")
print("median: ", median(friends), "\n")
print("mean", mean(friends), "\n")


# dispersion refers to measures of how spread out our data is
# one simple measure is range
# more complex measure of dispersion is the variance

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


print(data_range(friends))


def de_mean(xs: List[float]) -> List[float]:
    """ Translate xs by subtracting its mean """

    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:  # average squared deviation from the mean
    """ Almost the average squared deviation from the mean """
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """ The standard deviation is the square root of the variance """
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    """ Returns the difference between 75%-ile and 25%-ile """
    return quantile(xs, 0.75) - quantile(xs, 0.25)


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


def correlation(xs: List[float], ys: list[float]) -> float:
    """ Measures how much xs and ys vary in tandem about their means """
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0  # if not variation, correlation is zero

# correlation = 1 perfectly correlated, 0 zero correlation, -1 perfect anti correlation, 0.25 weak correlation
