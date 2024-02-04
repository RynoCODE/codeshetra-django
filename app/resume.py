from django.shortcuts import render 
def home(request): 
	return render(request, 'index.html') 
def gen_resume(request): 
	if request.method == 'POST': 
		name = request.POST.get('name', '') 
		about = request.POST.get('about', '') 
		age = request.POST.get('age', '') 
		email = request.POST.get('email', '') 
		phone = request.POST.get('phone', '') 
		skill1 = request.POST.get('skill1', '') 
		skill2 = request.POST.get('skill2', '') 
		skill3 = request.POST.get('skill3', '') 
		skill4 =request.POST.get('skill4', '') 
		skill5 =request.POST.get('skill5', '') 
		degree1 = request.POST.get('degree1', '') 
		college1 = request.POST.get('college1', '') 
		year1 = request.POST.get('year1', '') 
		degree2 = request.POST.get('degree2', '') 
		college2 = request.POST.get('college2', '') 
		year2 = request.POST.get('year2', '') 
		college3 = request.POST.get('college3', '') 
		year3 = request.POST.get('year3', '') 
		degree3 = request.POST.get('degree3', '') 
		lang1 = request.POST.get('lang1', '') 
		lang2 = request.POST.get('lang2', '') 
		lang3 = request.POST.get('lang3', '')	 
		project1= request.POST.get('project1', '') 
		durat1 = request.POST.get('duration1', '') 
		desc1 = request.POST.get('desc1', '') 
		project2 = request.POST.get('project2', '') 
		durat2 = request.POST.get('duration2', '') 
		desc2 = request.POST.get('desc2', '') 
		company1 = request.POST.get('company1', '') 
		post1 = request.POST.get('post1', '') 
		duration1 = request.POST.get('duration1', '') 
		lin11 = request.POST.get('lin11', '') 
		company2 = request.POST.get('company2', '') 
		post2 = request.POST.get('post2', '') 
		duration2 = request.POST.get('duration2', '') 
		lin21 = request.POST.get('lin21', '') 
		ach1 = request.POST.get('ach1', '') 
		ach2 = request.POST.get('ach2', '') 
		ach3 = request.POST.get('ach3', '') 
		return render(request, 'resume.html', {'name':name, 
											'about':about, 'skill5':skill5, 
											'age':age, 'email':email, 
											'phone':phone, 'skill1':skill1, 
											'skill2':skill2, 'skill3':skill3, 
											'skill4':skill4, 'degree1':degree1, 
											'college1':college1, 'year1':year1, 
											'college3':college3, 'year3':year3, 
											'degree3':degree3, 'lang1':lang1, 
											'lang2':lang2, 'lang3':lang3, 
											'degree2':degree2, 'college2':college2, 
											'year2':year2, 'project1':project1, 
											'durat1':durat1, 'desc1':desc1, 
											'project2':project2, 'durat2':durat2, 
											'desc2':desc2, 'company1':company1, 
											'post1':post1, 'duration1': duration1, 
											'company2':company2, 'post2':post2, 
											'duration2': duration2,'lin11':lin11, 
												'lin21':lin21, 'ach1':ach1, 
												'ach2':ach2,'ach3':ach3 }) 
	
	return render(request, 'resume-index.html')
