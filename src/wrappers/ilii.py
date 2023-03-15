#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'reminisce')
    send_src = path.join(cc_repo, 'orca-server-mahimahi')
    recv_src = path.join(cc_repo, 'client')

    if args.option == 'deps':
        print 'libtbb-dev libasio-dev libalglib-dev libboost-system-dev'
        return

    if args.option == 'setup':

        sh_cmd = ' ./sysctl_stuff.sh && ./build.sh'
        check_call(sh_cmd, shell=True, cwd=cc_repo)
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.ip , '1', args.port]
        check_call(cmd, cwd=utils.tmp_dir)
        return




    if args.option == 'sender':
        cmd = [send_src, args.port, '~' , '20000', '0' , 'illinois', '0', 'a' , 'b', '20', 'av' , '50' , '500' , '1']
        check_call(cmd, cwd=utils.tmp_dir)
        return


if __name__ == '__main__':
    main()
