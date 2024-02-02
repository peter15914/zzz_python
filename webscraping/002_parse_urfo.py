
good_specs = ['01.00.00', '02.00.00', '10.05.01', '09.03.03', '09.03.02', '09.03.01', '09.03.04']
inf_specs = ['09.03.03', '09.03.02', '09.03.01', '09.03.04']


def good_spec(spec):
    for s in good_specs:
        if s in spec:
            return True
    return False


def main():
    f = open('wrk/best_res.txt')
    res_file = open('wrk/sorted.txt', 'wt')

    res = {}

    def add_val(spec, snils, ball, best_human_in_the_world):
        if spec not in res:
            res[spec] = []

        if len(res[spec]) and res[spec][-1] == (ball, snils, best_human_in_the_world):
            return

        res[spec].append((ball, snils, best_human_in_the_world))

    cur_snils = 0
    prev_s = ''
    for s in f.readlines():

        if 'контрактная основа' in s:
            continue

        s = s.replace('Прием в пределах квоты', '', 1)
        s = s.replace('Общий конкурс', '', 1)
        s = s.replace('бюджетная основа', '', 1)

        prms = s[1:].split('#')
        if prms[0].isdigit():
            try: cur_snils = int(prms[0])
            except: cur_snils = -9999

        spec = ''
        for i in range(len(prms)):
            if good_spec(prms[i]):
                spec = prms[i]
                if i < len(prms)-1:
                    spec += ' ' + prms[i + 1]
                break

        inf_spec = False
        for c in inf_specs:
            if c in spec:
                inf_spec = True
                break

        try:
            ball = int(prms[-1])
        except:
            continue

        best_human_in_the_world = '68' in s and '91' in s and '88' in s and ball == 247

        if good_spec(s):
            add_val(spec, cur_snils, ball, best_human_in_the_world)
            add_val("merged", cur_snils, ball, best_human_in_the_world)
            if inf_spec:
                add_val("merged_inf", cur_snils, ball, best_human_in_the_world)

    for spec in sorted(res.keys()):
        print(spec)
        res_file.write(spec + '\n')

    for spec in sorted(res.keys()):

        # print('\n\n' + spec)
        res_file.write('\naaa\n' + spec + '\n')

        res[spec].sort(reverse=True)

        ind = 1
        prev_snils = 0
        for rec in res[spec]:
            # print(rec)
            c = '!!!' if rec[2] else ''
            res_file.write(f'{ind:<4} {rec[0]} {rec[1]} {c}\n')
            ind += 1

            # check for doubles
            if prev_snils == rec[1]:
                print(f'!!Error, doubles {rec[1]}')
            prev_snils = rec[1]

    res_file.close()


if __name__ == '__main__':
    main()
