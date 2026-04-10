from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame(data={
    'IncomeStability': ['High', 'Low', 'Medium', 'High', 'Low', 'Medium', 'High', 'Low'],
    'CreditHistory': ['Good', 'Poor', 'Good', 'Good', 'Poor', 'Poor', 'Good', 'Poor'],
    'EmploymentType': ['Salaried', 'SelfEmployed', 'Salaried', 'SelfEmployed',
                       'Salaried', 'SelfEmployed', 'Salaried', 'SelfEmployed'],
    'DefaultRisk': ['Low', 'High', 'Low', 'Low', 'High', 'High', 'Low', 'High']
})

model = DiscreteBayesianNetwork([
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk'),
    ('EmploymentType', 'DefaultRisk')
])

model.fit(data)

print(model.get_cpds())

inference = VariableElimination(model)

query_result = inference.query(
    variables=['DefaultRisk'],
    evidence={
        'IncomeStability': 'Low',
        'CreditHistory': 'Poor'
    }
)

print(query_result)
