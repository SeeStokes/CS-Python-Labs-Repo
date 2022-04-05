#====================================================================================================================================================
#  Program Name: Ocean Levels                      Author(s): Sierra Stokes                                                                         |
#  Date Created: 9/20/2021                     Program Location: Desktop                                                                            |
#  Created in partial fulfillment of the coursework for COSC 1336-014 at Austin Community College                                                   |
#---------------------------------------------------------------------------------------------------------------------------------------------------|
#  Copyright (c) 2021 By Sierra E. Stokes                                                                                                           |
#---------------------------------------------------------------------------------------------------------------------------------------------------|
#  Purpose of Program: Display the number of millimeters that the ocean will 
#  have risen each year for the next 25 years.                                                                                                      |
#====================================================================================================================================================
# Data Dictionary                                                                                                                                   |
#  Name                       Type              Range               Use                                                                             |
#  ------                     -----             ----------          -----------------------------------------                                       |
#  sea_level_rise_year        integer           any integer         variable to represent the year value in the range  
#  sea_level_rise             float             any float value     variable to represent the number of millimeters of sea level rise               |
#====================================================================================================================================================
#  Functions used: None                                                                                                                             |
#====================================================================================================================================================

#MAIN Code Begins Here ?????????????????????????????????????????????????????                                                                        |

# This program displays the number of millimeters that the ocean 
# will have risen each year for the next 25 years

# Displays two column headers "Years" and "Rise (in millimeters)"
print ('Years\t\t Rise (in millimeters)')

# Count controlled for-loop calculates the number of millimeters that the ocean rises 
# each year for the next 25 years
# Displays results in two columns for the user
for sea_level_rise_year in range(1, 26):
    sea_level_rise = 1.8 * sea_level_rise_year
    print(sea_level_rise_year,'\t\t' , format(sea_level_rise, '2.2f'))


   

