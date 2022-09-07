from prefect import task, flow, get_run_logger
from prefect.filesystems import GitHub


@task
def get_data():
    return [1, 2, 3, 4, 5, 6, 7]

@task
def print_data(data):
    get_run_logger().info(f"This is your data: {data}!")

@flow
def pipeline():
    data = get_data()
    print_data(data)

if __name__ == "__main__":
    g = GitHub(repository="https://github.com/PrefectHQ/prefect.git", reference="github-deployments")
    g.save("example")
    pipeline()