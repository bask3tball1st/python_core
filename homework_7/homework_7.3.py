class Doctor:
    def treat(self):
        print("Доктор проводит лечение")

class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")

class Dentist(Doctor):
    def treat(self):
        print("Стоматолог лечит зубы")

class Therapist(Doctor):
    def treat(self):
        print("Терапевт делает первичный осмотр пациента")
    @staticmethod
    def doctor_prescription(code):
        if code == 1:
            Patient.doctor = Surgeon()
        elif code == 2:
            Patient.doctor = Dentist()
        else:
            Patient.doctor = Therapist()
        return Patient.doctor

class Patient:
    doctor = None
    def __init__(self, treatment_plan):
        self.__treatment_plan = treatment_plan
        self.doctor = Therapist.doctor_prescription(treatment_plan)

patient1 = Patient(1)
patient2 = Patient(2)
patient3 = Patient(3)
patient1.doctor.treat()
patient2.doctor.treat()
patient3.doctor.treat()