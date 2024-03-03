import dataclasses
import typing

@dataclasses.dataclass
class Measurement:
    value: float
    timestamp: float
    location: tuple[float, float]
    error_estimate: tuple[float, float]


class Measurement(typing.NamedTuple):
    value: float
    timestamp: float
    location: tuple[float, float]
    error_estimate: tuple[float, float]


class Measurement(typing.TypedDict):
    value: float
    timestamp: float
    location: tuple[float, float]
    error_estimate: tuple[float, float]


def passing_structured_data_as_dict_or_tuple():
    # take some measurement
    measurement = 1.0001
    timestamp = ...
    location = ...
    error_estimate = ...

    data = {
        "measurement": measurement,
        "timestamp": timestamp,
        "location": location,
        "error_estimate": error_estimate,
    }

    data = (measurement, timestamp, location, error_estimate)

    return data
