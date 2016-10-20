import click
from tabulate import tabulate
from app.views import LyricsViews

pass_view = click.make_pass_decorator(LyricsViews, ensure=True)


@click.group()
def cli():
    pass


@cli.command('find')
@click.argument('search_parameters', nargs=-1)
@pass_view
def find(view, search_parameters):
    search_parameters = " ".join(search_parameters)
    results = view.search(search_parameters)

    table_headers = ['ID', 'Title', 'Artist']
    table = []

    for i in range(len(results)):
        song_id = results[i]['result']['id']
        title = results[i]['result']['title']
        artist = results[i]['result']['primary_artist']['name']

        table.append([song_id, title, artist])

    with click.progressbar(range(40000),
                           label=click.secho(
                               '\t\t\t\tLoading Data...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='yellow')
                           ) as prog_bar:
        for i in prog_bar:
            pass

    click.secho(tabulate(table, table_headers,
                         tablefmt="fancy_grid"), fg='yellow')


@cli.command('view')
@click.argument('song_id', nargs=1)
@pass_view
def view(view, song_id):
    lyrics = view.get_song_by_id(song_id)['lyrics']
    click.secho(lyrics, fg='yellow')


@cli.command('save')
@click.argument('song_id', nargs=1)
@pass_view
def save(view, song_id):
    view.save_song(song_id)


@cli.command('clear')
@pass_view
def clear(view):
    click.echo('Continue? [y/n] ', nl=False)
    c = click.getchar()
    if c == 'y':
        view.clear_db()
    if c == 'n':
        click.echo('Aborted! ', nl=False)
    else:
        click.echo('Invalid input :(')


if __name__ == '__main__':
    cli()
