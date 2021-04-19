import pytest
import pandas as pd
import datatest as dt

d = {
'cars' : ['BMW','Toyato','Audi'],
'year' : [2000,2001,2002],
}

myvar = pd.DataFrame(d)

def test_columns():
    dt.validate(
        myvar.columns,
        {'cars', 'year'}
    )
