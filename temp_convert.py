def temp_convert (temp, orig_unit='degC', target_unit ='K' ):
    """this function should convert temperature units beteween degC / K / degF"""

    if orig_unit == 'degC' and target_unit == 'K':
        t=temp+273
        print( t,'k')
    elif orig_unit == 'K' and target_unit=='degC':
        t=temp-273
        print(t,'degC')

    elif orig_unit=='K' and target_unit=='degF':
        t=((temp-273.5)*(9/5))+32
        print(t,'degF')
    elif orig_unit=='degF' and target_unit=='K':
        t=((temp-32)*(5/9))+273
        print(t,'K')

    elif orig_unit=='degC' and target_unit=='degF':
        t=(temp*9/5)+32
        print(t,'degF')
    elif orig_unit=='degF' and target_unit=='degC':
        t=(temp-32)*(5/9)
        print(t,'degC')
    

temp_convert(59,orig_unit='degF', target_unit='degC')

