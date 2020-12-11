#!/usr/bin/env python
# coding: utf-8

# --------------------
# Simulation name
# --------------------
sim_name='TwoBox_simulation'

# --------------------
# forcing data and directory to forcing data
# --------------------

# name of forcing data
#  Alternatives;
#  IPCC_AR5_HISTORICAL       : 1750-2011: Forcings from IPCC AR5
#  IPCC_AR5_HISTORICAL_RCP26 : 1750-2100: Historical+rcp2.6 forcings from IPCC AR5
#  IPCC_AR5_HISTORICAL_RCP45 : 1750-2100: Historical+rcp4.5 forcings from IPCC AR5
#  IPCC_AR5_HISTORICAL_RCP60 : 1750-2100: Historical+rcp6.0 forcings from IPCC AR5
#  IPCC_AR5_HISTORICAL_RCP85 : 1750-2100: Historical+rcp8.5 forcings from IPCC AR5
#  PMIP3                     : Forcings as reported in Schmidt et al (2012) "Climate forcing 
#                              reconstructions for use in the PMIP simulations of the Last
#                              Millennium". 
forcing_dataset='IPCC_AR5_HISTORICAL'

# Diretory to forcing data
forcing_dir='./FORCING_DATA/'


# --------------------
# Forcing switches [n=1 off=0]
# --------------------
switch_ghg=1     # Greenhouse gas forcing on=1 off=0
switch_solar=1   # Solar forcing on=1 off=0
switch_volc=0    # Volcanic forcing on=1 off=0
switch_land=1    # Landuse forcing on=1 off=0
switch_aero=1    # Pollution particle forcing on=1 off=0


# --------------------
# Feedback parameters fo TwoBox model [Wm-2/K]
#
# NOTE: The parameters are not nessecarily independent 
#       for ex: water vapor and lapse rate feedbacks
#       are tightly connected 
#      (they tend to counteract each other)
# --------------------


# CMIP5 values
# Stefan Boltzmann's 'feedback' [Wm-2K-1]
lambda_planck=-3.1      # best guesses  [-3.3 to -3.1]

# Lapse rate feedback [Wm-2K-1]
lambda_lapse=-0.6      # best guesses [-1.2 to -0.5]

# water vapor feedback [Wm-2K-1]
lambda_water=1.7      # best guesses [1.5 to 2.2]

# Clouds feedback [Wm-2K-1]
lambda_cloud=0.50      # best guesses [0.1 to 1.2]

# Surface albedo feedback [Wm-2K-1]
lambda_albedo=0.40      # best guesses [0.1 to 0.4]

# Other feedbacks [Wm-2K-1]
lambda_other=0.0


# CMIP3 values
lambda_planck=-3.15   
lambda_lapse=-0.84      
lambda_water=1.8  
lambda_cloud=0.68
lambda_albedo=0.26


# NORESM-M 4*CO2 values
#lambda_planck=-3.11;   
#lambda_lapse=-0.48;      
#lambda_water=1.49;      
#lambda_cloud=0.58;      
#lambda_albedo=0.33;  


# --------------------
# Heat uptake efficency switches  [n=1 off=0]
# --------------------
switch_ocnheat=1     #  Deep Ocean heat uptake on=1 off=0
switch_stocastic=0#  #  Stocastic deep Ocean heat uptake on=1 off=0

# --------------------
# Deep ocean
# Heat uptake efficency [Wm-2K-1]
# --------------------
# CMIP5 4*CO2
#gamma=-0.61 # best guesses [-0.82 to -0.44] Kulbroth and Gregory, 2012
# CMIP3
gamma=-0.69  # best guesses [-1 to -0.5]
# NORESM-M 4*CO2
# gamma=-0.75;

if switch_ocnheat==1 and  switch_stocastic==1:
 gamma_std=0.2
else:
 gamma_std=0.0

# --------------
# ocean depths [m]
# --------------
# mixed layer thickness [m]
H_MIX= 100
# rest of the ocean [m]     
H_DEEP=3700-H_MIX    

# --------------
# Some constants
# -------------
#density of water (kg m-3)
RHO = 1000
#specific heat capacity of water (J kg-1 K-1)
CPO = 4200
       
# fraction of earth that is ocean
f_o=0.7