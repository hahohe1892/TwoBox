#!/usr/bin/env python
# coding: utf-8

import numpy as np

def TwoBox_read_PMIP3_forcing(forcing_dir):
    #
    # PURPOSE
    # Read forcing data [W/m2]
    #
    # The data is the ones referenced in 
    # Schmidt et al (2010) "Climate forcing reconstructions for use in 
    # the PMIP simulations of the Last Millennium". 
    #
    # The original websites for the files are:
    # GHGs, Volc (CEA), solar reconstructions, orbital forcing:
    # https://pmip3.lsce.ipsl.fr/wiki/doku.php/pmip3:design:lm:final
    #
    # Volc (GRA): http://climate.envsci.rutgers.edu/IVI2/
    # Shindell et al (2006) Ozone parameterisation:
    # http://www.giss.nasa.gov/staff/gschmidt/dO3_shindell
    #
    # Vegetation reconstructions can be downloaded from:
    # http://cera-www.dkrz.de/WDCC/ui/Entry.jsp?acronym=RECON_LAND_COVER_800-1992
    #
    # OUPTPUT
    # wmghg_data      radiative forcing due to well-mixed greenhouse gas changes [W/m2] 
    # solar_data      radiative forcing due to solar forcing [W/m2]
    # volc_data       radiative forcing due to volcanic aerosols [W/m2]
    # landuse_data     radiative forcing due to landuse changes [W/m2]
    #
    # data read:
    # volc_data1: based on Gao, Robock and Ammmann
    # volc_data2: Based on Crowley et al
    #
    # solar_data1: based on Delaygue and Bard (no background)
    # solar_data2: based on Delaygue and Bard 
    # solar_data3: based on DMuscheler et al (no background)
    # solar_data4: based on DMuscheler et al 
    # solar_data5: based on Steinhilber, Beer and Froehlich
    # solar_data6: based on Vieira, Solanki and Krivova
    #
    # landuse_data: based on Pongratz et al. (2008)
    #
    # Author: Asgeir Sorteberg, 
    #         Geophysical Institute, University of Bergen.
    #         email: asgeir.sorteberg@gfi.uib.no
    #
    #           Feb. 2011
    #####################################################################################
    
    print('TwoBox_read_IPCC_PMIP3_forcing: reading PMIP3 forcing data 1750-2010')

    # well-mixed greenhouse gas changes (baseline 850 CE) 
    wmghg_year, wmghg_data=(np.array(()),)*2
    with open(forcing_dir+'wmghg.txt', 'r') as f:
        for i,line in enumerate(f):
            if i > 13:   # skip header (first 14 lines)
                values=line.strip('\n').split()
                wmghg_year=np.append(wmghg_year, int(values[0]))
                wmghg_data=np.append(wmghg_data,float(values[1].strip()))

    # volcanic aerosol forcing 
    volc_year, volc_data1, volc_data2=(np.array(()),)*3
    with open(forcing_dir+'volc.txt', 'r') as f:
        for i,line in enumerate(f):
            if i > 13:   # skip header (first 14 lines)
                values=line.strip('\n').split()
                volc_year=np.append(volc_year, int(values[0]))
                volc_data1=np.append(volc_data1, float(values[1].strip()))
                volc_data2=np.append(volc_data2, float(values[-1].strip()))

    # solar forcing (baseline PMOD 1976-2006))
    solar_year,solar_data1,solar_data2,solar_data3,solar_data4,solar_data5,solar_data6 = (np.array(()),)*7 
    with open(forcing_dir+'solar.txt', 'r') as f:
        for i,line in enumerate(f):
            if i > 23:       # skip header (first 24 lines)
                values=line.strip('\n').split()
                solar_year=np.append(solar_year, int(values[0].strip('.')))
                solar_data1=np.append(solar_data1,float(values[1]))
                solar_data2=np.append(solar_data2, float(values[2]))
                solar_data3=np.append(solar_data3, float(values[3]))
                solar_data4=np.append(solar_data4, float(values[4]))
                solar_data5=np.append(solar_data5, float(values[5]))
                solar_data6=np.append(solar_data6, float(values[6]))

    # landuse changes  (baseline pristine conditions)
    landuse_year, landuse_data=(np.array(()),)*2
    with open(forcing_dir+'landuse.txt', 'r') as f:
        for i,line in enumerate(f):
            if i > 13:    # skip header (first 14 lines)
                values=line.strip('\n').split()
                landuse_year=np.append(landuse_year, int(values[0]))
                landuse_data=np.append(landuse_data, float(values[1]))

    # rename
    wmghg_data=wmghg_data
    solar_data=solar_data2
    volc_data=volc_data1
    landuse_data=landuse_data

    print('TwoBox_read_IPCC_PMIP3_forcing: Finished')
    
    return wmghg_year, wmghg_data, solar_year, solar_data, volc_year, volc_data, landuse_year, landuse_data

