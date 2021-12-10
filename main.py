import click

@click.group()
def cli():
    pass

@click.command()
def createDB():
    print("created Database")

@click.command()
def deleteDB():
    print("deleted Database")


@click.command()
@click.option('--count', default=1, help='number of messages')
@click.argument('name')
def hello(count, name):
    for message in range(count):
        print(f"Hello {name}!")


cli.add_command(createDB)
cli.add_command(deleteDB)
cli.add_command(hello)


if __name__ == '__main__':
    cli()

