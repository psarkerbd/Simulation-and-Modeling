# -*- coding: utf-8 -*-
"""
Created on 8/22/2017 at 1:41 PM

@author: Pranta Sarker

Task: Inventory System

"""

Inventory_sys = {
    'event_time': [],
    'event_type': [],
    'event_size' : [],
    'inentory_level': []
}

IDS = input().split(' ');
#print(IDS);
IDS = list(map(int, IDS));

DS = input().split(' ');
DS = list(map(int , DS));

Dlog = input().split(' ');
Dlog = list(map(int , Dlog));

total_month = len(Dlog);
month = [];

for i in range(total_month):
    month.append(30 * (i+1));
print(month);

IDSlen = len(IDS);

initial_inventory_level = 40;

Inventory_sys.setdefault('event_time' , []).append(0);
Inventory_sys.setdefault('event_type' , []).append('None');
Inventory_sys.setdefault('event_size' , []).append(0);
Inventory_sys.setdefault('inventory_level' , []).append(initial_inventory_level);

#print(Inventory_sys);

limit = len(month)+6

monthIndex = 0;



