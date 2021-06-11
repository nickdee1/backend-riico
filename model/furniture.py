#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Furniture model
"""

from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import INTEGER

MATERIAL = Enum('solid wood', 'wood', 'metal', 'fabric', 'wood veneer')


class ModelFurniture:
        """Model for furniture"""

        __tablename__ = 'furniture'

        row_id = Column('furniture_id', \
                        INTEGER(unsigned=True), \
                        primary_key=True, \
                        autoincrement=True, \
                        doc='Furniture ID')

        category = Column('category',\
                          String(64),\
                          nullable=False,\
                          doc='Category of a furniture')

        name = Column('name',\
                      String(64),\
                      nullable=False,\
                      doc='Brand name of a furniture')

        color = Column('color',\
                      String(64),\
                      nullable=False,\
                      doc='Color of a furniture')

        location = Column('location',\
                      String(64),\
                      nullable=False,\
                      doc='Location of a furniture')

        material = Column('account_type',\
                        MATERIAL,\
                        nullable=False,\
                        doc='Material')

        width = Column('width', \
                    INTEGER(unsigned=True), \
                    doc='Width of a model')

        height = Column('height', \
                    INTEGER(unsigned=True), \
                    doc='Height of a model')

