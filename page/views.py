from django.shortcuts import render
from .models import Sale_assistant, Customer, Transaction
import pandas as pd
from plotly.offline import plot
import plotly.express as px

# def index(request):
#     qs = Project.objects.all()
#     projects_data = [
#         {
#             'Project':x.name,
#             'Start':x.start_date,
#             'Finish':x.end_date,
#             'Responsible':x.responsible,
#         } for x in qs
#     ]
#     df = pd.DataFrame(projects_data)
#     fig = px.timeline(
#         df,x_start='Start',x_end='Finish',y='Project',color='Responsible'
#     )
#
#     fig.update_yaxes(autorange='reversed')
#     gantt_plot = plot(fig,output_type='div')
#     context = {'plot_div':gantt_plot}
#
#
#     return render(request, 'page/index.html',context)

def index(request):
    return render(request,'pages/index.html')
def about(request):
    return render(request,'pages/about.html')


def annually_statistic(request):
    ...


def daily_statistics(request):
    ...



