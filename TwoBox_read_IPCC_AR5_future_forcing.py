#!/usr/bin/env python
# coding: utf-8

import numpy as np

def TwoBox_read_IPCC_AR5_future_forcing(forcing_dir):
    #
    # PURPOSE
    # Read forcing data for future relative to 1850 [W/m2]
    #
    # The data is the ones from IPCC AR5 WGI
    # Annex II: Climate System Scenario Tables: Table AII.6.10
    #
    # The original websites for the data is are:
    # https://www.ipcc.ch/report/ar5/wg1/ 
    #
    # OUPTPUT
    # sresa1b,rcp26,rcp45,rcp60,rcp85: total  anthropogenic plus natural
    # effective radiative forcing (ERF)  [W/m2] 
    # for different scenarios
    #
    #
    # Author: Asgeir Sorteberg, 
    #         Geophysical Institute, University of Bergen.
    #         email: asgeir.sorteberg@gfi.uib.no
    #
    #         Jul. 2014
    ###########################################################################
    
    print('TwoBox_read_IPCC_AR5_future_forcing: reading IPCC AR5 forcing data 2010-2090')
    year,sresa1b,sresa1b_std,rcp26,rcp26_std,rcp45,rcp45_std,rcp60,rcp60_std,rcp85,rcp85_std=(np.array(()),)*11
    with open(forcing_dir+'IPCC_AR5_ScenarioForcings.txt', 'r', errors='ignore') as f:
        for i,line in enumerate(f):
            if i > 26 :       # skip header (first 27 lines)
                values=line.strip('\n').split()
                if not values:
                    continue   # skip last row in file if it is empty
                year=np.append(year, int(values[0]))
                sresa1b=np.append(sresa1b, float(values[1]))
                sresa1b_std=np.append(sresa1b_std, float(values[2]))
                rcp26=np.append(rcp26, float(values[3]))
                rcp26_std=np.append(rcp26_std, float(values[4]))
                rcp45=np.append(rcp45, float(values[5]))
                rcp45_std=np.append(rcp45_std, float(values[6]))
                rcp60=np.append(rcp60, float(values[7]))
                rcp60_std=np.append(rcp60_std, float(values[8]))
                rcp85=np.append(rcp85, float(values[9]))
                rcp85_std=np.append(rcp85_std, float(values[10]))
            
    print('TwoBox_read_IPCC_AR5_future_forcing: Finished')
    
    return year,sresa1b,sresa1b_std,rcp26,rcp26_std,rcp45,rcp45_std,rcp60,rcp60_std,rcp85,rcp85_std

