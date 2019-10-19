# First iteration based only on the lowest of min temperature and returning a string
def gear_recommendation(weather_forecast):
    min_temperature = min(weather_forecast['morning']['min_temperature'],
                          weather_forecast['afternoon']['min_temperature'])

    if min_temperature < 5:
        return "Wear jacket with underskin, thick globes, long bib and thermal socks. " \
               "Cover for head and neck."
    elif min_temperature < 10:
        return "Wear jacket, thick globes and long bib. Cover for head and neck."
    elif min_temperature < 15:
        return "Wear long mallot or mallot with arm warmers, long globes and long bib " \
               "or short with leg warmers. Cover for neck."
    elif min_temperature < 20:
        return "Wear mallot (carry arm warmers in case), fingerless globes and short bib."
    else:
        return "Wear thin mallot, fingerless globes and short bib."
