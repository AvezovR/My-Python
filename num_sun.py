def oscillation(a, b):
    number_of_oscillations = 0
    while a > b:
        a -= a * 0.084
        number_of_oscillations += 1

    return number_of_oscillations

onset_amplitude = float(input('Введите начальную амплитуду: '))
stopping_amplitude = float(input('Введите амплитуду остановки: '))

while True:

    if onset_amplitude <= 0 or stopping_amplitude <= 0:
        print('Значения должны быть больше "0", введите значения заново')
        onset_amplitude = float(input('Введите начальную амплитуду: '))
        stopping_amplitude = float(input('Введите амплитуду остановки: '))
    else:
        number_of_oscillations = oscillation(onset_amplitude, stopping_amplitude)
        print(f'Маятник считается остановившимся через {number_of_oscillations} колебаний')
        break
