def hierarchical_classify(row):
    if row['safety'] == 'low':
        return 'unacc'
    elif row['safety'] == 'med':
        if row['persons'] == '2' or row['lug_boot'] == 'small':
            return 'unacc'
        else:
            if row['buying'] in ['vhigh','high'] or row['maint'] in ['vhigh','high']:
                return 'acc'
            else:
                return 'good'
    else:  # high
        if row['persons'] == '2':
            return 'unacc'
        elif row['lug_boot'] == 'small':
            return 'acc'
        else:
            if row['buying'] in ['vhigh','high'] or row['maint'] in ['vhigh','high']:
                return 'acc'
            else:
                return 'vgood'
