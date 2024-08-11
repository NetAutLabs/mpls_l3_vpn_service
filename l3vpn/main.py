from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_rich.progress_bar import RichProgressBar
from nornir_rich.functions import print_result


def apply_service_declaration(task: Task) -> Result:

    # TODO: Implement this task to provision the services defined in "services.yaml"
    # and deprovision any unnecessary services currently deployed on the devices.
    # Note: Ensure device management access.
    # Hint: Use subtasks to keep the code organized.

    return Result(host=task.host, result="TODO:", failed=True)


def main(dry_run: bool = True):
    nr = InitNornir(config_file="config.yaml", dry_run=dry_run)

    nr_with_processors = nr.with_processors([RichProgressBar()])
    result = nr_with_processors.run(task=apply_service_declaration)

    print_result(
        result,
        vars=["result", "failed", "diff", "changed"],
    )
