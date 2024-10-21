import numpy as np

MODIFIED_EMISSIONS = False
FORCING = False

n_boxes = 9

# Define initial carbon masses (Gt) of boxes in an array (size n_boxes)
"""
M1 = 725  # Atmosphere
M2 = 725  # Surface Ocean
M5 = 110  # Short-lived biota
M7 = 60  # Deep Ocean
"""
Mi0_onebox = np.array([725,0,0,0,0,0,0,0,0])

Mi0_fourboxes = np.array([725,725,0,0,110,0,60,0,0])
Mi0_perturbed_fourboxes = np.array([1000,725,0,0,110,0,60,0,0])

Mi0_nineboxes = np.array([725,725,3,37675,110,450,60,1350,160])
Mi0_perturbed = np.array([1000,725,3,37675,110,450,60,1350,160])

# Define initial fluxes (Gt/year) in a matrix (dimensions n_boxes x n_boxes)
"""
F_12 = 90  # Flux from Atmosphere to Surface Ocean
F_21 = 90  # Flux from Surface Ocean to Atmosphere
F_71 = 55  # Flux from Deep Ocean to Atmosphere
F_57 = 55  # Flux from Short-lived Biota to Deep Ocean
F_15 = 110  # Flux from Atmosphere to Short-lived Biota
F_51 = 55  # Flux from Short-lived Biota to Atmosphere
F_72 = 0  # Flux from Deep Ocean to Surface Ocean
"""
Fi0_onebox = np.zeros((n_boxes, n_boxes))
Fi0_onebox[0,1] = 90

Fi0_fourboxes = np.zeros((n_boxes, n_boxes))

Fi0_fourboxes[0,1] = 90
Fi0_fourboxes[1,0] = 90
Fi0_fourboxes[6,0] = 55
Fi0_fourboxes[4,6] = 55
Fi0_fourboxes[0,4] = 110
Fi0_fourboxes[4,0] = 55
Fi0_fourboxes[6,1] = 0



# Define initial fluxes (Gt/year)
F_12 = 89  # Flux from Atmosphere to Surface Ocean
F_21 = 90  # Flux from Surface Ocean to Atmosphere
F_71 = 50  # Flux from Deep Ocean to Atmosphere
F_15 = 110  # Flux from Atmosphere to Short-lived Biota
F_51 = 55  # Flux from Short-lived Biota to Atmosphere
F_72 = 1  # Flux from Deep Ocean to Surface Ocean
F_23 = 40
F_24 = 38
F_32 = 36
F_34 = 4
F_42 = 42
F_56 = 15
F_57 = 40
F_67 = 15
F_78 = 3
F_79 = 1
F_81 = 3
F_91 = 1

# Define initial flux matrix (n x n)
Fi0_nineboxes = np.zeros((n_boxes, n_boxes))
Fi0_nineboxes[0,1] = F_12
Fi0_nineboxes[1,0] = F_21
Fi0_nineboxes[6,0] = F_71
Fi0_nineboxes[4,6] = F_57
Fi0_nineboxes[0,4] = F_15
Fi0_nineboxes[4,0] = F_51
Fi0_nineboxes[6,1] = F_72

Fi0_nineboxes[0,1] = F_12 
Fi0_nineboxes[1,0] = F_21   
Fi0_nineboxes[6,0] = F_71   
Fi0_nineboxes[0,4] = F_15  
Fi0_nineboxes[4,0] = F_51   
Fi0_nineboxes[6,1] = F_72  
Fi0_nineboxes[1,2] = F_23 
Fi0_nineboxes[1,3] = F_24 
Fi0_nineboxes[2,1] = F_32 
Fi0_nineboxes[2,3] = F_34 
Fi0_nineboxes[3,1] = F_42 
Fi0_nineboxes[4,5] = F_56 
Fi0_nineboxes[4,6] = F_57 
Fi0_nineboxes[5,6] = F_67 
Fi0_nineboxes[6,7] = F_78 
Fi0_nineboxes[6,8] = F_79 
Fi0_nineboxes[7,0] = F_81 
Fi0_nineboxes[8,0] = F_91 

# array I use for making a legend (maybe this should be in main.ipynb..........)
ninebox_legend_arr = ['(1) Atmosphere', '(2) Surface water ', '(3) Surface biota ',
                      '(4) Intermediate and Deep water ', '(5) Short-lived biota ', '(6) Long-lived biota ',
                      '(7) Litter ', '(8) Soil ', '(9) Peat ']