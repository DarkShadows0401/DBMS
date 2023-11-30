
import mysql.connector as con
conn = con.connect(host="127.0.0.1", username="root", password="Sayyam@123", database="mydata")
my_cursor = conn.cursor()
my_cursor.execute("Use mydata")
# my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
#                     self.Nameoftablets.get(),
#                     self.ref.get(),
#                     self.Dose.get(),
#                     self.NoofTablets.get(),
#                     self.Lot.get(),
#                     self.Issuedate.get(),
#                     self.Expdate.get(),
#                     self.DailyDose.get(),
#                     self.sideEffect.get(),
#                     self.FurtherInformation.get(),
#                     self.StorageAdvice.get(),
#                     self.DrivingUsingMachine.get(),
#                     self.HowtoUseMedications.get(),
#                     self.PatientId.get(),
#                     self.nhsNumber.get(),
#                     self.PatientName.get(),
#                     self.DateOfBirth.get(),
#                     self.PatientAddress.get(),
#                     self.BloodP.get(),
#                     ))
my_cursor.execute("show tables;")
print(my_cursor.fetchone())
conn.commit()
# conn.close()
# messagebox.showinfo("Success", "Data has been inserted")
