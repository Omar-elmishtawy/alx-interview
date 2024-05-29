#!/usr/bin/python3

def pascal_triangle(n):
	pscl_list = [[1]]
	tmp_list = []
	for i in range(n):
    		tmp_list.append(1)
    		for j in range(1, len(pscl_list[i])):
        		tmp_list.append(pscl_list[i][j] + pscl_list[i][j - 1])
    		tmp_list.append(1)
    		pscl_list.append(tmp_list)
    		tmp_list = []
	return pscl_list
