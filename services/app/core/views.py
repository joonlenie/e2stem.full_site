from django.shortcuts import render

from database.models import Student

# Create your views here.


        
        
def survey(request):

    if request.method == 'GET':
    
        students = Student.objects.all()
        
        student_count = len(students)
        
        context = {
        
          'student_count': student_count
          
        }

        return render(request, 'survey.html', context)
  
    if request.method == 'POST':
    
        # print(request.POST)   
         
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        teacher = request.POST.get('teacher')        
                
        question_one = request.POST.get('q-1')     
        question_two = request.POST.get('q-2')       
        print(question_one)
        
        responses = [question_one, question_two]
        responses_str = "\n\n".join(responses)
                                            
        student = Student(
        
          name=name, 
          age=int(age),
          grade=int(grade), 
          teacher=teacher, 
          responses=responses_str   
               
        )
        
        student.save()
        
        context = {}

        return render(request, 'survey.html', context)

        
        
        
