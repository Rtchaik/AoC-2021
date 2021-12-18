import Day14.solution as current

test1 = ({
    'NN': 1,
    'NC': 1,
    'CB': 1
}, {
    'CH': ['CB', 'BH'],
    'HH': ['HN', 'NH'],
    'CB': ['CH', 'HB'],
    'NH': ['NC', 'CH'],
    'HB': ['HC', 'CB'],
    'HC': ['HB', 'BC'],
    'HN': ['HC', 'CN'],
    'NN': ['NC', 'CN'],
    'BH': ['BH', 'HH'],
    'NC': ['NB', 'BC'],
    'NB': ['NB', 'BB'],
    'BN': ['BB', 'BN'],
    'BB': ['BN', 'NB'],
    'BC': ['BB', 'BC'],
    'CC': ['CN', 'NC'],
    'CN': ['CC', 'CN']
})

assert current.part1(*test1, 10) == 1588

assert current.part1(*test1, 40) == 2188189693529
