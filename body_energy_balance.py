#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/06/13 19:10:33 (CST) daisuke>
#

# importing argparse module
import argparse

# constatns
fat_kcal_per_kg = 7200.0

# list of sex
list_sex = ['female', 'male']
list_life = ['low', 'medium', 'high']

# construction of parser object
desc   = 'energy balance of body'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-a', '--age', type=float, default=40.0, \
                     help='age in year (default: 40.0)')
parser.add_argument ('-f', '--food', type=float, default=-9999.9, \
                     help='energy input per day by food in kcal')
parser.add_argument ('-g', '--goal', type=float, default=5.0, \
                     help='goal of weight loss in kg (default: 5.0)')
parser.add_argument ('-l', '--life', choices=list_life, default='low', \
                     help='activity level of daily life (default: medium)')
parser.add_argument ('-r', '--range', type=float, default=6.0, \
                     help='range of exercise in month (default: 6)')
parser.add_argument ('-s', '--sex', choices=list_sex, default='female', \
                     help='sex (default: female')
parser.add_argument ('-t', '--height', type=float, default=170.0, \
                     help='height in cm (default: 170.0)')
parser.add_argument ('-w', '--weight', type=float, default=65.0, \
                     help='weight in kg (default: 65.0)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
sex         = args.sex
age_year    = args.age
height_cm   = args.height
weight_kg   = args.weight
life        = args.life
goal_kg     = args.goal
range_month = args.range
food_kcal   = args.food

# printing input parameters
print ("#")
print ("# Input parameters")
print ("#")
print ("#   sex    = %s" % sex)
print ("#   age    = %5.1f years" % age_year)
print ("#   height = %5.1f cm" % height_cm)
print ("#   weight = %5.1f kg" % weight_kg)
print ("#")
print ("#   goal of weight loss    = %4.1f kg" % goal_kg)
print ("#   time range of exercise = %4.1f month" % range_month)

# function to calculate basal metabolic rate from sex, age, height, and weight
def calc_basal_metabolic_rate (sex, age_year, height_cm, weight_kg):
    # basal metabolic rate in kcal
    # Gunpule et al. 2007
    # Ganpule AA, Tanaka S, Ishikawa-Takata K, Tabata I.
    # Interindividual variability in sleeping metabolic rate
    # in Japanese subjects. Eur J Clin Nutr 61(11): 1256-1261, 2007.
    # https://www.nibiohn.go.jp/eiken/hn/modules/kisotaisya/
    if (sex == 'female'):
        basal_metabolic_rate_kcal \
            = (0.1238 + 0.0481 * weight_kg + 0.0234 * height_cm \
               - 0.0138 * age_year - 0.5473 * 2.0) * 1000.0 / 4.186
    elif (sex == 'male'):
        basal_metabolic_rate_kcal \
            = (0.1238 + 0.0481 * weight_kg + 0.0234 * height_cm \
               - 0.0138 * age_year - 0.5473 * 1.0) * 1000.0 / 4.186
    # returning basal metabolic rate in kcal
    return (basal_metabolic_rate_kcal)

# function to evaluate activity level of daily life
def eval_body_activity_level (life):
    # low activity level
    if (life == 'low'):
        body_activity_level = 1.50
    # medium activity level
    elif (life == 'medium'):
        body_activity_level = 1.75
    # high activity level
    elif (life == 'high'):
        body_activity_level = 2.00
    # returning body activity level
    return (body_activity_level)

# function to calculate necessary energy consumption by exercise
def calc_energy_consumption_by_exercise \
    (goal_kg, range_month, fat_kcal_per_kg, \
     energy_consumption_without_exercise_kcal_per_day, food_kcal):
    # calculation of necessary energy consumption by exercise
    range_day = range_month * 30.0
    energy_exercise_kcal = goal_kg * fat_kcal_per_kg \
        + (food_kcal - energy_consumption_without_exercise_kcal_per_day) \
        * range_day
    energy_exercise_kcal_per_day = energy_exercise_kcal / range_day
    # returning necessary energy consumption by exercise per day
    return (energy_exercise_kcal_per_day)

# calculation of basal metabolic rate in kcal
basal_metabolic_rate_kcal = calc_basal_metabolic_rate (sex, age_year, \
                                                       height_cm, weight_kg)

# energy consumption without exercise per day
body_activity_level = eval_body_activity_level (life)
energy_consumption_without_exercise_kcal_per_day \
    = basal_metabolic_rate_kcal * body_activity_level

# energy input by food in kcal
if (food_kcal < 0.0):
    food_kcal = energy_consumption_without_exercise_kcal_per_day

# necessary energy consumption by exercise per day
energy_consumption_exercise_kcal_per_day \
    = calc_energy_consumption_by_exercise \
    (goal_kg, range_month, fat_kcal_per_kg, \
     energy_consumption_without_exercise_kcal_per_day, food_kcal)

# total energy consumption per day
total_energy_consumption_kcal_per_day \
    = energy_consumption_without_exercise_kcal_per_day \
    + energy_consumption_exercise_kcal_per_day

# input energy
energy_input = food_kcal

# output energy
#energy_output = 

# printing results of calculation
print ("#")
print ("# Results of calculation")
print ("#")
print ("#   Energy balance to achieve weight loss goal:")
print ("#                                                       %+7.1f kcal" \
       % (food_kcal - total_energy_consumption_kcal_per_day) )
print ("#   Energy input:")
print ("#     eating                                           = %6.1f kcal" \
       % food_kcal)
print ("#   Energy output:")
print ("#     basal metabolic rate                             = %6.1f kcal" \
       % basal_metabolic_rate_kcal)
print ("#     energy consumption without exercise per day      = %6.1f kcal" \
       % energy_consumption_without_exercise_kcal_per_day)
print ("#     necessary energy consumption by exercise per day = %6.1f kcal" \
       % energy_consumption_exercise_kcal_per_day)
print ("#     total energy consumption per day                 = %6.1f kcal" \
       % total_energy_consumption_kcal_per_day)
print ("#")
