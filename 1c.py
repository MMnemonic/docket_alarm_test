for i in range(1, 1001):

    if i % 7 == 0:
        text = 'Docket'
        if i % 6 == 0:
            text += ' Alarm'
    elif i % 6 == 0:
        text = 'Alarm'
    else: 
        text = str(i)

    print(text)

        






    
