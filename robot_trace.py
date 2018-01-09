#!/usr/bin/env python3
import argparse
import numpy as np
import re

def main():
    direction = np.array(['east','south','west','north'])
    unit_vector_along_x_axis = [1, 0, -1, 0]
    unit_vector_along_y_axis = [0, -1, 0, 1]
    parser = argparse.ArgumentParser(description='This code will trace the final location and direction of robot in 2D plane.')
    parser.add_argument('x', type=int, help='Initial X coordinate in 2D plane')
    parser.add_argument('y', type=int, help='Initial Y coordinate in 2D plane')
    parser.add_argument('d', type=str, help='Initial direction of facing')
    parser.add_argument('instruc', type=str, help='String instructions for robot to follow. e.g. R=>turn 90 degree right, L=>turn 90 degree left, WN=>walk n units forward.')
    args = parser.parse_args()
    x_init = args.x
    y_init = args.y
    d_init = str(args.d).lower()
    instructions = args.instruc

    d_final = d_init
    dir_index = np.where(direction == d_init)[0][0]
    #RegX will fetch all forward robo instruction
    forward_instructions = re.findall('W[0-9]+',instructions)
    forward_instructions_count = 0
    for instr in instructions:
        if instr == 'R':
            dir_index+=1
            if dir_index > 3:
                dir_index = 0


        if instr == 'L':
            dir_index-=1
            if dir_index < 0:
                dir_index = 3


        if instr == 'W':
            if len(forward_instructions) != 0:
                n_steps_forward = int(str(forward_instructions[forward_instructions_count]).split('W')[1])
                x_final = x_init+(unit_vector_along_x_axis[dir_index]*n_steps_forward)
                y_final = y_init+(unit_vector_along_y_axis[dir_index]*n_steps_forward)
                x_init = x_final
                y_init = y_final 
                forward_instructions_count+=1
                
            




    d_final = direction[dir_index]
    print(x_final,y_final,d_final.title())


if(__name__=='__main__'):
    main()

