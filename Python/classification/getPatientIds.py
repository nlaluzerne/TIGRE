

def getPatients(patients_path):
    patlist = open(patients_path, "r").readlines()
    patlist = [pat.strip().encode('utf-8').replace('\r','') for pat in patlist]
    return patlist
