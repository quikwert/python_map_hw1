import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from pyproj import transform



def create_map(center_lon=20):
    fig = plt.figure()
    ax = plt.axes(
        projection=ccrs.PlateCarree(central_longitude=center_lon)
    )
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    ax.set_extent([-20, 50, 25, 65], crs=ccrs.PlateCarree())

    return fig, ax

def create_artists(ax, n_lines):
    lines = []

    for _ in range(n_lines):
        line, = ax.plot([], [], transform=ccrs.PlateCarree())
        lines.append(line)

    return lines


def export_map(path, datasets):
    fig, ax = create_map()
    colors = ["red", "blue"]

    for dataset, color in zip(datasets, colors):
        for lons, lats in dataset:
            ax.plot(lons,lats,color=color,transform=ccrs.PlateCarree(), alpha=0.5)

        fig.savefig(path, dpi=300, bbox_inches="tight")
        plt.close(fig)
