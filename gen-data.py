speeds = [[30,30],[30,33],[30,38],[30,45],[30,55]]

drivers = ['DL12345','DL121212','DL11111','XL00000']

axles = [2,4,1]

def calculate_expected(sp, dr, ax):
    error = ("ERROR", 0.0)
    over_the_limit = sp[1] - sp[0]
    
    if over_the_limit < 1:
        return error
    elif dr.startswith('XL'):
        return error
    
    return ("FINE", 25.0)
    

def generate_cases():
    id = 0
    for sp in speeds:
        for dr in drivers:
            for ax in axles:
                id += 1
                action, cost = calculate_expected(sp, dr, ax)
                print(f'T{id:05}',sp[0],sp[1],dr,ax, action, cost, sep = ',')

if __name__ == '__main__':
    generate_cases()
