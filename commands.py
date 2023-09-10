# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
# import click

# from app import app
# from exts import db
# from models import UserModel


# @app.cli.command()
# @click.option("--drop", is_flag=True, help="Create after drop.")
# def initdb(drop):
#     """Initialize the database."""
#     if drop:
#         click.confirm(
#             "This operation will delete the database, do you want to continue?",
#             abort=True,
#         )
#         db.drop_all()
#         click.echo("Drop tables.")
#     db.create_all()
#     click.echo("Initialized database.")