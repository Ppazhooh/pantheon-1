#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'c2tcp')
    send_src = path.join(cc_repo,'server')
    recv_src = path.join(cc_repo,'client')

    if args.option == 'deps':
        print 'libtbb-dev libasio-dev libalglib-dev libboost-system-dev'
        return

    if args.option == 'setup':
        utils.apply_patch('c2tcp.patch', cc_repo)
        sh_cmd = './build.sh'
        check_call(sh_cmd, shell=True, cwd=cc_repo)
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.ip , '1', args.port]
        check_call(cmd, cwd=utils.tmp_dir)
        return




    if args.option == 'sender':
        target = '60'
        tuning_period = '500'
        cmd = [send_src, args.port, target , '150', tuning_period]
        check_call(cmd, cwd=utils.tmp_dir)
        return

if __name__ == '__main__':
    main()
