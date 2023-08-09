# # from django.shortcuts import render, redirect
# # from blog.models import Word
# # import random
# #
# #
# # def test(request):
# #     if request.method == 'POST':
# #         answer = request.POST.get('answer')
# #         correct_answer = request.session.get('correct_answer')
# #         if answer == correct_answer:
# #             return redirect('Just')
# #         else:
# #             return redirect('incorrect')
# #     else:
# #         word = Word.objects.all()
# #         words = random.sample(list(word), 4)
# #         correct_answer = random.choice(words).title
# #         pictures = correct_answer.picture
# #         title = correct_answer.title
# #         request.session['correct_answer'] = correct_answer
# #
# #         context = {
# #             'words': words,
# #             'pictures': pictures,
# #             'title': title,
# #         }
# #         return render(request, 'test.html', context)
# #
# #
# # def result(request):
# #     correct_answer = request.session.get('correct_answer')
# #     answer = request.POST.get('answer')
# #     if answer == correct_answer:
# #         return redirect('Just')
# #     else:
# #         return redirect('incorrect')
# #
# #
# # def Just(request):
# #     return render(request, 'just.html')
# #
# #
# # def incorrect(request):
# #     return render(request, 'incorrect.html')
#
#
# from django.shortcuts import render, redirect
# from blog.models import Word
# import random
# #
# from django.shortcuts import render, redirect
# from blog.models import Word
# import random
#
#
# def test(request):
#     if request.method == 'POST':
#         answer = request.POST.get('answer')
#         correct_answer = request.session.get('correct_answer')
#         if answer == correct_answer:
#             return redirect('Just')
#         else:
#             return redirect('incorrect')
#     else:
#         words = list(Word.objects.all())
#         sample_words = random.sample(words, 4)
#         for word in sample_words:
#             print(word.title)
#             print(word.picture)
#         request.session['correct_answer'] = correct_answer
#
#         context = {
#             'words': words,
#             'pictures': pictures,
#             'title': title,
#         }
#         return render(request, 'test.html', context)
#
#
# def result(request):
#     correct_answer = request.session.get('correct_answer')
#     answer = request.POST.get('answer')
#     if answer == correct_answer:
#         return redirect('Just')
#     else:
#         return redirect('incorrect')
#
#
# def Just(request):
#     return render(request, 'just.html')
#
#
# def incorrect(request):
#     return render(request, 'incorrect.html')


from django.shortcuts import render, redirect
from blog.models import Word
import random


def test(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        correct_answer = request.session.get('correct_answer')
        if answer == correct_answer:
            return redirect('Just')
        else:
            return redirect('incorrect')
    else:
        words = list(Word.objects.all())
        sample_words = random.sample(words, 4)
        correct_word = random.choice(sample_words)
        correct_answer = correct_word.title
        pictures = correct_word.picture
        title = correct_word.title
        request.session['correct_answer'] = correct_answer

        context = {
            'words': sample_words,
            'pictures': pictures,
            'title': title,
        }
        return render(request, 'test.html', context)


def result(request):
    correct_answer = request.session.get('correct_answer')
    answer = request.POST.get('answer')
    if answer == correct_answer:
        return redirect('Just')
    else:
        return redirect('incorrect')


def Just(request):
    return render(request, 'just.html')


def incorrect(request):
    return render(request, 'incorrect.html')
