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

    click.echo(tabulate(table, table_headers, tablefmt="fancy_grid"))


@cli.command('view')
@click.argument('song_id', nargs=1)
@pass_view
def view(view, song_id):
    lyrics = view.get_song_by_id(song_id)['lyrics']
    print(lyrics)


@cli.command('save')
@click.argument('song_id', nargs=1)
@pass_view
def save(view, song_id):
    view.save_song(song_id)


@cli.command('clear')
@pass_view
def clear(view):
    view.clear_db()


if __name__ == '__main__':
    cli()
