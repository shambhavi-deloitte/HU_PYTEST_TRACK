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