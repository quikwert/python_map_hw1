import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature



def create_map(center_lon=20):
    fig = plt.figure()
    ax = plt.axes(
        projection=ccrs.PlateCarree(central_longitude=center_lon)
    )
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    ax.set_extent([-25, 40, 35, 72], crs=ccrs.PlateCarree())

    return fig, ax

def create_artists(ax, n_lines):
    lines = []

    for _ in range(n_lines):
        line, = ax.plot([], [], transform=ccrs.PlateCarree())
        lines.append(line)

    return lines


