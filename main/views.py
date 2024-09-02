from django.shortcuts import render, redirect
from .models import *
from .forms import QuizForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.http import HttpRequest, HttpResponse
import os

# Create your views here.


def my_view(request):
    user = request.user
    return render(request, 'layout.html', {'user': user})


def start(request):
    return render(request, 'start.html')


def eleven(request):
    return render(request, '11.html')


def elevengeo(request):
    return render(request, '11synyp/11geo.html')


def ten(request):
    return render(request, '10.html')


def tengeo(request):
    return render(request, '10synyp/10geo.html')


def nine(request):
    return render(request, '9.html')


def ninegeo(request):
    return render(request, '9synyp/9geo.html')


def eight(request):
    return render(request, '8.html')


def eightgeo(request):
    return render(request, '8synyp/8geo.html')


def seven(request):
    return render(request, '7.html')


def sevengeo(request):
    return render(request, '7synyp/7geo.html')


def six(request):
    return render(request, '6.html')


def five(request):
    return render(request, '5.html')


def four(request):
    return render(request, 'bastay/4synyp.html')


def three(request):
    return render(request, 'bastay/3synyp.html')


def two(request):
    return render(request, 'bastay/2synyp.html')


def one(request):
    return render(request, 'bastay/1synyp.html')


def index(request):
    return render(request, 'index.html')


class QuizDetailView(DetailView):
    model = Quizz
    template_name = 'quiz game/details_view.html'
    context_object_name = 'quizgame'


class QuizUpdateView(UpdateView):
    model = Quizz
    template_name = 'quiz game/create.html'

    form_class = QuizForm


class QuizDeleteView(DeleteView):
    model = Quizz
    success_url = '/quiz%20game'
    template_name = 'quiz game/quiz-delete.html'


def geopoly(request):
    return render(request, 'geopoly.html')


def alpoly(request):
    return render(request, 'alpoly.html')


def mapoly5(request):
    return render(request, '5synyp/mapoly5.html')


def test(request):
    return render(request, 'tests/test.html')


def kbnt(request):
    return render(request, 'kbnt.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quiz game')
        else:
            error = 'Форма была неверной'

    form = QuizForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'quiz game/create.html', data)


def quiz(request):
    quizs = Quizz.objects.order_by('-id')
    return render(request, 'quiz game/quiz.html', {'quizs': quizs})


class Search(ListView):

    template_name = 'quiz game/quiz.html'
    context_object_name = 'quiz'
    paginate_by = 5

    def get_queryset(self):
        return Quizz.objects.filter(title__iregex=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def onlinetaq(request):
    return render(request, 'onlinetaq.html')


def razrab(request):
    return render(request, 'razrab.html')


def synypsq(request):
    return render(request, 'qmj/synyps.html')


def bastayq(request):
    return render(request, 'qmj/qbastay.html')


def bastay(request):
    return render(request, 'bastay.html')


def qmtoq1(request):
    return render(request, 'qmj/qmtoq1.html')


def qmtoq2(request):
    return render(request, 'qmj/qmtoq2.html')


def qmtoq3(request):
    return render(request, 'qmj/qmtoq3.html')


def qmtoq4(request):
    return render(request, 'qmj/qmtoq4.html')


def qmtoq5(request):
    return render(request, 'qmj/qmtoq5.html')


def qmtoq6(request):
    return render(request, 'qmj/qmtoq6.html')


def qmtoq7(request):
    return render(request, 'qmj/qmtoq7.html')


def qmtoq8(request):
    return render(request, 'qmj/qmtoq8.html')


def qmtoq9(request):
    return render(request, 'qmj/qmtoq9.html')


def qmtoq10(request):
    return render(request, 'qmj/qmtoq10.html')


def qmtoq11(request):
    return render(request, 'qmj/qmtoq11.html')


def kornekilik(request):
    return render(request, 'kornekilik.html')


def kor5(request):
    return render(request, 'kornekilik/kor5.html')


def kor6(request):
    return render(request, 'kornekilik/kor6.html')


def kor7(request):
    return render(request, 'kornekilik/kor7.html')


def kor8(request):
    return render(request, 'kornekilik/kor8.html')


def kor9(request):
    return render(request, 'kornekilik/kor9.html')


def kor10(request):
    return render(request, 'kornekilik/kor10.html')


def kor11(request):
    return render(request, 'kornekilik/kor11.html')


def preza(request):
    return render(request, 'preza.html')


def preza5(request):
    return render(request, 'preza/preza5.html')


def preza6(request):
    return render(request, 'preza/preza6.html')


def preza7(request):
    return render(request, 'preza/preza7.html')


def preza8(request):
    return render(request, 'preza/preza8.html')


def preza9(request):
    return render(request, 'preza/preza9.html')


def preza10(request):
    return render(request, 'preza/preza10.html')


def preza11(request):
    return render(request, 'preza/preza11.html')


def synyptar(request):
    return render(request, 'synyptar.html')


def sabaq11(request):
    return render(request, 'bastay/3synyp/11.html')


def sabaq12(request):
    return render(request, 'bastay/3synyp/12.html')


def sabaq13(request):
    return render(request, 'bastay/3synyp/13.html')


def sabaq14(request):
    return render(request, 'bastay/3synyp/14.html')


def sabaq15(request):
    return render(request, 'bastay/3synyp/15.html')


def sabaq16(request):
    return render(request, 'bastay/3synyp/16.html')


def sabaq17(request):
    return render(request, 'bastay/3synyp/17.html')


def sabaq18(request):
    return render(request, 'bastay/3synyp/18.html')


def sabaq19(request):
    return render(request, 'bastay/3synyp/19.html')


def sabaq110(request):
    return render(request, 'bastay/3synyp/110.html')


def sabaq21(request):
    return render(request, 'bastay/2synyp/21.html')


def sabaq22(request):
    return render(request, 'bastay/2synyp/22.html')


def sabaq23(request):
    return render(request, 'bastay/2synyp/23.html')


def sabaq24(request):
    return render(request, 'bastay/2synyp/24.html')


def sabaq25(request):
    return render(request, 'bastay/2synyp/25.html')


def sabaq31(request):
    return render(request, 'bastay/3synyp/31.html')


def sabaq32(request):
    return render(request, 'bastay/3synyp/32.html')


def sabaq33(request):
    return render(request, 'bastay/3synyp/33.html')


def sabaq34(request):
    return render(request, 'bastay/3synyp/34.html')


def sabaq35(request):
    return render(request, 'bastay/3synyp/35.html')


def sabaq36(request):
    return render(request, 'bastay/3synyp/35.html')


def sabaq51(request):
    return render(request, '5synyp/51sabaq.html')


def sabaq52(request):
    return render(request, '5synyp/52sabaq.html')


def sabaq53(request):
    return render(request, '5synyp/53sabaq.html')


def sabaq54(request):
    return render(request, '5synyp/54sabaq.html')


def sabaq55(request):
    return render(request, '5synyp/55sabaq.html')


def sabaq56(request):
    return render(request, '5synyp/56sabaq.html')


def sabaq57(request):
    return render(request, '5synyp/57sabaq.html')


def sabaq59(request):
    return render(request, '5synyp/59sabaq.html')


def sabaq510(request):
    return render(request, '5synyp/510sabaq.html')


def sabaq511(request):
    return render(request, '5synyp/511sabaq.html')


def sabaq512(request):
    return render(request, '5synyp/512sabaq.html')


def sabaq513(request):
    return render(request, '5synyp/513sabaq.html')


def sabaq514(request):
    return render(request, '5synyp/514sabaq.html')


def sabaq515(request):
    return render(request, '5synyp/515sabaq.html')


def sabaq516(request):
    return render(request, '5synyp/516sabaq.html')


def sabaq517(request):
    return render(request, '5synyp/517sabaq.html')


def sabaq518(request):
    return render(request, '5synyp/518sabaq.html')


def sabaq520(request):
    return render(request, '5synyp/520sabaq.html')


def sabaq521(request):
    return render(request, '5synyp/521sabaq.html')


def sabaq522(request):
    return render(request, '5synyp/522sabaq.html')


def sabaq523(request):
    return render(request, '5synyp/523sabaq.html')


def sabaq524(request):
    return render(request, '5synyp/524sabaq.html')


def sabaq526(request):
    return render(request, '5synyp/526sabaq.html')


def sabaq527(request):
    return render(request, '5synyp/527sabaq.html')


def sabaq61(request):
    return render(request, '6synyp/61sabaq.html')


def sabaq62(request):
    return render(request, '6synyp/62sabaq.html')


def sabaq63(request):
    return render(request, '6synyp/63sabaq.html')


def sabaq64(request):
    return render(request, '6synyp/64sabaq.html')


def sabaq65(request):
    return render(request, '6synyp/65sabaq.html')


def sabaq66(request):
    return render(request, '6synyp/66sabaq.html')


def sabaq67(request):
    return render(request, '6synyp/67sabaq.html')


def sabaq611(request):
    return render(request, '6synyp/611sabaq.html')


def sabaq612(request):
    return render(request, '6synyp/612sabaq.html')


def sabaq613(request):
    return render(request, '6synyp/613sabaq.html')


def sabaq614(request):
    return render(request, '6synyp/614sabaq.html')


def sabaq615(request):
    return render(request, '6synyp/615sabaq.html')


def sabaq616(request):
    return render(request, '6synyp/616sabaq.html')


def sabaq617(request):
    return render(request, '6synyp/617sabaq.html')


def sabaq621(request):
    return render(request, '6synyp/621sabaq.html')


def sabaq625(request):
    return render(request, '6synyp/625sabaq.html')


def sabaq71(request):
    return render(request, '7synyp/71sabaq.html')


def sabaq72(request):
    return render(request, '7synyp/72sabaq.html')


def sabaq73(request):
    return render(request, '7synyp/73sabaq.html')


def sabaq74(request):
    return render(request, '7synyp/74sabaq.html')


def sabaq77(request):
    return render(request, '7synyp/77sabaq.html')


def sabaq712(request):
    return render(request, '7synyp/712sabaq.html')


def sabaq713(request):
    return render(request, '7synyp/713sabaq.html')


def sabaq715(request):
    return render(request, '7synyp/715sabaq.html')


def sabaq716(request):
    return render(request, '7synyp/716sabaq.html')


def sabaq717(request):
    return render(request, '7synyp/717sabaq.html')


def sabaq82(request):
    return render(request, '8synyp/82sabaq.html')


def sabaq83(request):
    return render(request, '8synyp/83sabaq.html')


def sabaq84(request):
    return render(request, '8synyp/84sabaq.html')


def sabaq85(request):
    return render(request, '8synyp/85sabaq.html')


def sabaq86(request):
    return render(request, '8synyp/86sabaq.html')


def sabaq87(request):
    return render(request, '8synyp/87sabaq.html')


def sabaq88(request):
    return render(request, '8synyp/88sabaq.html')


def sabaq92(request):
    return render(request, '9synyp/92sabaq.html')


def sabaq99(request):
    return render(request, '9synyp/99sabaq.html')


def sabaq527(request):
    return render(request, '5synyp/527sabaq.html')


def sabaq528(request):
    return render(request, '5synyp/528sabaq.html')


def sabaq102(request):
    return render(request, '10synyp/102sabaq.html')


def sabaq103(request):
    return render(request, '10synyp/103sabaq.html')


def sabaq104(request):
    return render(request, '10synyp/104sabaq.html')


def sabaq105(request):
    return render(request, '10synyp/105sabaq.html')


def sabaq106(request):
    return render(request, '10synyp/106sabaq.html')


def sabaq108(request):
    return render(request, '10synyp/108sabaq.html')


def sabaq112(request):
    return render(request, '11synyp/112sabaq.html')


def sabaq114(request):
    return render(request, '11synyp/114sabaq.html')


def sabaq114geo(request):
    return render(request, '11synyp/11geo/114sabaqgeo.html')


def sabaq104geo(request):
    return render(request, '10synyp/10geo/104sabaqgeo.html')


def sabaq105geo(request):
    return render(request, '10synyp/10geo/105sabaqgeo.html')


def sabaq91geo(request):
    return render(request, '9synyp/9geo/91sabaqgeo.html')


def sabaq92geo(request):
    return render(request, '9synyp/9geo/92sabaqgeo.html')


def sabaq94geo(request):
    return render(request, '9synyp/9geo/94sabaqgeo.html')


def sabaq81geo(request):
    return render(request, '8synyp/8geo/81sabaqgeo.html')


def sabaq82geo(request):
    return render(request, '8synyp/8geo/82sabaqgeo.html')


def sabaq83geo(request):
    return render(request, '8synyp/8geo/83sabaqgeo.html')


def sabaq84geo(request):
    return render(request, '8synyp/8geo/84sabaqgeo.html')


def sabaq85geo(request):
    return render(request, '8synyp/8geo/85sabaqgeo.html')


def sabaq86geo(request):
    return render(request, '8synyp/8geo/86sabaqgeo.html')


def sabaq87geo(request):
    return render(request, '8synyp/8geo/87sabaqgeo.html')


def sabaq71geo(request):
    return render(request, '7synyp/7geo/71sabaqgeo.html')


def sabaq73geo(request):
    return render(request, '7synyp/7geo/73sabaqgeo.html')


def sabaq74geo(request):
    return render(request, '7synyp/7geo/74sabaqgeo.html')


def sabaq75geo(request):
    return render(request, '7synyp/7geo/75sabaqgeo.html')


def sabaq76geo(request):
    return render(request, '7synyp/7geo/76sabaqgeo.html')


def sabaq77geo(request):
    return render(request, '7synyp/7geo/77sabaqgeo.html')


def sabaq78geo(request):
    return render(request, '7synyp/7geo/78sabaqgeo.html')


def sabaq79geo(request):
    return render(request, '7synyp/7geo/79sabaqgeo.html')
