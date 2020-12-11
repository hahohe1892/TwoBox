#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy import interpolate
from TwoBox_read_IPCC_AR5_future_forcing import TwoBox_read_IPCC_AR5_future_forcing
from TwoBox_read_IPCC_AR5_historical_forcing import TwoBox_read_IPCC_AR5_historical_forcing
from TwoBox_read_PMIP3_forcing import TwoBox_read_PMIP3_forcing


def TwoBox_calc_FORCINGS(forcing_dataset, forcing_dir, base_syr, base_eyr):
    #
    # PURPOSE
    # read radiative forcings (W/m2) and rescale according to base period
    # all forcings except volcanoes are on avg. 0 over base period.
    # NOTE: Volcanoes are not scaled in order to keep the forcing to
    #       0 when there are no volcanoes.
    #
    # Input
    # forcing_dataset: IPCC_AR5_HISTORICAL
    #                  IPCC_AR5_HISTORICAL_RCP26
    #                  IPCC_AR5_HISTORICAL_RCP45
    #                  IPCC_AR5_HISTORICAL_RCP60
    #                  IPCC_AR5_HISTORICAL_RCP85
    #                  PMIP3
    # forcing_dir: Directory to forcing data
    # base_syr, base_eyr: beginning and end year of base period relative to which forcing is calculated
    # 
    #
    # OUTPUT
    # total_forcing: sum of radiative forcing from wmghg+solar+volc+landuse+manaero [W/m2]
    # wmghg         radiative forcing due to well-mixed greenhouse gas changes [W/m2]
    # solar      radiative forcing due to solar forcing [W/m2]
    # volc       radiative forcing due to volcanic aerosols [W/m2]
    # landuse     radiative forcing due to landuse changes [W/m2]
    # manaero     radiative forcing due to manmande aerosols [W/m2]
    #
    #
    # USES TwoBox_read_PMIP3_forcing.m
    #      TwoBox_read_IPCC_AR5_historical_forcing.m
    #      TwoBox_read_IPCC_AR5_scenario_forcing.m
    #
    # Author: Asgeir Sorteberg,
    #         Geophysical Institute, University of Bergen.
    #         email: asgeir.sorteberg@gfi.uib.no
    #
    #         Feb. 2011
    ###############################################################################################
    
    if forcing_dataset.upper().strip() == 'PMIP3':
        print('TwoBox_calc_FORCINGS: Using forcing dataset: ' + forcing_dataset.upper().strip())
    
        #read PMI3 forcings from Schmidt et al. 2010
        wmghg_year,wmghg_data,solar_year,solar_data,volc_year,volc_data,landuse_year,landuse_data=TwoBox_read_PMIP3_forcing(forcing_dir)
    
        #add some data to landuse since it only goes to 1992;
        #Assume data from 1992 and onwards same as 1992
        print('TwoBox_calc_FORCINGS: Landuse forcings only goes to 1992: Assume constant forcing after this')
        landuse_year=np.append(landuse_year, np.arange(1993,wmghg_year[-1]+1))
        landuse_data=np.append(landuse_data, [landuse_data[-1]]*len(np.arange(1993,wmghg_year[-1]+1)))

        indx_wmghg=np.logical_and(wmghg_year>=base_syr, wmghg_year<=base_eyr)
        wmghg_data=wmghg_data-np.mean(wmghg_data[indx_wmghg])
    
        indx_solar=np.logical_and(solar_year>=base_syr, solar_year<=base_eyr)
        solar_data=solar_data-np.mean(solar_data[indx_solar])
    
        indx_landuse=np.logical_and(landuse_year>=base_syr, landuse_year<=base_eyr)
        landuse_data=landuse_data-np.mean(landuse_data[indx_landuse])
    
        #read in  aerosol forcing from GISS data
        print('TwoBox_calc_FORCINGS: No manmade aerosol forcing in PMI3 using GISS direct aerosol forcing')
        giss_file=forcing_dir+'GISS_FORCING_data.txt'
        giss_yr, giss_ghg, giss_ozone, giss_StratH20, giss_solar, giss_LandUse, giss_SnowAlb, giss_StratAer, giss_BC, giss_ReflAer, giss_AIE=(np.array(()),)*11 
        with open(giss_file, 'r') as f:
            for i,line in enumerate(f):
                if i > 9:   # skip header (first 10 lines)
                    values=line.strip('\n').split()
                    giss_yr=np.append(giss_yr, float(values[0]))
                    giss_ghg=np.append(giss_ghg, float(values[1]))
                    giss_ozone=np.append(giss_ozone, float(values[2]))
                    giss_StratH20=np.append(giss_StratH20, float(values[3]))
                    giss_solar=np.append(giss_solar, float(values[4]))
                    giss_LandUse=np.append(giss_LandUse, float(values[5]))
                    giss_SnowAlb=np.append(giss_SnowAlb, float(values[6]))
                    giss_StratAer=np.append(giss_StratAer, float(values[7]))
                    giss_BC=np.append(giss_BC, float(values[8]))
                    giss_ReflAer=np.append(giss_ReflAer, float(values[9]))
                    giss_AIE=np.append(giss_AIE, float(values[10]))
                
        # total aerosol forcing (not indirect effect)
        manaero_data=giss_BC+giss_ReflAer
    
        # add some data to  since it only goes from 1880;
        # Assume data from 0 up to 1800
        print('TwoBox_calc_FORCINGS: Manmade aerosol forcing assumed to be zero before 1800')
        manaero_year=np.concatenate((np.arange(wmghg_year[0],1879+1), giss_yr))
        manaero_data=np.concatenate((np.zeros(len(np.arange(wmghg_year[0], 1879+1))),manaero_data))
    
        # Only use data to year 2000
        end_indx=int(np.where(manaero_year==2000)[0])+1
        manaero_year=manaero_year[0:end_indx]
        manaero_data=manaero_data[0:end_indx]
    
        indx_manaero=np.logical_and(manaero_year>=base_syr, manaero_year<=base_eyr)
        manaero_data=manaero_data-np.mean(manaero_data[indx_manaero])
    
        #total forcings
        total_year=wmghg_year
        total_forcing=wmghg_data+solar_data+volc_data+landuse_data+manaero_data

    elif forcing_dataset.upper().strip() in ['IPCC_AR5_HISTORICAL_RCP26', 'IPCC_AR5_HISTORICAL_RCP45', 'IPCC_AR5_HISTORICAL_RCP60', 'IPCC_AR5_HISTORICAL_RCP85']:
        #read IPCC AR5 forcings 1750-2100
        #historical data   
        hist_year,hist_co2_data,hist_ghg_other_data,hist_o3_tropos_data,hist_o3_stratos_data,hist_total_aero_data,hist_landuse_data,hist_h2o_stratos_data,hist_bc_snow_data,hist_contrails,hist_solar_data,hist_volc_data=TwoBox_read_IPCC_AR5_historical_forcing(forcing_dir)
    
        # total historical forcing
        # if only historical use all forcings
        if forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL':
            hist_total_forcing=hist_co2_data+hist_ghg_other_data+hist_total_aero_data+hist_landuse_data+hist_solar_data+hist_volc_data
    
        # if historical + scenario do nto use solar and volcanic as they are not in scenarios 
        elif forcing_dataset.upper().strip() in ['IPCC_AR5_HISTORICAL_RCP26', 'IPCC_AR5_HISTORICAL_RCP45', 'IPCC_AR5_HISTORICAL_RCP60', 'IPCC_AR5_HISTORICAL_RCP85']:
              hist_total_forcing=hist_co2_data+hist_ghg_other_data+hist_total_aero_data+hist_landuse_data
            
        # scenario data
        scen_year,sresa1b,sresa1b_std,rcp26,rcp26_std,rcp45,rcp45_std,rcp60,rcp60_std,rcp85,rcp85_std=TwoBox_read_IPCC_AR5_future_forcing(forcing_dir)
        if forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL_RCP26':
            scen_total_forcing=rcp26
        elif forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL_RCP45':
            scen_total_forcing=rcp45
        elif forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL_RCP60':
            scen_total_forcing=rcp60
        elif forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL_RCP85':
            scen_total_forcing=rcp85
    
        # interpolate forcing to each year
        scen_year2=np.arange(scen_year[0], scen_year[-1]+1)
        scen_total_forcing_interp_fun=interpolate.interp1d(scen_year, scen_total_forcing, 'linear')
        scen_total_forcing_interp=scen_total_forcing_interp_fun(scen_year2)
    
        # put data together
        year=np.concatenate((hist_year[:-2], scen_year2))
        total_forcing=np.concatenate((hist_total_forcing[:-2], scen_total_forcing_interp))
    
        # -----------
        # merge them to not get a jump going from historical to scenario
        # -----------
        # Linear weight between historical and scenario forcings over the
        # period merge_yr_low to merge_yr_high
        merge_yr_low=2000
        merge_yr_high=2022
        transition=np.arange(merge_yr_low, merge_yr_high+1)
    
        weight=(year-merge_yr_low)/(merge_yr_high-merge_yr_low)
        weight[year>merge_yr_high]=1
        weight[year<merge_yr_low]=0
    
        scen_total_forcing_extrap_fun=interpolate.interp1d(scen_year, scen_total_forcing, fill_value='extrapolate')
        scen_total_forcing_extrap=scen_total_forcing_extrap_fun(transition)
    
        hist_total_forcing_extrap_fun=interpolate.interp1d(hist_year, hist_total_forcing, fill_value='extrapolate')
        hist_total_forcing_extrap=hist_total_forcing_extrap_fun(transition)

        indx=np.intersect1d(year,transition, return_indices=True)[1]
        total_forcing[indx]=(weight[indx]*scen_total_forcing_extrap)+((1-weight[indx])*hist_total_forcing_extrap)
        total_year=year
    
        # individual components does no exist
        wmghg_year=np.NaN
        wmghg_data=np.NaN
        solar_year=np.NaN
        solar_data=np.NaN
        volc_year=np.NaN
        volc_data=np.NaN
        landuse_year=np.NaN
        landuse_data=np.NaN
        manaero_year=np.NaN
        manaero_data=np.NaN

    elif forcing_dataset.upper().strip() == 'IPCC_AR5_HISTORICAL':
        # read IPCC AR5 forcings 1750-2011
        year,co2_data,ghg_other_data,o3_tropos_data,o3_stratos_data,total_aero_data,landuse_data,h2o_stratos_data,bc_snow_data,contrails,solar_data,volc_data=TwoBox_read_IPCC_AR5_historical_forcing(forcing_dir)
    
        # total forcing
        total_year=year
        total_forcing=co2_data+ghg_other_data+total_aero_data+landuse_data+solar_data+volc_data
    
        # rename
        wmghg_year=year
        wmghg_data=co2_data+ghg_other_data
        solar_year=year
        solar_data=solar_data
        volc_year=year
        volc_data=volc_data
        landuse_year=year
        landuse_data=landuse_data
        manaero_year=year
        manaero_data=total_aero_data

    else:
        print('TwoBox_calc_FORCINGS: ERROR: Forcing dataset not recognized')

    print('TwoBox_calc_FORCINGS:Finished')
    
    return total_year,total_forcing,wmghg_year,wmghg_data,solar_year,solar_data,volc_year,volc_data,landuse_year,landuse_data,manaero_year,manaero_data

