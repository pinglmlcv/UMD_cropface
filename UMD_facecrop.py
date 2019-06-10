import csv
import os
import argparse
import cv2

def crop_face(inputfile, input_dir, output_dir):
	with open(inputfile) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		cnt = 0
		for row in csv_reader:
			if cnt == 0:
				cnt = cnt + 1
				continue
			img_name = row[1]
			face_x = int(float(row[4]))
			face_y = int(float(row[5]))
			face_width = int(float(row[6]))
			face_height = int(float(row[7]))

			if not os.path.isfile(os.path.join(input_dir, img_name)):
				print('Image \t{} NOT exists'.format(os.path.join(input_dir, img_name)))
				break
			else:
				print('Image \t{} exists'.format(os.path.join(input_dir, img_name)))
				print face_x
				print face_y
				print face_width
				print face_height

				img = cv2.imread(os.path.join(input_dir, img_name))
				savename = os.path.join(output_dir, img_name)
				print savename

				save_subdir = os.path.join(output_dir, img_name.split('/')[0])
				if not os.path.isdir(save_subdir):
					os.mkdir(save_subdir)
				# print save_subdir

				cv2.imwrite(savename, img[face_y:face_y+face_height, face_x: face_x+face_width, :]) 


def parse_args():

    description = "crop faces from original images"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--inputcsv', type=str)
    parser.add_argument('--input_dir', type=str)
    parser.add_argument('--output_dir', type=str)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
	args = parse_args()

	assert os.path.exists(args.inputcsv), 'Not found the input csv file=>'.format(args.inputcsv)
	assert os.path.exists(args.input_dir), 'Not found the input dir =>'.format(args.input_dir)

	if not os.path.isdir(args.output_dir):
		os.mkdir(args.output_dir)

	crop_face(args.inputcsv, args.input_dir, args.output_dir)