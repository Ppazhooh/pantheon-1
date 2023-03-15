#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'Reminis')
    send_src = path.join(cc_repo, 'server')
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
        report_period = '20000' #equal to min_rtt (ms * 1000)
        queue_threshold = '1'
        cmd = [send_src, args.port, report_period, '0' , 'cubic', '2', queue_threshold]
        check_call(cmd, cwd=utils.tmp_dir)
        return


if __name__ == '__main__':
    main()
