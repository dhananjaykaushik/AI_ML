# Generates output file with all descriptions
import glob
import json
import os

output_file_path = './output.txt'
root_dir = '../../../centilytics/centilytics-v2/local-s3/api-resources/'

content_string = 'Centilytics Description'

print('Combining all descriptions............')

for filepath in glob.iglob(root_dir + '**/description.json', recursive=True):
    splitted_path = filepath.split('/')
    file_name = splitted_path[-2]
    insight_root_directory = '/'.join(splitted_path[0:-1])
    # Reading insight json
    insight_json = '{}/{}.json'.format(insight_root_directory, file_name)
    insight_file = open(insight_json,)
    insight_file_data = json.load(insight_file)
    if 'text' in insight_file_data:
        description_json = '{}/description.json'.format(insight_root_directory)
        if os.path.isfile(description_json):
            description_file = open(
                description_json, 'r', encoding='utf-8', errors='ignore')
            description_file_data = json.load(description_file)
            if description_file_data and 'checkDescription' in description_file_data and 'description' in description_file_data['checkDescription']:
                check_description = description_file_data['checkDescription']
                content_string += '\n\n{}\n'.format(
                    insight_file_data['text'].strip())
                content_string += check_description['description'].strip()
                # .encode('utf-8', 'ignore')

    # Writing to file
    op_file = open(output_file_path, 'w')
    op_file.write(content_string)
    op_file.close()


print('Done')
print('Check the file at path: {}'.format(output_file_path))
