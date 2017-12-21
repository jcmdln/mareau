import click

@click.command()
@click.option('--name', default='world', help='target to say hello to')

def hi(name):
    print('mareau: Hello, %s' % name)
