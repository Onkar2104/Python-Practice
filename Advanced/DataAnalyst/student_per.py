import pandas as pd
import matplotlib.pyplot as plt

def percentages(data):
    df = pd.DataFrame(data)

    df.set_index('Roll Number')
    df.plot(kind='bar')

    plt.xlabel('Roll Number')
    plt.ylabel('Percentage (%)')
    plt.title('Student Percentages')
    plt.show()

student_data = [
    {'Roll Number': '01', 'Year 1 Percentage': 85, 'Year 2 Percentage': 88, 'Year 3 Percentage': 90},
    {'Roll Number': '02', 'Year 1 Percentage': 78, 'Year 2 Percentage': 80, 'Year 3 Percentage': 82},
    {'Roll Number': '03', 'Year 1 Percentage': 92, 'Year 2 Percentage': 94, 'Year 3 Percentage': 96},
    {'Roll Number': '04', 'Year 1 Percentage': 69, 'Year 2 Percentage': 72, 'Year 3 Percentage': 75},
]

percentages(student_data)
