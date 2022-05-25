import csv

movie_timings_seats={}

def calculating_timings(ip_title):
	data=single_movie_info[ip_title];all_timings=[]
	length=data[1];nos=data[7];fs=data[8];it=data[9];gap=data[10]
	time_split=length.split()
	h=time_split[0].split('hr')[0];m=time_split[1].split('mins')[0]
	total_minutes=int(m)+int(h)*60
	if 'AM' in fs:
		fs_split=fs.split('AM')
		if ':' in fs_split[0]:
			fs_h = int(fs_split[0].split(':')[0])
			fs_m = int(fs_split[0].split(':')[1])
		else:
			fs_split = fs.split('PM')
			if ':' in fs_split[0]:
				fs_h = int(fs_split[0].split(':')[0])
				fs_m = int(fs_split[0].split(':')[1])
		total_delay_time = 0
		total_delay_time += int(it.split('mins')[0])
		total_delay_time += int(gap.split('mins')[0])
		total_delay_time += total_minutes
		temp = total_delay_time
		all_timings.append([fs_h, fs_m])
		for i in range(int(nos) - 1):
			total_delay_time = temp
			while total_delay_time > 60:
				if fs_h == 11:
					fs_h = 0
				else:
					fs_h += 1
				total_delay_time -= 60
			fs_m += total_delay_time
			if fs_m > 60:
				if fs_h == 11:
					fs_h = 0
				else:
					fs_h += 1
				fs_m -= 60
			all_timings.append([fs_h, fs_m])
		return all_timings
	info_names = ['Genre', 'Length', 'Cast', 'Director', 'Admin Rating', 'Language', 'Timings',
				  'Number of Shows in a day', 'First Show', 'Interval Time', 'Gap Between Shows', 'Capacity']

	u_fields = ['USERNAME', 'EMAIL', 'PHONE', 'AGE', 'PASSWORD']
	users_data = [];
	uname_pass = {'admin': 'admin'}
	file_name = "C:\\Users\\shampriya\\Desktop\\user_data.csv"
	with open(file_name, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			if row != []:
				users_data.append(row)
				uname_pass[row[0]] = row[4]

	movies_info_names = ['Title', 'Genre', 'Length', 'Cast', 'Director', 'Admin Rating', 'Language', 'Timings',
						 'Number of Shows in a day', 'First Show', 'Interval Time', 'Gap Between Shows', 'Capacity']
	all_movies_info = []
	single_movie_info = {}
	file_name = "C:\\Users\\shampriya\\Desktop\\movies_data.csv"
	with open(file_name, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		fields = next(csvreader)
		for row in csvreader:
			try:
				if row[0] != '' and row != []:
					all_movies_info.append(row)
					single_movie_info[row[0]] = row[1:]
					if len(row) == 14:
						movie_timings_seats[row[0]] = [calculating_timings(row[0]), int(row[12]), row[13]]
					else:
						movie_timings_seats[row[0]] = [calculating_timings(row[0]), int(row[12]), '']
			except:
				continue

	def update_user_info():
		file_name = "C:\\Users\\shampriya\\Desktop\\user_data.csv"
		with open(file_name, 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(u_fields)
			csvwriter.writerows(users_data)