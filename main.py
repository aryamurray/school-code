import os


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """

    try:
        if os.path.isfile(fileName) == False:
            raise ValueError(
                "The file {} could not be found" .format(fileName))
    except ValueError as err:
        print("Error: {}" .format(err))
        exit()

    textline = 0
    patients = {}
    with open(fileName, "r") as contents:
        lines = contents.readlines()
        for line in lines:
            textline += 1
            line = line.replace("\n", "")
            key, *values = line.split(",")
            if len(values) != 7:
                print("Invalid number of fields ({}) in line: [{}]" .format(
                    1 + len(values), textline))
                continue
            else:
                try:
                    key = int(key)
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try:
                    values[1] = float(values[1])
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try:
                    for index in values[2:]:
                        values[values.index(index)] = int(index)
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try:
                    if not 30 <= values[1] <= 43:
                        raise ValueError(
                            "Invalid temperature value ({}) in line: [{}]" .format(values[1], textline))
                    if not 30 <= values[2] <= 200:
                        raise ValueError(
                            "Invalid heart rate value ({}) in line: [{}]" .format(values[2], textline))
                    if not 5 <= values[3] <= 60:
                        raise ValueError("Invalid respiratory rate value ({}) in line: [{}]" .format(
                            values[3], textline))
                    if not 50 <= values[4] <= 250:
                        raise ValueError("Invalid systolic blood pressure value ({}) in line: [{}]" .format(
                            values[4], textline))
                    if not 30 <= values[5] <= 150:
                        raise ValueError("Invalid diastolic blood pressure value ({}) in line: [{}]" .format(
                            values[5], textline))
                    if not 80 <= values[6] <= 100:
                        raise ValueError("Invalid oxygen saturation value ({}) in line: [{}]" .format(
                            values[6], textline))
                except ValueError as err:
                    print(err)
                    continue
                patients.setdefault(key, []).append(values)
    contents.close()
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    """Heart Rate: {heart rate value} bpm
    Respiratory Rate: {respiratory rate value} bpm
    Systolic Blood Pressure: {systolic blood pressure value} mmHg
    Diastolic Blood Pressure: {diastolic blood pressure value} mmHg
    Oxygen Saturation: {oxygen saturation value} %
    """
    if patientId == 0 or patientId == "0":
        for key in patients.keys():
            print("\n\nPatient ID: {}" .format(key))
            for sublist in patients[key]:
                print("Visit Date: {}" .format(sublist[0]))
                print("    Temperature: {} C" .format(sublist[1]))
                print("    Heart Rate: {} bpm" .format(sublist[2]))
                print("    Respitory Rate: {} bpm" .format(sublist[3]))
                print(
                    "    Systolic Blood Pressure: {} mmHg" .format(sublist[4]))
                print(
                    "    Diastolic Blood Pressure: {} mmHg" .format(sublist[5]))
                print("    Oxygen Saturation: {} %%" .format(sublist[6]))
    elif patientId in patients:
        for sublist in patients[patientId]:
            print("Visit Date: {}" .format(sublist[0]))
            print(" Temperature: {} C" .format(sublist[1]))
            print("  Heart Rate: {} bpm" .format(sublist[2]))
            print("  Respitory Rate: {} bpm" .format(sublist[3]))
            print("  Systolic Blood Pressure: {} mmHg" .format(sublist[4]))
            print("  Diastolic Blood Pressure: {} mmHg" .format(sublist[5]))
            print("  Oxygen Saturation: {} %%" .format(sublist[6]))
    else:
        print("Patient with ID {} not found." .format(patientId))


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        patientId = int(patientId)
    except ValueError:
        print("Error: 'patiendId should be an integer.")
        return
    if type(patients) != dict:
        print("Error: 'patients should be a dictionary.'")
        return
    avgtemp = []
    avgheartrate = []
    avgresprate = []
    avgsysbp = []
    avgdiabp = []
    avgoxy = []
    if patientId == 0 or patientId == "0":
        for key in patients.keys():
            for sublist in patients[key]:
                avgtemp.append(float(sublist[1]))
                avgheartrate.append(float(sublist[2]))
                avgresprate.append(float(sublist[3]))
                avgsysbp.append(float(sublist[4]))
                avgdiabp.append(float(sublist[5]))
                avgoxy.append(float(sublist[6]))
        avgtemp = sum(avgtemp) / len(avgtemp)
        avgheartrate = sum(avgheartrate) / len(avgheartrate)
        avgresprate = sum(avgresprate) / len(avgresprate)
        avgsysbp = sum(avgsysbp) / len(avgsysbp)
        avgdiabp = sum(avgdiabp) / len(avgdiabp)
        avgoxy = sum(avgoxy) / len(avgoxy)
        print("Vital Signs for All Patients:")
        print(" Average Temperature: %.2f C" % (avgtemp))
        print(" Average Heart Rate: %.2f bpm" % (avgheartrate))
        print(" Average Respiratory Rate: %.2f bpm" % (avgresprate))
        print(" Average Systolic Blood Presure: %.2f mmHg" % (avgsysbp))
        print(" Average Diastolic Blood Pressure: %.2f mmHg" % (avgdiabp))
        print(" Average Oxygen Saturation: %.2f %%" % (avgoxy))
    elif patientId in patients.keys():
        for sublist in patients[patientId]:
            avgtemp.append(float(sublist[1]))
            avgheartrate.append(float(sublist[2]))
            avgresprate.append(float(sublist[3]))
            avgsysbp.append(float(sublist[4]))
            avgdiabp.append(float(sublist[5]))
            avgoxy.append(float(sublist[6]))
        avgtemp = sum(avgtemp) / len(avgtemp)
        avgheartrate = sum(avgheartrate) / len(avgheartrate)
        avgresprate = sum(avgresprate) / len(avgresprate)
        avgsysbp = sum(avgsysbp) / len(avgsysbp)
        avgdiabp = sum(avgdiabp) / len(avgdiabp)
        avgoxy = sum(avgoxy) / len(avgoxy)
        print("Vital Signs for Patient %i:" % (int(patientId)))
        print(" Average Temperature: %.2f C" % (avgtemp))
        print(" Average Heart Rate: %.2f bpm" % (avgheartrate))
        print(" Average Respiratory Rate: %.2f bpm" % (avgresprate))
        print(" Average Systolic Blood Presure: %.2f mmHg" % (avgsysbp))
        print(" Average Diastolic Blood Pressure: %.2f mmHg" % (avgdiabp))
        print(" Average Oxygen Saturation: %.2f %%" % (avgoxy))
    else:
        print("No data found for patient with ID %i" % int(patientId))


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    splitdate = date.split("-")
    if len(splitdate[0]) != 4 or not 1 <= int(splitdate[1]) <= 12 or len(splitdate[1]) != 2 or not 1 <= int(splitdate[2]) <= 31 or len(splitdate[2]) != 2 or len(splitdate) > 3:
        print("Invalid Date. Please enter a valid date.")
        return
    try:
        if not 30 <= int(temp) <= 43:
            raise ValueError(
                "Invalid temperature. Please enter a temperature between 30 and 43 C")
        if not 30 <= int(hr) <= 200:
            raise ValueError(
                "Invalid heart rate. Please enter a heart rate between 30 and 200 bpm.")
        if not 5 <= int(rr) <= 60:
            raise ValueError(
                "Invalid respiratory rate. Please enter a respiratory rate between 5 and 60 bpm.")
        if not 50 <= int(sbp) <= 250:
            raise ValueError(
                "Invalid systolic blood pressure. Please enter a systolic blood pressure between 50 and 250.")
        if not 30 <= int(dbp) <= 150:
            raise ValueError(
                "Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 30 and 150.")
        if not 80 <= spo2 <= 100:
            raise ValueError(
                "Invalid oxygen saturation. Please enter an oxygen saturation between 80 and 100.")
    except ValueError:
        print(ValueError)

    with open(fileName, "a") as file:
        insert = f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}"
        file.write(insert)
    if patientId in patients.keys():
        oldpatients = patients[patientId]
        oldpatients.append([patientId, date, temp, hr, rr, sbp, dbp, spo2])
        patients[patientId] = oldpatients
    else:
        patients.update(
            {patientId: [patientId, date, temp, hr, rr, sbp, dbp, spo2]})
    print("Visit is saved successfully for patient #{}" .format(patientId))


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    if month != None:
        if not 1 <= month <= 12:
            return visits

    for patient in patients.keys():
        for visit in patients[patient]:
            dictdate = visit[0].split("-")
            dictyear = int(dictdate[0])
            dictmonth = int(dictdate[1])

            if year == None:
                visits.append((patient, visit))

            elif month == None:
                if year == dictyear:
                    visits.append((patient, visit))

            elif year == dictyear and month == dictmonth:
                visits.append((patient, visit))
            else:
                continue
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []

    for patient in patients.keys():
        for visit in patients[patient]:
            if not 60 < visit[2] < 100 or visit[4] > 140 or visit[5] >90 or visit[6] <90:
                if patient not in followup_patients:
                    followup_patients.append(int(patient))

    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    if patientId not in patients.keys():
        print("No data found for patient with ID {}".format(patientId))
        return
    
    patients.pop(patientId)

    with open(filename, "r") as contents:
        lines = contents.readlines()

    with open(filename, "w") as contents:
        contents.truncate()
        for line in lines:
            strippedline = line.replace("\n", "")
            indexline = strippedline.split(",")
            if not int(indexline[0]) == patientId:
                contents.write(line)
    print("Data for patient {} has been deleted" .format(patientId))


###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp,
                               hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
