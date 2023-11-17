import click
import numpy as np
from numpy import pi
import pandas as pd



@click.group()
def cmd_group():
    pass
@cmd_group.command()

@click.option(
    "-n",
    "--number",
    default=10,
)
def sin(number):
    """sinus in a table

    Args:
        number (int): the amount of rows between zero and two pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()