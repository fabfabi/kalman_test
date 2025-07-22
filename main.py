# %%
import numpy as np
import seaborn as sns


# %%
def parabola_1(x, x_min=0, x_max=10, height=2):
    """simple parabola that goes through x_min and x_max and has the maximum in the middle at 'height'"""
    return -(x - x_min) * (x - x_max) / (x_max - x_min) ** 2 * 4 * height


def data_faker(x_grid: np.ndarray, fun=parabola_1, height=2, noise=2):
    """simple data faker to create some data"""
    x_min = x_grid.min()
    x_max = x_grid.max()

    return np.array(
        [
            fun(
                x,
                x_min=x_min,
                x_max=x_max,
                height=height,
            )
            for x in x_grid
        ]
    ) + noise * np.random.normal(size=(x_grid.size,))


# %%
x_grid = np.linspace(0, 10, 100)
y_grid = data_faker(x_grid)
# %%
fig = sns.lineplot(x_grid, y_grid)
# %%
