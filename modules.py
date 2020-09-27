'''
All materials to visual Sentinel-5p data
'''
try:
    import xarray as xr # import xarray
    from matplotlib import pyplot as plt
    import numpy as np
    import cartopy.crs as ccrs
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
except:
    print('please install xarray, matplotlib, cartopy, numpy library in your python')

#choose space for stick axis
def vl_stick(dau,cuoi):
    a = np.array([])
    for i in range(dau,cuoi,5):
        a = np.append(a,i)
    return a
'''
NO2 section
- extract data
- plot data
'''
###############################
##### Extract data of NO2 #####
#### Data NO2 precision #####
def no2_pre(file):
    data5p = xr.open_dataset(file, group='PRODUCT')
    no2_data = data5p['nitrogendioxide_tropospheric_column_precision'][0,:,:]
    lats=no2_data.coords['latitude'].values
    lons=no2_data.coords['longitude'].values
    pack_data= {'data': no2_data,
                'lats': lats,
                'lons': lons}
    return pack_data
   

#### Data NO2 collum #####
def no2_col(file):
    data5p = xr.open_dataset(file, group='PRODUCT')
    no2_data = data5p['nitrogendioxide_tropospheric_column'][0,:,:]
    lats=no2_data.coords['latitude'].values
    lons=no2_data.coords['longitude'].values
    pack_data= {'data': no2_data,
                'lats': lats,
                'lons': lons}
    return pack_data
###########################
####NO2_plot###############
def plot_for_no2(data, lons, lats, check):
    plt.figure(figsize=(20,10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    extent=[int(np.amin(lons)), int(np.amax(lons)), int(np.amin(lats)), int(np.amax(lats))]
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    cot_lons=vl_stick(extent[0],extent[1]) 
    cot_lats=vl_stick(extent[2],extent[3])             
    ax.set_xticks(cot_lons, crs=ccrs.PlateCarree())
    ax.set_yticks(cot_lats, crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    data.plot.pcolormesh(ax=ax, x='longitude',
                         y='latitude',
                         add_colorbar=True,
                         cmap='jet',
                         transform=ccrs.PlateCarree())
    date=str(data.time.coords)
    plt.title(f'NO2 in atmosphere at {date[41:]}')
    plt.savefig(f'export/plot_{check}_{date[41:]}.png', dpi = 300)

'''
SO2 section
- extract data
- plot data
'''
###############################
##### Extract data of SO2 #####
#### Data SO2 precision #######

def so2_pre(file):
    data5ps = xr.open_dataset(file, group='PRODUCT')
    so2 = (data5ps['sulfurdioxide_total_vertical_column_precision'])
    lats = data5ps.data_vars['latitude'].values[0]
    lons = data5ps.data_vars['longitude'].values[0]
    pack_data = {'data': so2,
                'lats': lats,
                'lons': lons}
    return pack_data

###############################
##### Extract data of SO2 #####
#### Data SO2 collum #######

def so2_col(file):
    data5ps = xr.open_dataset(file, group='PRODUCT')
    so2 = (data5ps['sulfurdioxide_total_vertical_column'])
    lats = data5ps.data_vars['latitude'].values[0]
    lons = data5ps.data_vars['longitude'].values[0]
    pack_data = {'data': so2,
                'lats': lats,
                'lons': lons}
    return pack_data

#############################
#### SO2_plot ###############
def plot_for_so2(so2_data, lons, lats, check):
    unit = so2_data.units
    data=so2_data.values[0]
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    ax.coastlines()
    extent=[int(np.amin(lons)), int(np.amax(lons)), int(np.amin(lats)), int(np.amax(lats))]
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    cot_lons=vl_stick(extent[0],extent[1]) 
    cot_lats=vl_stick(extent[2],extent[3])             
    ax.set_xticks(cot_lons, crs=ccrs.PlateCarree())
    ax.set_yticks(cot_lats, crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xlabel("Longitude", fontsize = 12)
    ax.set_ylabel("Latitude", fontsize = 12)
    plot = ax.pcolormesh(lons,\
                          lats,\
                          data,\
                          transform=ccrs.PlateCarree())
    date=str(so2_data.time.values)
    plt.title(f'SO2 in atmosphere at {date[2:12]}')
    axpos = ax.get_position()
    cbar_ax = fig.add_axes([axpos.x1+0.05,axpos.y0,0.03,axpos.height])
    cbar = fig.colorbar(plot, cax = cbar_ax)
    cbar.ax.tick_params(labelsize = 12)
    cbar.set_label(f'{check} [{unit}]', labelpad = 15)
    plt.savefig(f'export/plot_{check}_{date[2:12]}.png', dpi = 300)