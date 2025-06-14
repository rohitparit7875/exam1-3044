from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
    return "<h1>Rohit Madolappa Parit Aditya Residency Plot No 42, Bijapur Road, Solapur Phone: 7875209477 Email: rohitparit70@gmail.com
PROFESSIONAL SUMMARY
Recent B.Tech graduate in Computer Science and Engineering with strong proficiency in content management and knowledge management systems. Demonstrated ability to work in virtual environments and across diverse cultures, with a foundation in client management and relationship building. Excellent written and oral communication skills, along with effective teamwork abilities.
ACADEMIC QUALIFICATIONS
B.Tech in Computer Science and Engineering Sveri's College of Engineering CGPA: 9.03 March 2020 – June 2024
TECHNICAL SKILLS
Proficiency in: MS Office Suite (Word, Excel, PowerPoint)
Programming Languages: HTML, CSS, JavaScript, C#, Java (OOPs)
Databases: Microsoft SQL Server,Sql
Networking Basics: Understanding of network protocols and configurations
SOFT SKILLS
Strong client management and relationship-building abilities
Excellent written and verbal communication skills
Strong problem-solving skills and attention to detail
Team-oriented with a collaborative approach
Resume:
2
Projects
Blood Bank App (March 2024 – May 2024) Developed an Android application to streamline blood donation processes, including donor registration and inventory management. Collaborated with peers to enhance functionality and user experience.
Technologies Used: Java, Android Studio
Shop Management System (April 2023 – July 2023) Designed a SQL-based inventory management system, implementing effective reporting and management tools. Worked in a team to ensure a smooth integration of front-end and back-end technologies.
Technologies Used: Microsoft SQL Server, HTML, CSS, Bootstrap, JavaScript, ASP.NET MVC
PUBLICATIONS
Stock Price Prediction International Journal for Research in Applied Science & Engineering Technology
Stock market price prediction relies on machine learning models such as Linear Regression, LSTM, Random Forest, and K-Nearest Neighbors (KNN). Linear Regression captures linear relationships, making it useful for straightforward predictions. LSTM, a type of recurrent neural network, excels at modeling time-based dependencies, crucial for understanding trends. Random Forest, with its ensemble approach, offers robustness against overfitting and noise. KNN predicts based on the closest historical data points, useful for identifying patterns in smaller datasets
Internship 2024/01 – 2024/06 Hyderabad, India
(Full Stack Developer)
This Internship employs a technology stack comprising HTML, CSS, and JavaScript for front-end development, ensuring interactive and responsive web interfaces. C# is used along side ADO.NET for server-side programming, facilitating efficient data connectivity and manipulation with SQL Server databases. ASP.NET and .NET Core provide the framework for scalable and high-performance web applications
Technology Used : Web Development with HTML, CSS, JavaScript, C#, ADO.NET, ASP.NET, .NET Core, and SQL Server</h1>"


app.run(port=5000, host="0.0.0.0")
