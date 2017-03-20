import argparse
import logging
import os
import pwd
import subprocess

from mbse.parser import parse_struct
import mbse.fmt.users_data as users_data

def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('--mbse-root', '-r', default='/opt/mbse')
    p.add_argument('--users', '-u')
    p.add_argument('--shell', '-S')
    p.add_argument('--home', '-H')

    return p.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level='INFO')
    log = logging.getLogger(__name__)

    if args.users is None:
        args.users = os.path.join(args.mbse_root, 'etc', 'users.data')

    if args.shell is None:
        args.shell = os.path.join(args.mbse_root, 'bin', 'mbsebbs')

    if args.home is None:
        args.home = os.path.join(args.mbse_root, 'home')

    with open(args.users, 'r') as fd:
        hdr = parse_struct(users_data.fmt_userhdr, fd)

        while True:
            try:
                user = parse_struct(users_data.fmt_userrec, fd)

                # skip deleted users
                if user['flags1'] & users_data.FLAG_DELETED:
                    continue

                user['Name'] = user['Name'].rstrip('\0')
                user['sUserName'] = user['sUserName'].rstrip('\0')
                user['Password'] = user['Password'].rstrip('\0')

                # check if users exists
                try:
                    pwd.getpwnam(user['Name'])
                    log.info('user %s already exists', user['Name'])
                except KeyError:
                    log.info('creating user %s', user['Name'])
                    subprocess.check_call([
                        'useradd',
                        '-c', user['sUserName'],
                        '-d', os.path.join(args.home, user['Name']),
                        '-s', args.shell,
                        '-g', 'bbs',
                        '-M', '-N',
                        user['Name']
                    ])

                    log.info('fixing permissions on home directory')
                    subprocess.check_call([
                        'chown', '-R', user['Name'],
                        os.path.join(args.home, user['Name'])])

                    log.info('setting password for user %s', user['Name'])
                    p = subprocess.Popen(['passwd', '--stdin', user['Name']],
                                         stdin=subprocess.PIPE)

                    p.communicate(input=user['Password'])
            except EOFError:
                break
if __name__ == '__main__':
    main()

