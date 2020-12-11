#!/usr/bin/env python
# coding: utf-8

import numpy as np

def TwoBox_read_IPCC_AR5_historical_forcing(forcing_dir):
    print('TwoBox_read_IPCC_AR5_historical_forcing: reading IPCC AR5 forcing data 1750-2011')
    year,co2_data,ghg_other_data,o3_tropos_data,o3_stratos_data,total_aero_data,landuse_data,h2o_stratos_data,bc_snow_data,contrails,solar_data,volc_data=(np.array(()),)*12
    with open(forcing_dir+'IPCC_AR5_historical_Forcings.txt', 'r') as f:
        for i,line in enumerate(f):
            if i > 1:       # skip header (first line)
                values=line.strip('\n').split()
                if not values:
                    continue   # skip last row in file if it is empty
                year=np.append(year, int(values[0]))
                co2_data=np.append(co2_data, float(values[1]))
                ghg_other_data=np.append(ghg_other_data, float(values[2]))
                o3_tropos_data=np.append(o3_tropos_data, float(values[3]))
                o3_stratos_data=np.append(o3_stratos_data, float(values[4]))
                total_aero_data=np.append(total_aero_data, float(values[5]))
                landuse_data=np.append(landuse_data, float(values[6]))
                h2o_stratos_data=np.append(h2o_stratos_data, float(values[7]))
                bc_snow_data=np.append(bc_snow_data, float(values[8]))
                contrails=np.append(contrails, float(values[9]))
                solar_data=np.append(solar_data, float(values[10]))
                volc_data=np.append(volc_data, float(values[11]))
    print('TwoBox_read_IPCC_AR5_historical_forcing: Finished')
    
    return year,co2_data,ghg_other_data,o3_tropos_data,o3_stratos_data,total_aero_data,landuse_data,h2o_stratos_data,bc_snow_data,contrails,solar_data,volc_data
      

