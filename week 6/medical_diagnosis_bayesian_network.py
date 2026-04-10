from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame(data={
    'Fever': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Cough': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'TestResult': ['Positive', 'Negative', 'Positive', 'Positive', 'Negative', 'Positive', 'Negative', 'Negative'],
    'Disease': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No']
})

model = DiscreteBayesianNetwork([
    ('Fever', 'Disease'),
    ('Cough', 'Disease'),
    ('TestResult', 'Disease')
])

model.fit(data)

print(model.get_cpds())

inference = VariableElimination(model)

query_result = inference.query(
    variables=['Disease'],
    evidence={
        'Fever': 'Yes',
        'TestResult': 'Positive'
    }
)

print(query_result)
