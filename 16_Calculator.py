from prefect.tasks.control_flow import switch, merge
from prefect import Parameter, Flow

# note: this will raise some warnings, but they're ok for this use case!
with Flow('Arithmetic') as flow:
    x, y = Parameter('x'), Parameter('y')
    operations = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }
    switch(condition=Parameter('op'), cases=operations)
    result = merge(*operations.values())

flow.visualize()


"""Test """
assert run(flow, x=1) == 2
assert run(flow, x=2) == 3
assert run(flow, x=-100) == -99
