# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ### Active Tables
# Allow students to input values into a table, each of which is graded.

# <codecell>

import pandas as pd

# <codecell>

Numeric = 'NUMERIC_RESPONSE'

questionTable = [
        ['Last name','First name','Age'],
        ['Obama','Barack',Numeric],
        ['Bush','George',Numeric],
        ['Clinton','William',Numeric],
    ]

header = questionTable.pop(0)
#print pd.DataFrame(data=answerTable,columns=header).to_html(index=False)

answerTable = [
        ['Last name','First name','Age'],
        ['Obama','Barack',53],
        ['Bush','George',68],
        ['Clinton','William',68],
    ]

table =  pd.DataFrame(data=questionTable,columns=header).to_html(index=False)
print table.replace('NUMERIC_RESPONSE','<input size="10px"></input>')

# <codecell>

%%HTML
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Last name</th>
      <th>First name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>   Obama</td>
      <td>  Barack</td>
      <td> <input size="10px"></input></td>
    </tr>
    <tr>
      <td>    Bush</td>
      <td>  George</td>
      <td> <input size="10px"></input></td>
    </tr>
    <tr>
      <td> Clinton</td>
      <td> William</td>
      <td> <input size="10px"></input></td>
    </tr>
  </tbody>
</table>

# <codecell>


