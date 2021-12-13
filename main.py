import click
import re
import datetime
import collections
import argparse
import os


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
#@click.option('--print', 'p', 'print_' help='The printfile function allows you to see a file. You can try with Expenses, Income or Bitcoin')
 
@click.argument('file')
def printFile(file):
    f= open('{}.ledger'.format(file), 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()


@click.command()
@click.option('--count', default=1, help='number of messages')
@click.argument('name')
def hello(count, name):
    for message in range(count):
        print(f"Hello {name}!")


cli.add_command(createDB)
cli.add_command(deleteDB)
cli.add_command(printFile)
cli.add_command(hello)


if __name__ == '__main__':
    cli()
