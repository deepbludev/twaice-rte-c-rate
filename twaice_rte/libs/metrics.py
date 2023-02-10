import pandas as pd


def rte(df: pd.DataFrame) -> float:
    """Calculates the RTE (Roundtrip efficiency) of a battery.

    The RTE is the ratio of the discharged energy to the charged energy.
    For the given data, the RTE is calculated as follows:
        - Calculate the total charged and discharged energy.
        - Calculate the SoC factor as the ratio of the total charge to discharge.
        - Multiply the two ratios to get the RTE.

    The data should come in the form of a CSV file with the following columns:
        - soc: State of charge of the battery in percent [0, 100].
        - current: Current flowing into the battery.
        - voltage: Voltage of the battery.

    It is assumed that the data is sampled at equidistant intervals.

    Args:
        df (pd.DataFrame): DataFrame containing the battery data

    Returns:
        The RTE of the battery as a [0,1] float.
    """

    cols = ["soc", "current", "voltage"]

    charge = df[df["current"] > 0][cols]
    discharge = df[df["current"] < 0][cols]

    charged_energy = charge["current"] * charge["voltage"]
    discharged_energy = discharge["current"].abs() * discharge["voltage"]

    soc_charge = charge["soc"].diff().abs().sum()
    soc_discharge = discharge["soc"].diff().abs().sum()
    soc_factor: float = soc_charge / soc_discharge

    rte: float = soc_factor * discharged_energy.sum() / charged_energy.sum()
    return rte


def c_rate(df: pd.DataFrame, capacity: float) -> float:
    """Calculates the C-rate of a battery.

    The C-rate is the ratio of the total current to the capacity of the battery.
    For the given data, the C-rate is calculated as follows:
        - Calculate the total charge and discharge current.
        - Calculate the SoC factor as the ratio of the total charge / discharge to 100%.
        - Multiply the two ratios to get the C-rate.

    The data should come in the form of a CSV file with the following columns:
        - soc: State of charge of the battery in percent [0, 100].
        - current: Current flowing into the battery.
    """

    total_current = df["current"].abs().sum()
    soc_factor = 100 / df["soc"].diff().abs().sum()

    c_rate: float = soc_factor * total_current / (capacity * 3600)
    return c_rate
