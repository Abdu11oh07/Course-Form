from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
from .forms import LessonForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app/course_list.html', {'courses': courses})

def lesson_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    return render(request, 'app/lesson_list.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'app/lesson_detail.html', {'lesson': lesson})


def add_post(request, ):
    if request.method == 'POST':
        form = LessonForm(data=request.POST)
        if form.is_valid():
            lesson = Lesson.objects.create(
                **form.cleaned_data
            )
            print(lesson, "Qo'shildi!")

    form = LessonForm()
    context = {
        "form": form
    }
    return render(request, 'app/add_post.html', context)