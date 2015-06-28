# -*- coding: utf-8 -*-

from CuraSlicer.slicer import slicing
import click, sys

@click.command()
@click.option('--pref', required=True)
@click.option('--config', required=True)
@click.option('--model', required=True)
@click.option('--output', required=True)
def main(pref, config, model, output):
    slicing(pref, config, model, output)

if __name__ == '__main__':
    main()
