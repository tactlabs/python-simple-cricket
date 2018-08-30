#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

@author: raja.raman

source:
    https://pymotw.com/3/threading/
'''

from random import randint
import time

BALL_INTERVAL = 0.1
TOTAL_OVERS = 20
TOTAL_PLAYERS = 11

team_a = 'India'
team_b = 'England'

team_a_players = [    
    'Virat Kohli',
    'Rohit Sharma',
    'Jasprit Bumrah',
    'Yuzvendra Chahal',
    'Shikhar Dhawan',
    'MS Dhoni',
    'Dinesh Karthik',
    'Kuldeep Yadav',
    'Bhuvneshwar Kumar',
    'Manish Pandey',
    'Hardik Pandya',
    ]
team_b_players = [
    'Eoin Morgan',
    'Moeen Ali',
    'Jonny Bairstow',
    'Jake Ball',
    'Jos Buttler',
    'Sam Curran',
    'Tom Curran',
    'Alex Hales',
    'Chris Jordan',
    'Liam Plunkett',
    'Adil Rashid',
    ]

team_a_total_score = 0
team_b_total_score = 0

team_a_wickets_down = 0
team_b_wickets_down = 0

def get_random_run():
    
    wicket_probability_base = randint(0, 10)
    
    wicket = 0
    if(wicket_probability_base > 9):
        wicket = 1
        
    run = randint(0, 6)
    
    if(run == 5):
        run = 4
    
    return wicket, run

def team_1_batting(over_no, ball_no, team_name):
    """ team 1 batting function"""
        
    wicket, run = get_random_run()
    
    global team_a_total_score
    global team_a_wickets_down
    
    if(wicket == 0):
        team_a_total_score = team_a_total_score + run
    else:
        team_a_wickets_down = team_a_wickets_down +1                            
    
    if(wicket == 1):
        print('Ball %s \t It\'s a wicket!' % (ball_no) )        
    else:
        print('Ball %s \t Batsman scored : %s total[%s / %s] ' % (ball_no, run, team_a_total_score, team_a_wickets_down))
        

def team_2_batting(over_no, ball_no, team_name):
    """bowl function"""
        
    wicket, run = get_random_run()
    
    #print(wicket)
    
    global team_a_total_score
    global team_b_total_score
    
    global team_a_wickets_down
    global team_b_wickets_down
    
    if(wicket == 0):     
        team_b_total_score = team_b_total_score + run
        #print('team_b_total_score : '+str(team_b_total_score))
        
        if(team_b_total_score > team_a_total_score):
            raise TeamBWonTheMatch        
    else:
        team_b_wickets_down = team_b_wickets_down +1
            
    if(wicket == 1):
        print('Ball %s \t It\'s a wicket!' % (ball_no) )        
    else:
        print('\t Batsman scored : %s total[%s / %s] ' % (run, team_b_total_score, team_b_wickets_down))        
    
# deprecated
def bowl(over_no, ball_no, team_index, team_name):
    """bowl function"""
        
    wicket, run = get_random_run()
    
    #print(wicket)
    
    global team_a_total_score
    global team_b_total_score
    
    global team_a_wickets_down
    global team_b_wickets_down
    
    if(team_index == 1):
        if(wicket == 0):
            team_a_total_score = team_a_total_score + run
        else:
            team_a_wickets_down = team_a_wickets_down +1
        
        
    else:   
        if(wicket == 0):     
            team_b_total_score = team_b_total_score + run
            #print('team_b_total_score : '+str(team_b_total_score))
            
            if(team_b_total_score > team_a_total_score):
                raise TeamBWonTheMatch
            
        else:
            team_b_wickets_down = team_b_wickets_down +1
            
                            
    
    #print('Ball %s : ' % (ball_no))
    if(wicket == 1):
        print('Ball %s \t It\'s a wicket!' % (ball_no) )        
    else:
        if(team_index == 1):
            print('Ball %s \t Batsman scored : %s total[%s / %s] ' % (ball_no, run, team_a_total_score, team_a_wickets_down))
        else:
            print('\t Batsman scored : %s total[%s / %s] ' % (run, team_b_total_score, team_b_wickets_down))
            
        
class AllWicketsDownException( Exception ):
    pass

class TeamBWonTheMatch( Exception ): # by matching the runs
    pass

class TeamAWonTheMatch( Exception ): # by getting all wickets of second team
    pass        
        
def play_over(overs, team_index, team):
    
    for over in range(overs):
        
        over_no = over + 1
        print('------------------------')        
        print('Over '+str(over_no))
        
        for ball in range(6):
            
            ball_no = ball+1 
            #bowl(over_no, ball_no, team_index, team)
            
            if(team_index == 1):
                team_1_batting(over_no, ball_no, team)
            else:
                team_2_batting(over_no, ball_no, team)
            
            
            if(team_index == 1):
                if(team_a_wickets_down >= (TOTAL_PLAYERS-1)):
                    raise AllWicketsDownException
        
            if(team_index == 2):
                if(team_b_wickets_down >= (TOTAL_PLAYERS-1)):
                    raise AllWicketsDownException

            
            time.sleep(BALL_INTERVAL)

def main():
    
    # First Innings
    print(team_a+' Batting')
    print('---------------')
    try:    
        play_over(TOTAL_OVERS, 1, team_a)
    except AllWicketsDownException:
        print(team_a+' lost all Wickets')        
    print('\n'+team_a+' Total Score : '+str(team_a_total_score)+'/'+str(team_a_wickets_down)) 
        
    print('\n\n')
        
    # Second Innings
    print(team_b+' Batting')
    print('---------------')    
    try:
        play_over(TOTAL_OVERS, 2, team_b)
    except AllWicketsDownException:
        print(team_b+' lost all Wickets')
    except TeamBWonTheMatch:
        print(team_b+' won the match')  
    print('\n'+team_b+' Total Score : '+str(team_b_total_score)+'/'+str(team_b_wickets_down))
    
    print('\n\n')
    
    if(team_a_total_score > team_b_total_score):
        print(team_a+' Won by '+str(team_a_total_score - team_b_total_score) + ' runs')
    elif(team_b_total_score > team_a_total_score):
        print(team_b+' Won by '+str((TOTAL_PLAYERS-1) - team_b_wickets_down) + ' wickets')    
    else:
        print('Match Tied')    
    
if __name__ == '__main__':
    main()
    
    
'''
India:
http://www.espncricinfo.com/ci/content/squad/1134740.html
    Virat Kohli
    Rohit Sharma
    Jasprit Bumrah
    Yuzvendra Chahal
    Shikhar Dhawan
    MS Dhoni
    Dinesh Karthik
    Kuldeep Yadav
    Bhuvneshwar Kumar
    Manish Pandey
    Hardik Pandya
    Axar Patel
    Lokesh Rahul
    Suresh Raina
    Shardul Thakur
    Jaydev Unadkat

England:
http://www.espncricinfo.com/ci/content/squad/1149791.html
    Eoin Morgan
    Moeen Ali
    Jonny Bairstow
    Jake Ball
    Jos Buttler
    Sam Curran
    Tom Curran
    Alex Hales
    Chris Jordan
    Liam Plunkett
    Adil Rashid
    Joe Root
    Jason Roy
    David Willey
'''