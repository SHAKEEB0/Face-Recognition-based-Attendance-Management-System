Face-Recognition-Based-Attendance-System

A Project Report
submitted in partial fulfillment of the requirements
of 
AICTE Internship on AI: Transformative Learning 
with 
TechSaksham – A joint CSR initiative of Microsoft & SAP


by

Mohammed Shakeebuddin , mohammedshakeeb.ok@gmail.com

Under the Guidance of 
Aditya Prashant Ardak
Master Trainer, Edunet Foundation


 
ACKNOWLEDGEMENT

I would like to take this opportunity to express my heartfelt gratitude to all the individuals who have supported me throughout this project, both directly and indirectly.
First and foremost, I would like to thank my supervisor, Aditya Prashant Ardak, Master Trainer at Edunet Foundation, for being an exceptional mentor. His constant guidance, insightful advice, and constructive feedback have been invaluable throughout the development of this project. His encouragement and confidence in me have been a tremendous source of motivation, driving me to complete the project successfully. I consider myself fortunate to have had the chance to work with him over the past year. His support went beyond just the project work, as he also imparted lessons that have shaped me into a responsible and proactive professional.
I would also like to thank everyone who played a part in this journey. Without their support, this project would not have been possible.





ABSTRACT
The Face Recognition Attendance Management System is an AI-based solution aimed at automating the attendance process in educational institutions. This system leverages facial recognition technology to automatically detect and record student attendance, eliminating the need for manual entry and reducing the likelihood of errors and fraud. The system uses a webcam to capture student faces in real-time and matches them against a pre-trained dataset. In case of recognition failure, a manual attendance option is provided for the teacher or administrator to ensure accuracy. The system is integrated with a MySQL database for storing attendance records securely and allows for the generation of detailed attendance reports in CSV format. The user interface, developed with Tkinter, is simple and intuitive, enabling easy interaction with the system. This project aims to improve the efficiency, accuracy, and security of attendance management in educational settings, reducing administrative workload and enhancing data integrity. The system represents a significant step toward automating administrative tasks in educational institutions and demonstrates the potential of AI and machine learning in transforming traditional processes.














TABLE OF CONTENT
Chapter	Page
Abstract	I
Chapter 1: Introduction	1
1.1 Problem Statement	1
1.2 Motivation	1
1.3 Objectives	1
1.4 Scope of the Project	1
Chapter 2: Literature Survey	2
Chapter 3: Proposed Methodology	3
3.1 Features	3
3.2 Technologies Used	3
Chapter 4: Implementation and Results	4
4.1 Snapshots of Results	7
4.2 GitHub Link for Code	9
Chapter 5: Discussion and Conclusion	10
References	12








LIST OF FIGURES
Figure No.	Figure Caption	Page No.
Figure 1	Fig 1 main aap	5
Figure 2	Fig 2 manual attendance	5
Figure 3	Fig 3 manual attendance with subject	6






















LIST OF TABLES
Table. No.	Table Caption	Page No.
1	Table 3.1 : key features	3
2	Table 3.2 : Required programming languages, libraries, and databases	4

CHAPTER 1: INTRODUCTION
1.1 Problem Statement
The traditional methods of attendance management in educational institutions are time-consuming, prone to errors, and require significant manual effort. Students can often manipulate manual attendance by proxy or falsifying records. There is also a need for efficient data storage, analysis, and reporting, which becomes challenging in the case of manual systems. This project aims to automate the process of attendance marking using facial recognition, ensuring accuracy, time efficiency, and data security.
1.2 Motivation
The motivation for this project stems from the need to improve the efficiency and accuracy of the attendance management system. Traditional systems suffer from issues such as human errors, fraudulent attendance, and time delays. By integrating AI-driven face recognition technology, this project aims to address these challenges and offer a more reliable and automated solution. Additionally, the system's user-friendly interface and the option to generate reports make it an ideal tool for educators and administrators.
1.3 Objectives
The objectives of the Face Recognition Attendance Management System are as follows:
To automate attendance marking using facial recognition.
To allow manual attendance marking in case of face recognition failure.
To store attendance data in a secure MySQL database.
To provide the option to export reports in CSV format.
To create an intuitive graphical user interface (GUI) for system interaction.
1.4 Scope of the Project
The scope of this project is limited to automating attendance recording in educational institutions using facial recognition technology. The system is designed for classroom settings and small to medium-sized institutions. The system allows for real-time attendance recording, data storage, CSV export, and visual reports. It does not include features such as student performance tracking or integration with other institutional software systems. Additionally, the system assumes a controlled environment with stable lighting and clear student faces.








CHAPTER 2: LITERATURE SURVEY
2.1 Review of Relevant Literature
Various studies and projects have explored the use of biometrics in attendance systems. In the past, many systems relied on fingerprint scanning or RFID cards, but these methods have limitations such as errors in data capture and potential for misuse. Recent advancements in facial recognition technology, supported by libraries such as OpenCV and dlib, have made it feasible to develop robust attendance systems that rely on face detection algorithms for real-time identification.
2.2 Existing Models and Methodologies
Several models have been proposed for automated attendance marking. For instance, some systems use Bluetooth beacons or QR codes for attendance tracking. However, these systems often face challenges in terms of security and authentication. Facial recognition, on the other hand, offers a secure, touchless solution that addresses these issues effectively.
2.3 Gaps in Existing Solutions
Despite the promising use of facial recognition in attendance systems, most existing solutions face challenges like high computational requirements, incorrect identification due to lighting or angle issues, and high setup costs. This project aims to overcome such limitations by focusing on efficient and cost-effective implementation of facial recognition algorithms using open-source tools.











CHAPTER 3: PROPOSED METHODOLOGY
3.1 Features
The Face Recognition Attendance Management System includes several key features designed to streamline the process of attendance marking. The key features are:
Feature	Description
Face Recognition	Automatically recognizes students' faces in real-time and marks their attendance.
Image Capture	Captures and saves images for training the facial recognition model.
Manual Attendance	Provides an option for manual attendance entry. If face recognition fails, the admin/teacher can manually mark attendance for specific students.
CSV Export	Generates and exports attendance reports in CSV format. These reports can be used for administrative purposes, audits, or further data analysis.
Database Integration	Integrates with MySQL database to store student profiles, attendance records, and log details.
User Authentication	Ensures that only authorized users (teachers/admins) can access or modify attendance records.
Daily Reports	Automatically generates daily, weekly, or monthly reports of student attendance. Reports include names, dates, check-in times, and status (present/absent).
Graphical User Interface (GUI)	A user-friendly GUI built with Tkinter allows teachers and admins to interact with the system. Users can add students, check attendance, generate reports, and view live face recognition.

Table 3.1 : key features




3.2 Technologies Used
The Face Recognition Attendance Management System is built using a combination of programming languages, libraries, and databases. These tools work together to ensure seamless real-time recognition, report generation, and user interaction. The following table highlights the technologies used and their purpose.
Technology	Purpose
Python	Core programming language for logic, recognition, and database operations.
OpenCV	Detects and recognizes faces using Haar cascades and dlib-based models.
Tkinter	Builds the graphical user interface (GUI) for system interactivity.
NumPy	Supports numerical computations required for image processing and facial recognition.
Pandas	Reads, writes, and manipulates CSV files for attendance reports.
MySQL	Stores and manages student attendance records in a relational database.
Pillow (PIL)	Captures, resizes, and preprocesses images for training and face recognition.

Table 3.2 : Required programming languages, libraries, and databases





CHAPTER 4: IMPLEMENTATION AND RESULTS
4.1 Snapshots of Results

Fig 1: Main page

Fig:2

Fig:3
Below are some snapshots showcasing the output of the system. These snapshots demonstrate the face recognition process, GUI interface, and attendance report generation:
1.Snapshot 1: Image showing real-time face recognition in the system.
2.Snapshot 2: Screenshot of the user interface for adding a new student.
3.Snapshot 3: Example of the attendance report generated in CSV format.
4.2 GitHub Link for Code
The complete source code for the Face Recognition Attendance Management System can be accessed through the following GitHub link:https://github.com/SHAKEEB0/Face-Recognition-based-Attendance-Management-System.git








CHAPTER 5: DISCUSSION AND CONCLUSION
5.1 Future Work
While the system provides an efficient method for automating attendance, there are areas for improvement. Future enhancements could include:
Improved facial recognition accuracy by incorporating deep learning models.
Adding multi-device support to allow recognition from different cameras.
Implementing cloud storage for data backup and remote access.
Integrating AI-based performance tracking alongside attendance.
5.2 Conclusion
The Face Recognition Attendance Management System provides a reliable and efficient solution to automate the attendance marking process. By utilizing cutting-edge facial recognition technology and a user-friendly interface, the system addresses many of the issues inherent in traditional manual attendance systems. This project demonstrates the potential of AI and machine learning in transforming educational administrative tasks and highlights the importance of integrating these technologies for real-time, accurate attendance tracking.































REFERENCES
[1]. Ming-Hsuan Yang, David J. Kriegman, Narendra Ahuja, “Detecting Faces in Images: A Survey”, IEEE Transactions on Pattern Analysis and Machine Intelligence, Volume. 24, No. 1, 2002.
[2]. R. B. Rusu, M. M. Do, et al. “Face Recognition Using Deep Convolutional Neural Networks,” IEEE Transactions on Image Processing, 2021.
[3]. R. Szeliski, "Computer Vision: Algorithms and Applications," Springer, 2010.
