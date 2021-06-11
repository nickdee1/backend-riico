#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Component model
"""

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER


class ModelFurniture:
        """Model for component"""

        __tablename__ = 'component'

        row_id = Column('id', \
                        INTEGER(unsigned=True), \
                        primary_key=True, \
                        autoincrement=True, \
                        doc='Furniture ID')

        name = Column('name',\
                      String(64),\
                      nullable=False,\
                      doc='Brand name of a component')

        price = Column('price', \
                    INTEGER(unsigned=True), \
                    doc='Price of a component')
