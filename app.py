import cmd
import click
from tabulate import tabulate
from app.views import LyricsViews

view = LyricsViews()


class AppRun(cmd.Cmd):
    prompt = "Neuro>>"

    def do_find(self, search_parameters):
        """
        Returns a list of songs that match the search criteria
        """
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
                                   '\t\t\t\tLoading Data...',
                                   blink=True,
                                   bold=True),
                               fill_char=click.style('  ', bg='yellow')
                               ) as prog_bar:
            for i in prog_bar:
                pass

        click.secho(tabulate(table, table_headers,
                             tablefmt="fancy_grid"), fg='yellow')

    def do_view(self, song_id):
        """
        View song lyrics based on it's id.
        """
        lyrics = view.get_song_by_id(song_id)['lyrics']
        click.secho(lyrics, fg='yellow')

    def do_save(self, song_id):
        """
        Store song details and lyrics locally.
        """
        view.save_song(song_id)
        click.echo('Song Saved Succesfully\n ', nl=False) 

    # Clear Database
    def do_clear(self, line):
        click.echo('Continue? [y/n]\n ', nl=False)
        c = click.getchar()
        if c == 'y':
            view.clear_db()
            click.echo('Database Cleared Succesfully\n ', nl=False)
        elif c == 'n':
            click.echo('Aborted\n ', nl=False)
        else:
            click.echo('Invalid input :(')

    # Clear command line
    def do_cls(self, arg):
        click.clear()

    def do_EOF(self):
        # Exit
        return True


if __name__ == '__main__':
    try:
        AppRun().cmdloop()

    except KeyboardInterrupt:
        with click.progressbar(range(2000),
                               label=click.secho(
                               '\t\t\t\tExiting...',
                               blink=True,
                               bold=True),
                               fill_char=click.style('  ',
                               bg='red')) as prog_bar:
            for i in prog_bar:
                pass
