from driver import driver

o_driver = [driver("Galang", "7371239219", "Perempuan", "Kuli", "268149", "PT. Jawa Membangun Negeri", "Striker", "12235", "22 November 2016", "Motor"),
driver("Ucup", "63932543054", "Laki - laki", "Manusia Silver", "7813", "PT. Silver Man", "Leadarship", "3580879", "30 Februari 2002", "Mobil")]

print("----------------------D R I V E R--------------------")
for i in range(2):
    print(o_driver[i].printDriver())

