
ticket_number = input("Vvedite nomer is 6 chisel: ")

if len(ticket_number) != 6:
    print("false, nomer ne pravolnii, vvedite drugoi")
else:
    
    first_half = ticket_number[:3]
    second_half = ticket_number[3:]

    
    sum_first_half = sum(map(int, first_half))
    sum_second_half = sum(map(int, second_half))

    if sum_first_half == sum_second_half:
        print("yes")
    else:
        print("no")