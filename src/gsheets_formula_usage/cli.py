"""Command line interface to interact with GSheets Formula Usage tool."""
import click
from gsheets_formula_usage import Index, get_service


@click.command()
@click.argument('spreadsheet_id', required=True)
def get_usage(spreadsheet_id: str):
    """Find formulas used in a given Google spreadsheet."""
    service = get_service()
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id, includeGridData=True).execute()

    for sheet in spreadsheet['sheets']:
        title = sheet['properties']['title']
        for layer in sheet['data']:
            for n, row in enumerate(layer.get('rowData', [])):
                for m, value in enumerate(row.get('values', [])):
                    formula_value = value.get('userEnteredValue', {}).get('formulaValue')
                    if formula_value is not None:
                        formula_value_oneliner = formula_value.replace('\n', '\\n')
                        print(f'{title}!{Index.to_letter(m)}{Index.to_number(n)}: {formula_value_oneliner}')
