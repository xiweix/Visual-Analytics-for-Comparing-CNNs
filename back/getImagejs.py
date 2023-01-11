import os
from utils import idxToWord, idxToID

dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
write_path = 'image.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default [\n')
for label in range(1000):
    wordID = idxToID(dataset_path, label)
    name = idxToWord(dataset_path, label)
    name = f'{label}.{name}'
    if label == 999:
        with open(write_path, 'a') as ftxt:
            ftxt.write('  {\n')
            ftxt.write('    label: \'')
            ftxt.write(f'{label}')
            ftxt.write('\',\n')
            ftxt.write('    name: \'')
            ftxt.write(f'{name}')
            ftxt.write('\',\n')
            ftxt.write('    id: \'')
            ftxt.write(f'{wordID}')
            ftxt.write('\'\n')
            ftxt.write('  }\n')
    else:
        with open(write_path, 'a') as ftxt:
            ftxt.write('  {\n')
            ftxt.write('    label: \'')
            ftxt.write(f'{label}')
            ftxt.write('\',\n')
            ftxt.write('    name: \'')
            ftxt.write(f'{name}')
            ftxt.write('\',\n')
            ftxt.write('    id: \'')
            ftxt.write(f'{wordID}')
            ftxt.write('\'\n')
            ftxt.write('  },\n')
with open(write_path, 'a') as ftxt:
    ftxt.write(']\n')
