from django import forms


class IDAndItem(forms.Form):

    student_id = forms.CharField(
        max_length=20,
        label="Student ID",
        widget=forms.TextInput(
            attrs={
                "class": "validate",
                "onkeyup": "moveOnMax(this, this.id)",
                "id": "student_id",
            }
        )
    )
    item = forms.CharField(
        max_length=20,
        label="Item",
        widget=forms.TextInput(
            attrs={
                "class": "validate",
                "onkeyup": "moveOnMax(this, this.id)",
                "id": "item",
            }
        )
    )
