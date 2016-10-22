#!/usr/bin/env python3.5

print("Входные данные")
minutes = int(input())

d_hours = minutes // 60
d_minutes = minutes - (d_hours * 60)
d_days = (minutes // (24 * 60)) * 24

print(minutes, '-', d_hours - d_days, d_minutes)
