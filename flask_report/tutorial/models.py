#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# models.py
from datetime import datetime

from basemain import db


class Department(db.Model):

    __tablename__ = 'TB_DEPARTMENT'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)

    def __repr__(self):
        return '<Department(%s)>' % self.name


class Worker(db.Model):

    __tablename__ = 'TB_WORKER'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    deparment_id = db.Column(db.Integer, db.ForeignKey('TB_DEPARTMENT.id'),
                             nullable=False)
    age = db.Column(db.Integer)

    department = db.relationship('Department', backref='worker_list')


class WorkCommand(db.Model):

    __tablename__ = 'TB_WORK_COMMAND'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    worker_id = db.Column(db.Integer, db.ForeignKey('TB_WORKER.id'),
                          nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)

    worker = db.relationship('Worker', backref='work_command_list')
