import numpy
import pandas as pd

fichier = open("C:/Users/maell/OneDrive/Documents/Polytech 4A/Stage Polytechnique/Script/102_stop.txt")

df = pd.read_csv(fichier, skiprows=5, sep=r"\s+",
    dtype={
        "Stop_ID": int,
        "Early_St_Time (HHMM)": str,  # garde les zéros initiaux ex: "0400"
        "Late_St_Time (HHMM)": str,
        "Svice_Time(Sec)": int,
        "Load (Yards)": int        # 0 depot, 1 charge, 2 decharge
    },
)

C = 280.0 				# vehicle capacity (yards), real number
D = 400.0				# total yardage allowed for a vehicle per day, real number
S = 500				    # total number of regular stops for a vehicle allowed per day
pause = 3600			# lunch time duration in second, lunch time should start between 11:00am and 12:00 pm
V = 40				    # speed: MPH
