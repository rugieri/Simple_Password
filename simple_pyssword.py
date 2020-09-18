#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simple_pyssword.py
#  
#  Copyright 2020 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import string
import secrets

def secure_password_gen(passlength):
    password = ''.join((secrets.choice(string.ascii_letters + string.hexdigits) for i in range(passlength)))
    return password

n = int(input('Enter length of password : '))
print('Password generated is :', secure_password_gen(n))

