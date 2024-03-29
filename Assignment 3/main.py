# Patient Organization System
# Developed by Arya Murray for Comp Sci 1026 Assignment 3
# Version 1.0

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
    # testing for invalid input (inappropreate filename)
    try:
        if os.path.isfile(fileName) == False:
            raise ValueError(
                "The file {} could not be found" .format(fileName))
    except ValueError as err:
        print("Error: {}" .format(err))
        exit()
    #initialize some variables we require
    textline = 0
    patients = {}
    #open the text document and read the data
    with open(fileName, "r") as contents:
        lines = contents.readlines()
        for line in lines:  # For loop to read each line
            textline += 1  # textline keeps track of which line in the original document that the current line iteration is on
            line = line.replace("\n", "")
            key, *values = line.split(",")
            if len(values) != 7: #checks for inappropriate number of fields in line
                print("Invalid number of fields ({}) in line: [{}]" .format(1 + len(values), textline))
                continue
            else:
                try:
                    key = int(key) #enures that the first value of each line is an integer
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try:
                    values[1] = float(values[1]) #ensures that the temperature is a float
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try:
                    for index in values[2:]: # ensures that the rest of the values are integers
                        values[values.index(index)] = int(index)
                except ValueError:
                    print("Invalid data type in line: [{}]" .format(textline))
                    continue
                try: # All of these statements ensure that the values are in an acceptable range, if they are not. They are discarded and not appended.
                    if not 35 <= values[1] <= 42:
                        raise ValueError("Invalid temperature value ({}) in line: {}" .format(values[1], line))
                    if not 30 <= values[2] <= 180:
                        raise ValueError("Invalid heart rate value ({}) in line: {}" .format(values[2], line))
                    if not 5 <= values[3] <= 40:
                        raise ValueError("Invalid respiratory rate value ({}) in line: {}" .format(values[3], line))
                    if not 70 <= values[4] <= 200:
                        raise ValueError("Invalid systolic blood pressure value ({}) in line: {}" .format(values[4], line))
                    if not 40 <= values[5] <= 120:
                        raise ValueError("Invalid diastolic blood pressure value ({}) in line: {}" .format(values[5], line))
                    if not 70 <= values[6] <= 100:
                        raise ValueError("Invalid oxygen saturation value ({}) in line: {}" .format(values[6], line))
                except ValueError as err:
                    print(err)
                    continue
                patients.setdefault(key, []).append(values) # If no errors have been raised, then the data is appended to patients
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
    # In the case that 0 is the input, it scans all the patients
    if patientId == 0 or patientId == "0":
        for key in patients.keys():
            print("\n\nPatient ID: {}" .format(key))
            for sublist in patients[key]:
                print(" Visit Date: {}" .format(sublist[0]))
                print("  Temperature: {} C" .format(sublist[1]))
                print("  Heart Rate: {} bpm" .format(sublist[2]))
                print("  Respitory Rate: {} bpm" .format(sublist[3]))
                print("  Systolic Blood Pressure: {} mmHg" .format(sublist[4]))
                print("  Diastolic Blood Pressure: {} mmHg" .format(sublist[5]))
                print("  Oxygne Saturation: {} %" .format(sublist[6]) )
    # Given a single patient id, it prints their information
    elif patientId in patients:
        for sublist in patients[patientId]:
            print("Visit Date: {}" .format(sublist[0]))
            print(" Temperature: {} C" .format(sublist[1]))
            print("  Heart Rate: {} bpm" .format(sublist[2]))
            print("  Respitory Rate: {} bpm" .format(sublist[3]))
            print("  Systolic Blood Pressure: {} mmHg" .format(sublist[4]))
            print("  Diastolic Blood Pressure: {} mmHg" .format(sublist[5]))
            print("  Oxygen Saturation: {} %%" .format(sublist[6]))
    #if the id is not found, prints error
    else:
        print("Patient with ID {} not found." .format(patientId))


def displayStats(patients, patientId = 0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    # Some error testing at the beginning to ensure valid types
    try:
        patientId = int(patientId)
    except ValueError:
        print("Error: 'patiendId' should be an integer.")
        return
    if type(patients) != dict:
        print("Error: 'patients' should be a dictionary.'")
        return
    #instantiate the lists for averages
    avgtemp = []
    avgheartrate = []
    avgresprate = []
    avgsysbp = []
    avgdiabp = []
    avgoxy = []
    # In the case that 0 is the input, it scans all the patients and prints the average vitals for all patients
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
    #Given a single patient id, it scans all the patients and prints the average vitals for all patients
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
    #If incorrect integer input, prints error
    else:
        print("No data found for patient with ID %i." % int(patientId))


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
    #checks for valid date input
    splitdate = date.split("-")
    if len(splitdate[0]) != 4 or not 1 <= int(splitdate[1]) <= 12 or not 1 <= int(splitdate[2]) <= 31 or not int(splitdate[0]) >= 1900 or len(splitdate) > 3:
        print("Invalid Date. Please enter a valid date.")
        return
    # All of these statements ensure that the values are in an acceptable range, if they are not, returns error. Quits.
    try:
        if not 35 <= int(temp) <= 42:
            raise ValueError("Invalid temperature. Please enter a temperature between 35 and 42 C")
        if not 30 <= int(hr) <= 180:
            raise ValueError("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        if not 5 <= int(rr) <= 40:
            raise ValueError("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        if not 70 <= int(sbp) <= 200:
            raise ValueError("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200.")
        if not 40 <= int(dbp) <= 120:
            raise ValueError("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120.")
        if not 70 <= spo2 <= 100:
            raise ValueError("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100.")
    except ValueError:
        print(ValueError)
        return
    #opens the patients file and inserts the new data.
    with open(fileName, "a") as file:
        insert = f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}"
        file.write(insert)
    # Updates the patients Dictionary with the new data. If key exists, appends the new list to the old list
    if patientId in patients.keys():
        oldpatients = patients[patientId]
        oldpatients.append([date, temp, hr, rr, sbp, dbp, spo2])
        patients[patientId] = oldpatients
    # If key doesn't exist, just makes new entry and updates it
    else:
        patients.update({patientId: [patientId, date, temp, hr, rr, sbp, dbp, spo2]})
    print("Visit is saved successfully for patient #{}" .format(patientId))


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    # ensures that month is a valid value
    visits = []
    if month != None:
        if not 1 <= month <= 12:
            return visits
    #checks for the given values within the patient dictionary
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
    # Literally just checks for invalid values that are in the patients dict for abnormal values as specified in the outline
    for patient in patients.keys():
        for visit in patients[patient]:
            if not 60 < visit[2] < 100 or visit[4] > 140 or visit[5] > 90 or visit[6] < 90:
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
    # if the patient id does not exist, returns error
    if patientId not in patients.keys():
        print("No data found for patient with ID {}".format(patientId))
        return
    # removes the patientid entry from the dictionary
    patients.pop(patientId)
    #whole section underneath copies contents from textfile and rewrites the whole document without the specified patientid
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
