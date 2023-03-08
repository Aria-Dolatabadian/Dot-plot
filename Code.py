import pygal
dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'RGAs Number on Chromosomes'
dot_chart.x_labels = ['CNL', 'TNL', 'RLK', 'RLP', 'NBS', 'TX', 'TN', 'NBS-LRR']
dot_chart.add('Chromosome 1', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
dot_chart.add('Chromosome 2', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
dot_chart.add('Chromosome 3', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
dot_chart.add('Chromosome 4', [4543, 9541, 6559, 2579, 5144, 6136, 734, 3102])
dot_chart.render()
dot_chart.render_to_file('dot_chart.svg')
