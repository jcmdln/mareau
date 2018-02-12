import click
from markan.cmd import (reddit, sheets, wordpress)


CONTEXT = {'help_option_names': ['-h', '--help']}
UNKNOWN_OPTIONS = {'ignore_unknown_options': True}

class Command(click.Group):
    def command(self, context, name):
        if name == 'use':
            return shell
        return click.Group.command(self, context, name)

@click.group(cls = Command, context_settings = CONTEXT)
@click.version_option(None, '-v', '--version')


def markan():
    pass


markan.add_command(reddit)
markan.add_command(sheets)
markan.add_command(wordpress)
