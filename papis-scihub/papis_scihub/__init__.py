#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import papis.cli
import papis.api
import plugin


def download_doc(doc):
    """Tries to download documents from scihub."""
    importer = plugin.Importer(doi=doc["doi"])
    try:
        importer.get_files()
    except Exception as e:


@click.command()
@papis.cli.query_option()
@click.help_option('-h', '--help')
@click.option(
    '-o', '--out',
    help='Output file',
    default='document.pdf'
)
def main(query, out):
    """
    Tries to fetch documents from scihub.
    """
    docs = papis.api.get_documents_in_lib(
        library=papis.api.get_lib_name(),
        search=query
    )
