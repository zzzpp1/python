import csv
import json
student_csv=open('student.csv','r',encoding='utf-8')
student_json=open('student.json','w',encoding='utf-8')

column = ('name','age','gender','class','score')
value = csv.DictReader(student_csv, column)
for row in value:
    output=json.dumps([row],ensure_ascii=False)
    student_json.write(output)
    student_json.write('\n')
def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):
    pass


