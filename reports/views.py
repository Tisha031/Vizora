import pandas as pd
import matplotlib.pyplot as plt
import io, base64

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import ReportHistory


REPORT_DATA = None


# ------------------- Upload & Process -------------------
def upload_file(request):
    global REPORT_DATA

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

           
            history = ReportHistory.objects.create(
                file_name=file.name,
                processed=False
            )

         
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            df = df.dropna()

            if len(df.columns) > 1:
                df_grouped = df.groupby(df.columns[0]).sum(numeric_only=True)
            else:
                df_grouped = df

            REPORT_DATA = df_grouped
            history.processed = True
            history.save()

           
            return redirect('report')
    else:
        form = FileUploadForm()

    return render(request, 'reports/upload.html', {'form': form})




def view_report(request):
    global REPORT_DATA
    chart = None

    if REPORT_DATA is None:
        return redirect('upload')

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))

    try:
       
        REPORT_DATA.head(5).reset_index().plot(
            x=REPORT_DATA.index.name or "index",
            y=REPORT_DATA.columns[0],
            kind='bar',
            legend=False
        )

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

    except Exception as e:
        print("Chart error:", e)

    return render(request, 'reports/report.html', {
        'columns': REPORT_DATA.columns,
        'rows': REPORT_DATA.to_html(classes='table table-striped', border=0),
        'chart': chart
    })




# ------------------- Export Report -------------------
def export_report(request, file_type):
    global REPORT_DATA
    if REPORT_DATA is None:
        return redirect('upload')

    if file_type == 'csv':
        response = HttpResponse(REPORT_DATA.to_csv(index=False), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report.csv"'
        return response
    elif file_type == 'excel':
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
        REPORT_DATA.to_excel(response, index=False)
        return response
    else:
        return HttpResponse("Invalid file type")


# ------------------- Report History -------------------
def view_history(request):
    history = ReportHistory.objects.all().order_by('-uploaded_at')
    return render(request, 'reports/history.html', {'history': history})
