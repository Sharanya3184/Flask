from flask import Flask

api = Flask(__name__)

@api.route('/')
def hello():
    return( """<html>
<head>
    <style>
        body {
            background: black;
            color: white;
            
        }
        h1 {
            color: lightgreen;
            font-family: Times New Roman;
            font-size: 50px;
            font-weight: bold;
        }
        .content {
            color: white;;
            padding: 20px;
            border-radius: 10px;
            font-family: Times New Roman;
            font-size: 20px;
           align:absolute;
        }
       
            }
        }
    </style>
</head>
<body>
    <center><h1>SELF-INTRO</h1></center>
    <div class="content">
        <p>Hi, good afternoon. I am Sharanya R from Vellore.</p> 
        <p>I am currently pursuing my Bachelor of Computer Applications at Auxilium College (Autonomous), Katpadi.</p>

        <p>I completed both my SSLC and HSC at Shanthinikethan Matric Higher Secondary School, Vellore.</p>

        <p>I have completed an internship at Aura Harks Technology Pvt. Ltd. as a Software Developer Trainee, where I gained hands-on experience in form validation, responsive design for mobile view, and backend development.</p>

        <p>During this time, I worked on two real-time projects: a Clinic Booking System and a Personalized Mentor Platform. 
        I was involved in both frontend and backend development.</p>

        <p>Additionally, I performed manual testing to ensure functionality and reliability.</p>
        <p>My core skill is Python, and I’m continuously learning and improving in this domain.</p><br>

           
        <center><p>***Thank you for giving me this opportunity to introduce myself.***</p><center>
    </div>
</body>
</html>""")

if __name__ == '__main__':
    api.run(debug=True,
    host='0.0.0.0',
    port=3010)


