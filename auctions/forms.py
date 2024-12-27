from django import forms

class AuctionListingForm(forms.Form):
    # Form field for the title of the auction listing
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Give it a title'
        })
    )

    # Form field for the category of the auction listing (optional)
    category = forms.CharField(
        label='Category',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category (optional)'
        })
    )

    # Form field for the estimated price of the item (optional)
    price = forms.DecimalField(
        label='Price',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Estimated price (optional)',
            'min': '0.01',
            'max': '999999999.99',
            'step': '0.01'
        })
    )

    # Form field for the starting bid (required)
    starting_bid = forms.DecimalField(
        label='Starting Bid',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting bid',
            'min': '0.01',
            'max': '99999999999.99',
            'step': '0.01'
        })
    )

    # Form field for the image URL of the item (optional)
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        initial='https://i.imghippo.com/files/bQyI7776Dg.webp',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Image URL (optional)',
        })
    )

    # Form field for the description of the item (required)
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Tell more about the product',
            'rows': '3'
        })
    )

    # Custom validation for the starting_bid field
    def clean_starting_bid(self):
        amount = float(self.cleaned_data.get('starting_bid'))
        if isinstance(amount, float) and amount > 0:
            return amount
        raise forms.ValidationError('Should be a number larger than zero!')

    # Custom processing for the category field to return lowercase value
    def clean_category(self):
        category = self.cleaned_data.get('category')
        return category.lower()

class CommentForm(forms.Form):
    # Form field for the comment text (required)
    text = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control comment',
            'rows': '3',
            'cols': '100'
        })
    )

    # Custom validation for the text field
    def clean_comment(self):
        text = self.cleaned_data.get('text')
        if len(text) > 0:
            return text
        return self.errors