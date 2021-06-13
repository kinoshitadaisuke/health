#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/13 19:10:24 (CST) daisuke>
#

# importing argparse module
import argparse

# activities
list_activity = [
    'walking', \
    'running', \
    'swimming', \
    'cycling', \
    'squat', \
]

# METs
# Ref.: https://www.nibiohn.go.jp/eiken/programs/2011mets.pdf
data_mets = {
    'walking':  3.5,
    'running':  7.0,
    'swimming': 7.0,
    'cycling':  4.0,
    'squat':    5.0,
    }

# construction of parser object
desc   = 'calculating energy consumption by exercise using METs'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-a', '--activity', choices=list_activity, \
                     default='walking', help='activity (default: walking)')
parser.add_argument ('-t', '--time', type=float, default=1.0, \
                     help='time of exercise in hour (default: 1.0)')
parser.add_argument ('-w', '--weight', type=float, default=65.0, \
                     help='weight in kg (default: 65.0)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
activity  = args.activity
time_hr   = args.time
weight_kg = args.weight

# METs
mets = data_mets[activity]

# calculation of energy consumption
energy_consumption_kcal = (mets - 1.0) * 1.05 * time_hr * weight_kg

# printing result
print ("energy consumption = %6.1f kcal" % energy_consumption_kcal)
