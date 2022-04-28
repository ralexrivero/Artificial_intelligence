#!/usr/bin/env python3
""" dictionary iteration requieres the items() method """

europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw',
          'austria': 'vienna'}

for key, value in europe.items():
    print("The capital of {} is {}".format(key, value))
