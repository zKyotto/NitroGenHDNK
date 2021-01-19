# -*- coding: utf-8 -*-
import random, string,os
from colorama import Fore, init
init(convert=True)

def main():
    os.system('cls&title [Discord Nitro Generator] By Kyotto')
    print(Fore.RED + """
    
                                                                                         
                                                                                   
 7MMF    7MMF   db       7MM       7MM     Dev: Kyotto          7MN.     7MF7 MMF  YMM' 
  MM      MM              MM        MM                           MMN.    M    MM   .M'   
  MM      MM  `7MM   ,M""bMM   ,M""bMM  .gP"Ya `7MMpMMMb.        M YMb   M    MM .d"     
  MMmmmmmmMM    MM ,AP    MM ,AP    MM ,M'   Yb  MM    MM        M  `MN. M    MMMMM.     
  MM      MM    MM 8MI    MM 8MI    MM 8M""""""  MM    MM        M   `MM.M    MM  VMA    
  MM      MM    MM `Mb    MM `Mb    MM YM.    ,  MM    MM        M     YMM    MM   `MM.  
.JMML.  .JMML..JMML.`Wbmd"MML.`Wbmd"MML.`Mbmmd'.JMML  JMML.    .JML.    YM  .JMML.   MMb.
                                                                                         
                                                                                              
    
    """ + Fore.RESET)
    print(Fore.GREEN + "[$] Finalizada la descarga... Puedes empezar a generar!\n" + Fore.RESET)
    amount = int(input(Fore.CYAN + '[$] Pon la cantidad de nitro que quieras generar [ >>> ]: '))
    value = 1
    while value <= amount:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        f = open('codes.txt', "a+")
        f.write(f'{code}\n')
        f.close()
        print(Fore.GREEN + "[$] [GENERADO...] " + Fore.RESET , code)
        value += 1
    print(Fore.WHITE + "Se han generado " + str(value-1) + " Codes Correctamente!\nSi quieres ver los codigos revisa " + Fore.RED + "Codes.txt " + Fore.RESET + "En el directorio del programa.")
    input(Fore.MAGENTA + 'Presiona enter para salir del generador:')

try:
    main()
except Exception as e:
    print(e)
    pass    