from django.db import models

class PrimaryTechnologyAreas(models.Model):
    TA_1 = 'LPS'
    TA_2 = 'ISPT'
    TA_3 = 'SPES'
    TA_4 = 'RAS'
    TA_5 = 'CNODTCS'
    TA_6 = 'HHLSHS'
    TA_7 = 'HEDS'
    TA_8 = 'SIOSS'
    TA_9 = 'EDLS'
    TA_10 = 'N'
    TA_11 = 'MSITP'
    TA_12 = 'MSMSM'
    TA_13 = 'GLS'
    TA_14 = 'TMS'
    TA_15 = 'A'
    PRIMARY_TECH_AREA_CHOCIES = (
        (TA_1, 'Launch Propulsion Systems'),
        (TA_2, 'In-Space Propulsion Technologies'),
        (TA_3, 'Space Power and Energy Storage'),
        (TA_4, 'Robotics and Autonomous Systems'),
        (TA_5, 'Communications, Navigation, and Orbital Debris Tracking and Characterization Systems'),
        (TA_6, 'Human Health, Life Support, and Habitation Systems'),
        (TA_7, 'Human Exploration Destination Systems'),
        (TA_8, 'Science Instruments, Observatories, and Sensor Systems'),
        (TA_9, 'Entry, Descent, and Landing Systems'),
        (TA_10, 'Nanotechnology'),
        (TA_11, 'Modeling, Simulation, Information Technology and Processing'),
        (TA_12, 'Materials, Structures, Mechanical Systems and Manufacturing'),
        (TA_13, 'Ground and Launch Systems'),
        (TA_14, 'Thermal Management Systems'),
        (TA_15, 'Aeronautics')
    )
