#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "Hfasdfasdfello": "World",
        "234234asdfasdfello": "World",
    }
