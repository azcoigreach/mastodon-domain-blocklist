import click

# click group with no command
@click.group()
def cli():
    '''List Builder CLI'''
    pass

# merge command
@cli.command()
@click.argument('list1', type=click.File('r'))
@click.argument('list2', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def merge(list1, list2, output):
    '''Merge two lists'''
    # compare two lists to remove duplicates and sort
    list1 = list(set(list1.read().splitlines()))
    list2 = list(set(list2.read().splitlines()))
    list1.extend(list2)
    list1 = list(set(list1))
    list1.sort()

    # output sorted list to file using click
    for item in list1:
        output.write(item + '\n')

# remove command
@cli.command()
@click.argument('list1', type=click.File('r'))
@click.argument('list2', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def remove(list1, list2, output):
    '''Remove items from list1 that are in list2'''
    # remove list2 from list1
    list1 = list(set(list1.read().splitlines()))
    list2 = list(set(list2.read().splitlines()))
    list1 = [item for item in list1 if item not in list2]

    # output sorted list to file using click
    for item in list1:
        output.write(item + '\n')

