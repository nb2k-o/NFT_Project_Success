#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:56:49 2022

@author: Sugar
"""

import twint
import nest_asyncio


nest_asyncio.apply()

c = twint.Config()
c.Username = "AvaStarsNFT"
c.Until = "2022-03-06"
c.Store_csv = True
c.Output = "Sum.csv"
c.Store_object = True


twint.run.Lookup(c)