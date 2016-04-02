# Challenge # 12 Difficult

import winsound

def main():
    pass

def instrument():
    note = input('Which note should I play? ').upper()
    duration = int(input('How many miliseconds should the note be played? '))
    if note == 'A' or note == 'LA':
        winsound.Beep(440, duration)
    elif note == 'B' or note == 'SI':
        winsound.Beep(494, duration)
    elif note == 'C' or note == 'DO':
        winsound.Beep(523, duration)
    elif note == 'D' or note == 'RE':
        winsound.Beep(587, duration)
    elif note == 'E' or note == 'MI':
        winsound.Beep(659, duration)
    elif note == 'F' or note == 'FA':
        winsound.Beep(698, duration)
    elif note == 'G' or note == 'SO':
        winsound.Beep(784, duration)
    else:
        print('Input error.')
    print('\nSome of the notes are off-key.  Sorry.')
   
if __name__ == '__main__':
    main()
