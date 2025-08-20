from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel/CSV File")

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.xlsx', '.csv')):
            raise forms.ValidationError("Only .xlsx or .csv files are allowed.")
        if file.size > 5 * 1024 * 1024:  # 5 MB limit
            raise forms.ValidationError("File too large (max 5 MB).")
        return file
