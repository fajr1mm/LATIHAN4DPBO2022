# LATIHAN4DPBO2022

Saya Fajri Maulana Iskandar mengerjakan LATIHAN4DPBO2022 dalam mata kuliah DPBO untuk keberkahanNya 
maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Design Class
![Desgin Class](https://user-images.githubusercontent.com/99385328/156907207-ecfcc9cb-927b-4c7e-85c1-2d8fc6081ab0.png)

### - Spesifikasi Code

Dalam Program Python ini terdapat 6 Class yaitu **Main**,**Vehicle** *sebagai parent class dari* **Ship** dan **Airplane** dengan konsep hierarchial inheritance, **Person**, dan **Job** *sebagai parent class dari* **Driver** dengan konsep multiple inheitance. Alasan saya menggunakan hierarchial inheritance pada class vehicle, karena pada dasarnya Ship dan Airplane merupakan sama - sama jenis alat transportasi yang artinya merupakan turunan child dari vehicle, sedangkan untuk multiple inheritance pada class person dan job, karena antara driver berhubungan dengan person menjadi parentnya, juga Job adalah parent dari driver yang mana itu adalah pekerjaan maka itu saya memakai konsep multiple inheritance.

Penggunaan atribut seperti name,fueltype,maxpass,type,age,manufactori dijadikan sebagai derived atribut karena pada class ship dan airplane juga mempunyai kesamaan atribut tersebut, yang membedakan hanyalah saya menambahkan masing masing pada child class 3 atribut sebagai pembeda spesifikasi dari class tersebut, lalu atribut pada class person dan job serta driver tidak mengalami derived atribut karena objek person dengan job kita ketahui tidak memiliki hubungan yang erat dalam spesifikasi atributnya sendiri, lalu saya menjadikan derived atribut antara class person dan driver.

### Running Program :
```
main.py
```

## Screenshot Hasil Compiler menggunakan Tools **Python.org** :

![image](https://user-images.githubusercontent.com/99385328/153930717-c7c5f121-03dd-4886-8c63-e9222f88ba75.png)
