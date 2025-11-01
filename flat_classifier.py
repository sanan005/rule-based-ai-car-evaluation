def flat_classify(row):
    if row['safety'] == 'low':
        return 'unacc'
    if row['persons'] == '2':
        return 'unacc'
    if row['buying'] == 'vhigh' and row['maint'] == 'vhigh':
        return 'unacc'
    if row['safety'] == 'high' and row['lug_boot'] == 'big' and row['persons'] == 'more':
        return 'vgood'
    if row['safety'] == 'high' and row['buying'] in ['low', 'med']:
        return 'good'
    if row['safety'] == 'med' and row['lug_boot'] != 'small':
        return 'acc'
    return 'unacc'  # default
