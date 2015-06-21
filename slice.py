# -*- coding: utf-8 -*-

from CuraSlicer.slicer import slicing
import click, sys

@click.command()
@click.option('--config', required=True)
@click.option('--model', required=True)
@click.option('--output', required=True)
def main(config, model, output):
    slicing(config, model, output)

if __name__ == '__main__':
    main()
