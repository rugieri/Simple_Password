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

p = "y"
while p=="y":
	def secure_password_gen(passlength):
		"""Makes a random password with combination of uppercase and lowcase letters,
		numbers and some special digits
		"""		
		password = ''.join((secrets.choice(string.ascii_letters + string.digits + '!@#$%¨&*')
		for i in range(passlength)))
		return password 
					
	n = int(input("Enter length of password : "))
	print('Password generated is :', secure_password_gen(n))
	p = input("Push Y to generate another password or X to esc  ") 
	

else:
	while  p != "x":
		print("Sorry but you must press X to esc")
		n = int(input("Enter length of password: "))
		print('Password generated is :', secure_password_gen(n))
		p = input("Push Y to generate another password or X to esc  ")
		

