from flask import Flask, request, render_template,url_for
from matplotlib import pyplot as plt

with open ('data.csv') as file:
        file_data = file.readlines()[1:]

def image_creator(marklist):
    plt.hist(marklist, bins = 10)
    plt.savefig('static/image.png')


app = Flask(__name__)
@app.route('/', methods = ["GET", "POST"])

def home ():
    if request.method == "GET":
        return render_template('index.html')
    else:
        data = request.form
        if data['ID'] == 'student_id':
            _sid = data['id_value']
            student_details = []
            total_marks = 0

            for row in file_data:
                sid,cid,marks = row.strip().split(', ')
                marks = int(marks)
                if sid == _sid:
                    entry = {'sid': sid, 'cid': cid, 'marks': marks}
                    total_marks += marks
                    student_details.append(entry)
            
            if student_details:
                return render_template('student_details.html', data = student_details, total = total_marks)
            else:
                return render_template('error.html')
        else:
            _cid = data['id_value']
            marklist = []
            total_marks = 0
            avg = 0
            maxi = 0

            for row in file_data:
                sid,cid,marks = row.strip().split(', ')
                marks = int(marks)
                if cid == _cid:
                    marklist.append(marks)
            if marklist:
                maxi = max(marklist)
                total_marks = sum(marklist)
                avg = total_marks/len(marklist)
                image_creator(marklist=marklist)
                return render_template('course_details.html', avg=avg, maxi=maxi)
            else: 
                return render_template('error.html')
            return marklist
    
if __name__ == "__main__":
    app.run(debug=True)