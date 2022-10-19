#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:08:44 2022

@author: rhenatabella
"""

umur = 0
total = 0 
while(umur!=''):
    umur = input('Masukkan Umur:\n')
    if umur != '':
        umur_angka = int(umur)
        if umur_angka <= 2:
            print('Gratis')
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12:
            print('$14.00')
            price = 14
        elif umur_angka >= 65 :
            print('Harga $18.00')
            price = 18
        else:
            print('Harga $23.00')
            price = 23
        total += price
        print('Total: %0.2f' % total)
        
jumlah = int(input('Masukkan jumlah uang: '))
hasil = jumlah - total
print('kembalian: %0.2f' % hasil)

print('Terima kasih telah menggunakan program ini')