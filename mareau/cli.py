import click
from mareau.cmd import (hi)

CONTEXT = {
    'help_option_names': ['-h', '--help']
}

UNKNOWN_OPTIONS = {
    'ignore_unknown_options': True,
    **CONTEXT
}

class Command(click.Group):
    def command(self, context, name):
        if name == 'use':
            return shell
        return click.Group.command(self, context, name)

@click.group(cls=Command, context_settings=CONTEXT)
@click.version_option()

def mareau():
    pass

mareau.add_command(hi)
