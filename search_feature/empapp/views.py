
from django.shortcuts import render
from .models import Employee

def employee_search(request, lookup_field, lookup_type, search_term):
    valid_lookup_fields = ['fname', 'lname', 'age', 'address']
    valid_lookup_types = ['startswith', 'contains', 'lte']

    if lookup_field not in valid_lookup_fields or lookup_type not in valid_lookup_types:
        return render(request, 'empapp/error.html', {'error_message': 'Invalid lookup parameters'})

    filter_param = f"{lookup_field}__{lookup_type}"
    filter_value = search_term

    if lookup_type == 'lte' and not search_term.isdigit():
        return render(request, 'empapp/error.html', {'error_message': 'Invalid age value'})

    results = Employee.objects.filter(**{filter_param: filter_value})
    context = {
        'results': results,
        'lookup_field': lookup_field,
        'lookup_type': lookup_type,
        'search_term': search_term,
    }
    return render(request, 'empapp/employee_search_results.html', context)
