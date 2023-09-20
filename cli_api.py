import json

import click
import os
import requests

API_BASE_URL = os.environ.get('API_BASE_URL', 'http://127.0.0.1:8000/')
API_URL = f'{API_BASE_URL}/api'

@click.group()
def api_security():
    """CLI Wrapper for the security API, assigned by Paylocity"""
    pass

@click.option('-s', '--sort_date', is_flag=True, help='Sorts the results by date')
@api_security.command()
def get(sort_date: bool):
    """List all Security Features"""
    json_results = run_api('get')['results']
    if sort_date:
        json_results.sort(reverse=True, key=lambda d: d['date']) 
    click.echo(json.dumps(json_results, indent=2))

@click.option('-c', '--count', default=1, help='Number of objects to add')
@api_security.command()
def post(count: int):
    """Add one or more Security Objects"""
    json_resp = run_api('post', create_data(count))
    click.echo(json.dumps(json_resp, indent=2))

def run_api(method: str, data = None):
    assert method.lower() in ['get', 'post'], 'Not an acceptable method'
    try:
        r = requests.request(method.upper(), API_URL, json=data)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(click.style('Http Error:', fg='red'), errh)
        raise SystemExit(1)
    except requests.exceptions.ConnectionError as errc:
        print(click.style('Error Connecting:', fg='red') + errc)
        raise SystemExit(1)
    except requests.exceptions.Timeout as errt:
        print(click.style('Timeout Error:', fg='red') + errt)
        raise SystemExit(1)
    except requests.exceptions.RequestException as err:
        print(click.style('General Exception', fg='red') + err)
        raise SystemExit(1)
    return r.json()
    
        
def create_data(count: int):
    """Prompts the user for data for the number of security feature objects to be created"""
    type_choices = ['Platform']
    data = [{ 
            'name': click.prompt('Name of the security feature'),
            'type': click.prompt(
                'Type of security feature', 
                type=click.Choice(type_choices),
                show_choices=True,
                show_default=True,
                default="Platform").capitalize(),
            'description': click.prompt('Description of security feature')
        } for _ in range(count)]

    click.echo(json.dumps(data, indent=2))
    click.confirm('Are the objects correct?', abort=True)
    return data if len(data) > 1 else data[0]

if __name__ == '__main__':
    api_security(prog_name='api_security')