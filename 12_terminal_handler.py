def custom_terminal_state_handler(
    flow: Flow,
    state: State,
    reference_task_states: Set[State],
) -> Optional[State]:
    failed = False
    # iterate through reference task states looking for failures
    for task_state in reference_task_states:
        if task_state.is_failed():
            failed = True
    # update the terminal state of the Flow and return
    if failed:
        state.message = "Some important tasks have failed"
    return state

class FailingTask(Task):
    def run(self):
        raise Exception

flow = Flow(
    "my flow with custom terminal state handler",
    terminal_state_handler=custom_terminal_state_handler,
)
