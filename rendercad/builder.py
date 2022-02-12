'''
Copyright 2022 zach wick <zach@zachwick.com>
Licensed under the AGPLv3 or later
'''

from mako.lookup import TemplateLookup
import click
import os
from os.path import exists


def get_file_path():
    current_dir = os.getcwd()
    cont = input(f"Will save in {current_dir + '/render.yaml'}. Continue? (Y)/n ")
    if cont.lower() == 'y':
        filepath = current_dir + '/render.yaml'
    else:
        exit(1)


def write_to_file(file, content):
    # Now that we always have a render.yaml, we can write to it.
    with open(file, 'a') as yaml:
        yaml.write(content)


def get_service_block():
    lookup = TemplateLookup(directories=['templates'], module_directory='/tmp/mako_modules')
    filepath = os.getcwd() + '/render.yaml'
    buffer = ""
    templates = [
        "flask",
        "flower",
        "redis",
        "sinatra",
        "worker",
        # "postgresql",
    ]
    # Maybe use pprint for this?
    for idx, tmp in enumerate(templates):
        print(f"({idx}) {tmp}")
    print(f"(W) Write to file and exit")
    print(f"(Q) Quit without writing")

    selection = input("Service type to add: ")
    if selection.lower() == 'q':
        print("Quitting without writing to file.")
        if exists(filepath):
            os.remove(filepath)
        return False
    elif selection.lower() == 'w':
        # Since we actually write to render.yaml on each continuing selection, this option is really just writing
        # the envVarGroups section
        template = lookup.get_template('envvargroups')
        buffer += template.render()
        write_to_file(filepath, buffer)
        return False
    else:
        try:
            selection = int(selection)
        except ValueError:
            print("Service type not recognized. Try again.")
            return True
    if selection < len(templates):
        # If we don't already have render.yaml file started, create one using the `base` template
        if not exists(filepath):
            template = lookup.get_template('base')
            buffer += template.render()

        template = lookup.get_template(templates[selection])
        buffer += template.render()
        write_to_file(filepath, buffer)
        return True
    else:
        print("Service type not recognized. Try again.")
        return True


@click.command()
def main():
    current_dir = os.getcwd()
    if exists(current_dir + '/render.yaml'):
        print("A render.yaml already exists in this directory. Exiting.")
        exit(0)
    cont = input(f"Will save in {current_dir + '/render.yaml'}. Continue? (Y)/n ")
    if cont.lower() == 'y':
        innercont = True
        while innercont:
            innercont = get_service_block()
    else:
        exit(1)
