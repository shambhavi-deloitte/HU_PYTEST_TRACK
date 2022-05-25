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